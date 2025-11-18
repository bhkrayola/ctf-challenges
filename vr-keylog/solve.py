import csv
import numpy as np
import sys

def parseSource(filePath):
    timestamps = []
    positions = []
    orientations = []
    keystrokes = []
    with open(filePath, newline='') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            firstField = row[0].strip()
            if firstField == 'Keystroke':
                label = row[1].strip()
                if label == 'Space_Button':
                    label = ' '
                try:
                    timeVal = float(row[2].strip())
                    keystrokes.append((label, timeVal))
                except:
                    pass
            else:
                try:
                    timeVal = float(row[0].strip())
                    posRaw = ",".join(row[2:5]).strip().lstrip("(").rstrip(")")
                    px, py, pz = [float(x) for x in posRaw.split(",")]
                    oriRaw = ",".join(row[5:9]).strip().lstrip("(").rstrip(")")
                    qx, qy, qz, qw = [float(x) for x in oriRaw.split(",")]
                    timestamps.append(timeVal)
                    positions.append((px, py, pz))
                    orientations.append((qx, qy, qz, qw))
                except:
                    pass
    return timestamps, positions, orientations, keystrokes

def parseUnknown(filePath):
    timestamps = []
    positions = []
    orientations = []
    with open(filePath, newline='') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if not row:
                continue
            firstField = row[0].strip().lower()
            if firstField == 'answer':
                continue
            else:
                try:
                    timeVal = float(row[0].strip())
                    posRaw = ",".join(row[2:5]).strip().lstrip("(").rstrip(")")
                    px, py, pz = [float(x) for x in posRaw.split(",")]
                    oriRaw = ",".join(row[5:9]).strip().lstrip("(").rstrip(")")
                    qx, qy, qz, qw = [float(x) for x in oriRaw.split(",")]
                    timestamps.append(timeVal)
                    positions.append((px, py, pz))
                    orientations.append((qx, qy, qz, qw))
                except:
                    pass
    return timestamps, positions, orientations
def quatInverse(q):
    x, y, z, w = q
    normSq = x*x + y*y + z*z + w*w
    return (-x/normSq, -y/normSq, -z/normSq, w/normSq)

def quatMultiply(a, b):
    ax, ay, az, aw = a
    bx, by, bz, bw = b
    x = aw*bx + ax*bw + ay*bz - az*by
    y = aw*by - ax*bz + ay*bw + az*bx
    z = aw*bz + ax*by - ay*bx + az*bw
    w = aw*bw - ax*bx - ay*by - az*bz
    return (x, y, z, w)

def pitchAndRoll(o):
    x, y, z, w = o
    pitch = np.arctan2(2*(w*x + y*z), 1 - 2*(x*x + y*y))
    roll = np.arcsin(2*(w*y - z*x))
    return pitch, roll

def rotationMatrix(pitch, roll):
    rp = np.array([
        [np.cos(pitch), 0, np.sin(pitch)],
        [0, 1, 0],
        [-np.sin(pitch), 0, np.cos(pitch)]
    ])
    rr = np.array([
        [1, 0, 0],
        [0, np.cos(roll), -np.sin(roll)],
        [0, np.sin(roll), np.cos(roll)]
    ])
    return rp @ rr

def estimateCursor(position, orientation):
    pr, rl = pitchAndRoll(orientation)
    R = rotationMatrix(pr, rl)
    rel = np.array([position[0], position[1], position[2] - 2.0]) #computing points 2 units in front of the controller :)
    return R @ rel

def recoverMessage(sourceFile, unknownFile):
    sourceTs, sourcePs, sourceOs, sourceKs = parseSource(sourceFile)
    unknownTs, unknownPs, unknownOs = parseUnknown(unknownFile)

    firstUnknownTime = unknownTs[0]
    sourceTimeForT = None
    for label, t in sourceKs:
        if label == 't':
            sourceTimeForT = t
            break

    idxSource = min(range(len(sourceTs)), key=lambda i: abs(sourceTs[i] - sourceTimeForT))
    idxUnknown = min(range(len(unknownTs)), key=lambda i: abs(unknownTs[i] - firstUnknownTime))
    quatSource = sourceOs[idxSource]
    quatUnknown = unknownOs[idxUnknown]

    globalQuat = quatMultiply(quatUnknown, quatInverse(quatSource))
    invQuat = quatInverse(globalQuat)

    def quatToMatrix(q):
        x, y, z, w = q
        return np.array([
            [1 - 2*y*y - 2*z*z, 2*x*y - 2*z*w,     2*x*z + 2*y*w],
            [2*x*y + 2*z*w,     1 - 2*x*x - 2*z*z, 2*y*z - 2*x*w],
            [2*x*z - 2*y*w,     2*y*z + 2*x*w,     1 - 2*x*x - 2*y*y]
        ])

    invRotMat = quatToMatrix(invQuat)
    alignedPositions = []
    alignedOrientations = []
    for posU, oriU in zip(unknownPs, unknownOs):
        pAligned = invRotMat @ np.array(posU)
        alignedPositions.append(tuple(pAligned.tolist()))
        qAligned = quatMultiply(invQuat, oriU)
        qArr = np.array(qAligned)
        qArr /= np.linalg.norm(qArr)
        alignedOrientations.append(tuple(qArr.tolist()))

    pathSource = np.array([estimateCursor(p, o) for p, o in zip(sourcePs, sourceOs)])
    pathUnknown = np.array([estimateCursor(p, o) for p, o in zip(alignedPositions, alignedOrientations)])

    srcKeyPos = []
    sourceKeyLabels = []
    for lbl, t in sourceKs:
        idx = min(range(len(sourceTs)), key=lambda i: abs(sourceTs[i] - t))
        srcKeyPos.append(pathSource[idx])
        sourceKeyLabels.append(lbl)
    srcKeyPos = np.array(srcKeyPos)

    uKeyPos = []
    for t in unknownTs:
        idx = min(range(len(unknownTs)), key=lambda i: abs(unknownTs[i] - t))
        uKeyPos.append(pathUnknown[idx])
    uKeyPos = np.array(uKeyPos)

    guessedLabels = []
    for pt in uKeyPos:
        dists = np.linalg.norm(srcKeyPos - pt, axis=1)
        bestIdx = np.argmin(dists)
        guessedLabels.append(sourceKeyLabels[bestIdx])

    outputChars = []
    i = 0
    braceFlip = 0
    while i < len(guessedLabels):
        if guessedLabels[i] == ' ':
            if i + 1 < len(guessedLabels) and guessedLabels[i+1] == ' ':
                outputChars.append('{' if braceFlip == 0 else '}')
                braceFlip ^= 1
                i += 2
            else:
                outputChars.append('_')
                i += 1
        else:
            outputChars.append(guessedLabels[i])
            i += 1

    return "".join(outputChars)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python solve.py source.txt unknown.txt")
        sys.exit(1)
    print(recoverMessage(sys.argv[1], sys.argv[2]))

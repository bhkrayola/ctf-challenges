#!/usr/local/bin/python

import sys
import select

def input_with_timeout(prompt, timeout=30):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    ready, _, _ = select.select([sys.stdin], [], [], timeout)
    if ready:
        return sys.stdin.buffer.readline().rstrip(b'\n').decode('utf-8')
    raise Exception("Timed out!")

def coding_challenge():
    print("\nCoding Challenge:")
    print("Here’s a vulnerable Solidity function:")
    print("""
    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        (bool sent, ) = msg.sender.call{value: amount}("");
        require(sent, "Failed to send Ether");
        balances[msg.sender] -= amount;
    }
    """)
    print("\nFix the vulnerability. There are multiple correct solutions")
    #print("1. Move the balances[msg.sender] -= amount; line above the external call.")
    #print("2. Use the nonReentrant modifier to block recursive calls.")
    print("\nWrite your Solidity code and type 'END' on a new line to finish.")

    code_lines = []
    while True:
        try:
            line = input_with_timeout(">>> ", timeout=120).strip()
            if line.upper() == "END":
                break
            code_lines.append(line)
        except Exception as e:
            print("\nError or timeout. Please try again.")
            return False

    user_code = "\n".join(code_lines)

    if "balances[msg.sender] -= amount" in user_code and user_code.find("balances[msg.sender] -= amount") < user_code.find("call"):
        print("\nGood job! You moved the balance update correctly.")
        return True
    elif "nonReentrant" in user_code:
        print("\nGood job! You used the nonReentrant modifier.")
        return True
    else:
        print("\nYour solution is missing a key fix (skill issue). Review your code and try again.")
        return False

def main():
    flag = "flag{secure_contracts_master}"
    questions = [
        "Are you going to use ChatGPT for this quiz and the subsequent coding challenge?",
        "What is the smallest unit of Bitcoin called?",
        "What data type in Solidity is used to store Ether balances?",
        "What is the term for the fee paid to miners for validating a transaction?",
        "What is the term for a temporary split in the blockchain caused by differing versions of the chain?",
        "What is the most widely used token standard in Ethereum?",
        "What is the web-based development environment commonly used to write, compile, and deploy Ethereum smart contracts?"
    ]
    answers = [
        "No",
        "Satoshi",
        "uint",
        "Gas",
        "Fork",
        "ERC-20",
        "Remix"
    ]
    
    print("Blockchain Quiz 2.0: Interactive Edition mwhahhahahahah")
    print("Answer the questions correctly and complete the coding challenge to get the flag.")
    
    for i in range(len(questions)):
        print()
        print(f"Question {i+1}:")
        print(questions[i])
        answer = input("Your answer: ").replace(" ", "").replace("-", "").lower()
        if answer!=answers[i].replace(" ", "").replace("-", "").lower():
            print("Incorrect answer! you have to restart >:(")
            quit()

    print("\nYou've answered all questions correctly! Now, onto the coding challenge.")
    if coding_challenge():
        print("\nwow. you really are a blockchain pro. you might even be able to take on cheeseballman427. \n Here is your flag:")
        print(flag)
    else:
        print("\nThe coding challenge was incomplete or incorrect (skill issue). Better luck next time!")

if __name__ == "__main__":
    main()

#Brian Ho 11/15/24

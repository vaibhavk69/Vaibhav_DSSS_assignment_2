import random


def getNumber(min, max): # changing method name according to relevance
    """
    Random integer.
    """
    return random.randint(min, max)     # to get random numbers within the specified range


def getOperation():  # changing this method name since it returns what operation is to be performed
    return random.choice(['+', '-', '*'])  # to get the a random operation from the list i.e. +, - and *


def caculate(num1, num2, operation): # changing the method name according to action it performs 
    try:
        problem = f"{num1} {operation} {num2}"
        if operation == '+': ans = num1 + num2    # correcting the operation performed for + and - (* is correct)
        elif operation == '-': ans = num1 - num2
        else: ans = num1 * num2
        return problem, ans   
    except Exception as e:
        print(f"error :: {e}")

def math_quiz():
    score = 0     # changing the variable name and make it more understandable
    total_ques = 3
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    try:
        for _ in range(total_ques):
            num1 = getNumber(1, 10); num2 = getNumber(1, round(5.5)); operation = getOperation()

            PROBLEM, ANSWER = caculate(num1, num2, operation)
            print(f"\nQuestion: {PROBLEM}")
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)

            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                score+=1   
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")
    except Exception as e:       # this exception catches all the i/o error as well as other errors like array-out-of-bound-exception, etc.
        print(f"error :: {e}")

    print(f"\nGame over! Your score is: {score}/{total_ques}")

if __name__ == "__main__":
    math_quiz()

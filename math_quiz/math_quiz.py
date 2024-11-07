import random


def getNumber(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def getOperation():
    return random.choice(['+', '-', '*'])


def caculate(num1, num2, operation):
    try:
        problem = f"{num1} {operation} {num2}"
        if operation == '+': ans = num1 + num2
        elif operation == '-': ans = num1 - num2
        else: ans = num1 * num2
        return problem, ans
    except:
        print("wrong inputs")

def math_quiz():
    score = 0
    total_ques = 3
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_ques):
        num1 = getNumber(1, 10); num2 = getNumber(1, round(5.5)); operation = getOperation()

        PROBLEM, ANSWER = caculate(num1, num2, operation)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s+=1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_ques}")

if __name__ == "__main__":
    math_quiz()

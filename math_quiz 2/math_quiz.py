import random


def generate_random_integer(minimum, maximum):
    # Generates a random integer within the range.
    return random.randint(minimum, maximum)


def generate_random_operator():
    #Generates a random operator (+, -, or *).
    return random.choice(['+', '-', '*'])


def calculate_result(number1, number2, operator):
    #Calculates the result of a mathematical expression.
    expression = f"{number1} {operator} {number2}"
    
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2
    
    return expression, result


def math_quiz():
    #Conducts a simple math quiz game.
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = generate_random_integer(1, 10)
        number2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = calculate_result(number1, number2, operator)

        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()

# Define questions and answers
questions = [
    "What is the capital of France?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the chemical symbol for water?",
    "What is the tallest mammal?",
    "What is the currency of Japan?"
]

options = [
    ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
    ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Leo Tolstoy"],
    ["A. W", "B. O", "C. H2O", "D. CO2"],
    ["A. Elephant", "B. Giraffe", "C. Lion", "D. Tiger"],
    ["A. Yuan", "B. Won", "C. Yen", "D. Rupee"]
]

answers = ["B", "A", "C", "B", "C"]

# Function to display questions
def display_question(question, options):
    print(question)
    for option in options:
        print(option)

# Function to check answer
def check_answer(answer, user_answer):
    if answer.upper() == user_answer.upper():
        print("Correct answer!")
        return True
    else:
        print("Wrong answer!")
        return False

# Main function
def main():
    print("Welcome to Kaun Banega Crorepati!")
    print("Game Begins!!!!!!")
    print("You will be asked 5 questions.")

    score = 0
    for i in range(len(questions)):
        print(f"Question {i+1}:")
        display_question(questions[i], options[i])
        user_answer = input("Your answer (Enter A/B/C/D): ")
        if check_answer(answers[i], user_answer):
            score += 1
            print("Congratulation your answer is right")

        else:
            print("Oops!! its wrong")
            break

    print("Quiz ended!")
    print(f"Your final score is: {score}/5")

if __name__ == "__main__":
    main()


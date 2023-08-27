import random
question_bank = [
    {
        "question": "What is the capital of India?",
        "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"],
        "correct_answer": "New Delhi",
    },
    {
        "question": "Which gas do plants use for photosynthesis?",
        "options": ["Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen"],
        "correct_answer": "Carbon Dioxide",
    },
    {
        "question": "What does the expression `'Python' * 3` evaluate to?",
        "options": ["PythonPythonPython", "Python3", "Python,Python,Python", "TypeError"],
        "correct_answer": "PythonPythonPython",
    }
    # Add more
]

def display_question(question_data):
    print(question_data["question"])
    for i in range(len(question_data["options"])):
        option = question_data["options"][i]
        print(f"{i + 1}. {option}")

level_winnings = [1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,500000,1000000]
def game():
    print("Welcome to Kaun Banega Crorepati!")
    total_winnings = level = 0

    # Shuffle the question bank to present questions in random order
    random.shuffle(question_bank)

    for question_data in question_bank:
        display_question(question_data)

        # Get user's answer choice
        user_choice = int(input("Enter your choice (1-4): "))

        # Validate user input
        if user_choice < 1 or user_choice > 4:
            print("Invalid choice. Please enter a valid choice.")
            continue

        selected_option = question_data["options"][user_choice - 1]

        if selected_option == question_data["correct_answer"]:
            total_winnings = level_winnings[level]
            print("Correct answer! You won", total_winnings, "points.\n")
            level += 1
        else:
            print("Sorry, that's incorrect. The correct answer was:", question_data["correct_answer"], "\n")
            break

    print("Congratulations! You won a total of", total_winnings, "points.")
    print("Thank you for playing!")

if __name__ == "__main__":
    game()
import random

question_bank = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Bangalore", "Kolkata"],
        "correct_answer": "New Delhi"
    },
    {
        "question": "Which river is known as the Ganga in India?",
        "options": ["Yamuna", "Brahmaputra", "Indus", "Ganges"],
        "correct_answer": "Ganges"
    },
    {
        "question": "Which famous monument in India is also known as the 'Symbol of Love'?",
        "options": ["Red Fort", "Hawa Mahal", "Qutub Minar", "Taj Mahal"],
        "correct_answer": "Taj Mahal"
    },
    {
        "question": "In which state of India is the city of Jaipur located?",
        "options": ["Rajasthan", "Kerala", "Gujarat", "Madhya Pradesh"],
        "correct_answer": "Rajasthan"
    },
    {
        "question": "Which festival is celebrated by lighting oil lamps in India?",
        "options": ["Diwali", "Holi", "Eid", "Christmas"],
        "correct_answer": "Diwali"
    },
    {
        "question": "Who is known as the 'Father of the Nation' in India?",
        "options": ["Jawaharlal Nehru", "Sardar Patel", "Subhas Chandra Bose", "Mahatma Gandhi"],
        "correct_answer": "Mahatma Gandhi"
    },
    {
        "question": "Which Indian cricketer has the nickname 'Captain Cool'?",
        "options": ["Sachin Tendulkar", "Virat Kohli", "Rahul Dravid", "MS Dhoni"],
        "correct_answer": "MS Dhoni"
    },
    {
        "question": "Which Indian festival is known for the colorful decoration of kites?",
        "options": ["Navratri", "Pongal", "Makar Sankranti", "Eid"],
        "correct_answer": "Makar Sankranti"
    },
    {
        "question": "What is the currency of India?",
        "options": ["Dollar", "Pound", "Euro", "Rupee"],
        "correct_answer": "Rupee"
    },
    {
        "question": "Which Indian state is famous for the backwaters and houseboats?",
        "options": ["Goa", "Kerala", "Tamil Nadu", "Himachal Pradesh"],
        "correct_answer": "Kerala"
    }
]

def display_question(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data["options"], start=1):
        print(f"{i}. {option}")

def fifty_fifty_lifeline(question_data):
    # Create a copy of the options list
    options_copy = question_data["options"][:]
    
    # Remove two incorrect options randomly
    options_copy.remove(question_data["correct_answer"])
    incorrect_option = random.choice(options_copy)
    options_copy.remove(incorrect_option)
    
    # Display the updated options
    print(question_data["question"])
    for i, option in enumerate(options_copy, start=1):
        print(f"{i}. {option}")

level_winnings = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 500000, 1000000]

def game():
    print("Welcome to Kaun Banega Crorepati!")
    total_winnings = level = 0

    # Shuffle the question bank to present questions in random order
    random.shuffle(question_bank)

    for question_data in question_bank:
        display_question(question_data)

        # Get user's choice including lifeline option
        user_choice = int(input("Enter your choice (1-4, or 5 for 50-50 lifeline): "))

        if user_choice == 5:
            # Use the 50-50 lifeline
            fifty_fifty_lifeline(question_data)
            user_choice = int(input("Enter your choice (1 or 2): "))

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

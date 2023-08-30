import random

question_bank = [
  {
"question": "What is the result of 5 + 7?",
"options": ["12", "57", "35", "None of the above"],
"correct_answer": "12"
}
,
{
"question": "Which data type is used to store a single character in Python?",
"options": ["char", "character", "str", "single"],
"correct_answer": "str"
}
,
{
"question": "What is the output of print('Hello, ' + 'world!')?",
"options": ["Hello, world!", "Hello, + world!", "Hello, world!", "Hello, world! "],
"correct_answer": "Hello, world!"
}
,
{
"question": "How do you start a multiline comment in Python?",
"options": ["/*", "#", "//", "'''"],
"correct_answer": "'''"
}
,
{
"question": "What is the result of len('Python')?",
"options": ["6", "5", "7", "TypeError"],
"correct_answer": "6"
}
,
{
"question": "Which keyword is used to define a function in Python?",
"options": ["def", "function", "define", "fun"],
"correct_answer": "def"
}
,
{
"question": "What is the output of 2 ** 3?",
"options": ["8", "6", "9", "23"],
"correct_answer": "8"
}
,
{
"question": "What does the expression True and False evaluate to?",
"options": ["True", "False", "None", "Error"],
"correct_answer": "False"
}
,
{
"question": "Which built-in function is used to sort a list in Python?",
"options": ["sort()", "order()", "sorted()", "arrange()"],
"correct_answer": "sorted()"
}
,
{
"question": "What is the result of 10 / 2?",
"options": ["5.0", "5", "2.5", "2"],
"correct_answer": "5.0"
}
,
{
"question": "Which symbol is used for single-line comments in Python?",
"options": ["//", "#", "/*", "%%"],
"correct_answer": "#"
}
,
{
"question": "What does the pop() method do in Python?",
"options": ["Adds an element to a list", "Removes the last element from a list", "Deletes a variable", "Performs a mathematical operation"],
"correct_answer": "Removes the last element from a list"
}
,
{
"question": "What is the output of print(len([1, 2, 3]))?",
"options": ["6", "3", "2", "TypeError"],
"correct_answer": "3"
}
,
{
"question": "Which operator is used to perform exponentiation in Python?",
"options": ["^", "", "*", "^^"],
"correct_answer": ""
}
,
{
"question": "What is the result of 3 != 5?",
"options": ["True", "False", "None", "Error"],
"correct_answer": "True"
}


    
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
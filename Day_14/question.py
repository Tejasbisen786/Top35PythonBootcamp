question_set = [
    {
        "que_no": 1,
        "que_title": "What is the capital of France?",
        "que_options": ["London", "Paris", "Berlin", "Madrid"],
        "correct_ans": "Paris"
    },
    {
        "que_no": 2,
        "que_title": "Which planet is known as the Red Planet?",
        "que_options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_ans": "Mars"
    },
    {
        "que_no": 3,
        "que_title": "What is the largest mammal?",
        "que_options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct_ans": "Blue Whale"
    }
]


for question in question_set:
    print(f"Question {question['que_no']}: {question['que_title']}")
    for i, option in enumerate(question['que_options'], start=1):
        print(f"{i}. {option}")
    print(f"Correct Answer: {question['correct_ans']}")
    print()
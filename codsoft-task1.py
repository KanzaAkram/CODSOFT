import random

# Define quiz questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Madrid", "Paris", "Berlin"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Lion"],
        "correct_answer": "Blue Whale"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "correct_answer": "Carbon Dioxide"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy"],
        "correct_answer": "William Shakespeare"
    },
]

# Initialize variables
score = 0
lifelines = 1  # User has one 50-50 lifeline

# Display welcome message and rules
print("**********Welcome to the Quiz Game!**********")
print("You will be asked multiple-choice questions. Try to get as many correct as you can!")
print("You have one 50-50 lifeline. You can use it at any time by typing '50-50' as your answer.\n")

# Shuffle the order of questions
random.shuffle(quiz_questions)

# Present quiz questions
for index, question_data in enumerate(quiz_questions, start=1):
    print(f"Question {index}: {question_data['question']}")
    for i, option in enumerate(question_data["options"], start=1):
        print(f"{i}. {option}")
    
    while True:
        user_answer = input("Enter the number of your answer or type '50-50' for a lifeline: ")

        if user_answer.lower() == "50-50":
            if lifelines > 0:
                # Implement the 50-50 lifeline
                options_copy = question_data["options"][:]  # Create a copy of options
                correct_answer_index = options_copy.index(question_data["correct_answer"])
                options_copy.pop(correct_answer_index)  # Remove the correct answer
                incorrect_answers = random.sample(options_copy, 2)  # Select 2 incorrect answers to remove
                options_to_remove = [incorrect_answers[0], incorrect_answers[1]]
                for option in question_data["options"]:
                    if option not in options_to_remove:
                        print(f"{question_data['options'].index(option) + 1}. {option}")
                lifelines -= 1
            else:
                print("You have already used your 50-50 lifeline.\n")
        else:
            try:
                user_answer_index = int(user_answer) - 1
                correct_answer_index = question_data["options"].index(question_data["correct_answer"])

                if user_answer_index == correct_answer_index:
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is: {question_data['correct_answer']}\n")

                break  # Move to the next question

            except ValueError:
                print("Invalid input. Please enter a number or '50-50'.\n")

# Calculate the final score
total_questions = len(quiz_questions)
percentage_score = (score / total_questions) * 100

# Display final results
print(f"Quiz completed!\nYour score: {score}/{total_questions} ({percentage_score:.2f}%)")

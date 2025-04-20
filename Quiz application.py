def run_quiz(questions):
    score = 0
    total_questions = 0

    for question in questions:
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)

        answer = input(
            "Enter your answer (A, B, C, D) or type 'EXIT' to quit: ").strip().upper()

        if answer == "EXIT":
            print("\nYou chose to exit the quiz.")
            print(f"Final Score: {score} out of {total_questions}")
            return  # Exit immediately

        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.\n")

        total_questions += 1

    print(
        f"Quiz Finished! You got {score} out of {total_questions} questions correct.")


questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Au", "B. Ag", "C. Fe", "D. Hg"],
        "answer": "A"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Mark Twain", "B. J.K. Rowling", "C. William Shakespeare", "D. Jane Austen"],
        "answer": "C"
    },
    {
        "question": "What is the speed of light?",
        "options": ["A. 300,000 km/s", "B. 150,000 km/s", "C. 450,000 km/s", "D. 600,000 km/s"],
        "answer": "A"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
        "answer": "B"
    },
    {
        "question": "What is the boiling point of water?",
        "options": ["A. 100°C", "B. 50°C", "C. 0°C", "D. 25°C"],
        "answer": "A"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
        "answer": "C"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A. Diamond", "B. Ruby", "C. Sapphire", "D. Emerald"],
        "answer": "A"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    }
]

run_quiz(questions)

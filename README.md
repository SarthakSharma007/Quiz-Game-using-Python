Quiz Game 

Welcome to the Quiz Application! 🎉 This Python-based program is a fun and interactive way to test your general knowledge through multiple-choice questions. It provides an engaging experience where users can answer questions, get immediate feedback, and track their score in real-time.

Code Description 📄
This Python script is designed to run a command-line quiz game with multiple-choice questions. Here's a breakdown of how the code works:

Key Components:
Function: run_quiz(questions)

This is the core function of the quiz application.

It loops through each question in the questions list and displays them one by one to the user.

The user is prompted to enter an answer (A, B, C, or D).

If the user enters "EXIT", the quiz will terminate immediately, and their current score will be displayed.

After each question, the user's answer is compared with the correct answer. If the answer is correct, the score increases by 1.

After all questions have been answered or if the user exits, the final score is displayed.

Question Data Structure:

The questions are stored in a list of dictionaries.

Each dictionary represents a question and contains the following keys:

question: The question text.

options: A list of multiple-choice options (A, B, C, D).

answer: The correct answer corresponding to the options.

The questions can easily be modified or extended by adding more dictionaries to this list.

User Interaction:

The user interacts with the quiz by typing their answer or choosing to exit the quiz.

After each answer, feedback is given. If the answer is correct, the program prints "Correct!" Otherwise, it prints the correct answer.

The program continues until all questions are answered or the user decides to exit.

Score Tracking:

The score variable keeps track of the number of correct answers.

The total_questions variable tracks the total number of questions answered.

At the end of the quiz, the final score is displayed in the format: "You got X out of Y questions correct."

How the Code Works:
Initialization:

The quiz starts by calling the run_quiz() function with a predefined list of questions.

The function initializes score and total_questions to 0.

Main Loop:

The script iterates through the list of questions, displaying each question and its options.

The user is prompted for an answer, and their response is processed.

If the answer is correct, the score is incremented.

If the answer is wrong, the correct answer is displayed.

Exit Option:

At any time, the user can type "EXIT" to stop the quiz and view their score up to that point.

End of Quiz:

Once all the questions are answered (or the user exits), the final score is displayed.

Example Usage:
The program starts by displaying a question with four options (A, B, C, D). After the user enters their answer, the program checks it against the correct answer. If correct, the user is informed; if not, the correct answer is displayed. The quiz continues until all questions are answered or the user exits.

import random

print("Welcome to Quiz Game!")

quiz = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "Is Python a snake or a programming language?", "answer": "both"},
]

random.shuffle(quiz)

score = 0

for q in quiz:
    print("\nQuestion:")
    print(q["question"])
    user_answer = input("Your Answer: ").strip().lower()
    if user_answer == q['answer'].lower().strip():
        print("Correct answer champ!")
        score += 1
    elif q["question"] == "Is Python a snake or a programming language?":
        if user_answer == q['answer'].lower().strip():
            print(f"Hey! i wasn't expecting anyone to get this one")
            score += 1
        else:
            print(f"It's a trick question wise guy. it's {q['answer'].lower()}!")
    else:
        print(f"Not quite right. The correct answer was {q['answer'].lower()}. Let's get that genius brain working, go read a book and come back.")
print(f"\nQuiz complete! Your final score is {score}/{len(quiz)}.")       
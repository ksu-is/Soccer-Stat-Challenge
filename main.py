import json
import random

# Load questions
with open("questions.json", "r") as f:
    quiz = json.load(f)

# Pick 10 random questions (since the system uses up to 10)
quiz = random.sample(quiz, 10)

score = 0
streak = 0
bonus_active = False
bonus_stage = 0  # counts from question 4 onward

for i, q in enumerate(quiz, start=1):
    print(f"\nQuestion {i}: {q['question']}")
    user_answer = input("Your answer: ").lower().strip()

    correct = user_answer in q["answers"]

    # First 3 questions (normal scoring)
    if not bonus_active:
        if correct:
            print("Correct!")
            score += 1
            streak += 1

            # Activate bonus after 3 correct in a row
            if streak == 3:
                bonus_active = True
                print("Bonus round unlocked!")
        else:
            print("Incorrect!")
            print("Correct answer:", q["answers"][0])
            streak = 0

    # Bonus rounds
    else:
        bonus_stage += 1

        if correct:
            # If questions 4–7 are correct, they're worth 2 points
            if 1 <= bonus_stage <= 4:
                print("Correct! (+2 points)")
                score += 2

            # If questions 8–10 are correct, they're worth 3 points
            elif 5 <= bonus_stage <= 7:
                print("Correct! (+3 points)")
                score += 3

        else:
            print("Incorrect!")
            print("Correct answer:", q["answers"][0])

            # Lose bonus if any mistake
            print("Bonus round failed!")
            bonus_active = False

print("\nFinal score:", score)

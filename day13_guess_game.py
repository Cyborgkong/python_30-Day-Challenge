import json
import os
import random

SCORE_PATH = 'json Projects/guess_game_score.json'

def load_score():
    if not os.path.exists(SCORE_PATH):
        return None
    with open(SCORE_PATH, 'r') as file:
        return json.load(file).get("high_score")

def save_score(score):
    with open(SCORE_PATH, 'w') as file:
        json.dump({"high_score": score}, file, indent=4)
        
difficulties = {
    '1': {'label': 'Easy', 'range': 50},
    '2': {'label': 'Hard', 'range': 500}
}

def display_score():
    score = load_score()
    if score is None:
        print("No high score yet.")
    else:
        print(f"🏆 High score: {score} attempts")

def get_hint(diff):
    diff = abs(diff)
    if diff == 0:
        return "🎯 Correct!"
    elif diff <= 3:
        return "🔥 Very close!"
    elif diff <= 10:
        return "🙂 Close"
    elif diff <= 25:
        return "😐 A bit off"
    elif diff <= 50:
        return "😕 Far"
    else:
        return "❄️ Ice cold!"

def start_game():
    while True:
        print("\n🎮 Welcome to the Guessing Game!")
        
        difficulty = input(f"Select difficulty (Hard or Easy): ").strip().lower()
        
        if difficulty == 'easy':
            selected = difficulties['1']
        elif difficulty == 'hard':
            selected = difficulties['2']
        else:
            print("❌ Invalid option. Enter 'Easy' or 'Hard'.")
            continue
        max_range = selected['range']
        answer = random.randint(1, max_range)
        attempts = 0
        
        print(f"\nGuess a number between 1 and {max_range}")
        
        while True:
            try:
                guess = int(input("🔢 Your guess: "))
                attempts += 1
                diff = guess - answer 
                
                hint = get_hint(diff)
                print(hint)
                
                if guess == answer:
                    print(f"🎉 You guessed it in {attempts} attempts!")
                    high_score = load_score()
                    if high_score is None or attempts < high_score:
                        print("🏅 New high score!")
                        save_score(attempts)
                    break
            except ValueError:
                print("❌ Enter a valid number.")
                
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            break
        
if __name__ == "__main__":
    display_score()
    start_game()
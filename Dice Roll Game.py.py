import random
total_score = 0
roll_count = 0
max_rolls = 6


playing = True
while True:
    if roll_count >= max_rolls:
        print("\nYou reached the maximum number of rolls.")
        break
    choice = input("Roll the Dice (y/n): ").lower()
    if choice == 'y':
        Dice1 = random.randint(1,6)
        Dice2 = random.randint(1,6)yield
        roll_total = Dice1 + Dice2
        total_score += roll_total
        roll_count += 1
        print(f"({Dice1}, {Dice2}) → Roll Total: {roll_total} | Score: {total_score} | Rolls Left: {max_rolls - roll_count}")
    elif choice == 'n':
        print("thanks for playing")
        break
    else:
        print("invaid choice")
print(f"\nGame Over! Total Score: {total_score} after {roll_count} roll(s).")

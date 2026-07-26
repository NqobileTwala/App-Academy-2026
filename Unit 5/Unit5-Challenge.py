print("The High-Score Tracker Game.")
print("----------------------------")
print("")

while True:
    score = input("Please enter a game score next to the flashing cursor: ").lower().strip()

    if score == "stop":
        print("Game session ended!")
        break
    else:
        score = int(score)
        if score > 100:
            print("Wow! That's a new high score!")
        else:
            print("Good try, keep playing!")
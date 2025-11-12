with open("goals.txt", "w", encoding="utf-8") as f:
    f.write("1. To study in Germany\n") # write goals
    f.write("2. To become a specialist in Artificial Intelligence\n") # write goals
    f.write("3. To create projects that make a difference in the world\n") # write goals
    f.write("4. To live a successful and meaningful life\n") # write goals

with open("goals.txt", "r", encoding="utf-8") as f:
    goals = f.readlines()
    for m in goals:
        print(m.strip())

with open("goals.txt", "a", encoding="utf-8") as f:
    f.write("5. To launch my own startup\n") # like append


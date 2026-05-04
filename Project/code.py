file = open("marks2.txt", "r")
lines = file.readlines()
file.close()

first_line_parts = lines[0].strip().split(",")[3:]
subjects = [item.split(":")[0] for item in first_line_parts]

highest_marks = {subject: 0 for subject in subjects}
highest_students = {subject: [] for subject in subjects}
gold_medal_total = 0
gold_medal_student = []

for line in lines:
    parts = line.strip().split(",")
    name = parts[0]
    total = 0

    for item in parts[3:8]:
        subject, mark = item.split(":")
        mark = int(mark)
        total += mark

        if mark > highest_marks[subject]:
            highest_marks[subject] = mark
            highest_students[subject] = [name]

        elif mark == highest_marks[subject]:
            highest_students[subject].append(name)

    if total > gold_medal_total:
        gold_medal_total = total
        gold_medal_student = [name]

    elif total == gold_medal_total:
        gold_medal_student.append(name)

print("Highest Marks in Each Subject:")
for subject in subjects:
    print(f"{subject}: {', '.join(highest_students[subject])} ({highest_marks[subject]})")

print("\nGold Medalist (Highest Total Marks):")
print(f"{', '.join(gold_medal_student)} ({gold_medal_total})")
~                                                                                                                                                                                                                                              
~                                                                  

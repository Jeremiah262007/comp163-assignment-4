student_name = "Jeremiah"
current_gpa = 4.0
study_hours = 21
social_points = 50
stress_level = 67

print("---NCAT: LIFESTYlE---")
print(f"Welcome {student_name}!")
print(f"Your current stats are, GPA: {current_gpa}, Study Hours: {study_hours}, Social Points: {social_points}, Stress Level: {stress_level}")

print("---HOW HARD ARE YOU GONNA WORK---")
print("Choose your course load:") 
print("A) Light (12 credits)")  
print("B) Standard (15 credits)") 
print("C) Heavy (18 credits)") 
choice = input("Your choice: ") 
if choice == "A":
    if current_gpa >= 2.0:
        study_hours += 5
        stress_level += 10
    print("You choose choice A, enjoy your low stress life!")
elif choice == "B":
    if current_gpa >= 3.0:
        study_hours += 10
        stress_level += 20
    print("You choose choice B, you won't be put through the ringer but it won't be a cakewalk!")
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours += 15
        stress_level += 30
    print("You choose choice C, enjoy your days now because I'm praying for you!")
else:
    ("Print invalid input as choice A, B, C was not chosen")

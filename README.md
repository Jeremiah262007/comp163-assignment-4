# comp163-assignment-4
# NCAT: LIFESTYLE

## Game Overview
*NCAT: LIFESTYLE* is a text-based simulation game that puts you in the shoes of a North Carolina A&T student, managing academics, social life, and stress throughout the semester. Players make choices about course load, study focus, and participation in social events, and each decision affects GPA, study hours, social points, and stress level. The game ends with different outcomes depending on your accumulated stats, teaching players the consequences of balancing academics and social life.

---

## Branching Concepts Demonstrated

1. **Decision 1 – Course Load**  
   - Players choose a course load: Light (A), Standard (B), or Heavy (C).  
   - Demonstrates **if/elif/else** branching.  
   - Changes `study_hours` and `stress_level` based on `current_gpa`.  

2. **Decision 2 – Study Focus**  
   - Players select a subject: Programming, Math, English, or History.  
   - Uses **membership operators** (`in`, `not in`) and logical operators (`and`, `or`).  
   - Affects `current_gpa` and `social_points` differently based on subject.  

3. **Decision 3 – Last Day of School (LDOC)**  
   - Players decide whether to attend LDOC (`yes`/`no`).  
   - Demonstrates **nested if statements** and multiple endings.  
   - Outcomes depend on accumulated stats: `current_gpa`, `social_points`, and `stress_level`.

---

# Endings and Explanations

## Ending 1
**Criteria:** Attended LDOC (`yes`), `social_points >= 30`, `current_gpa >= 3.5`  
**Explanation:** You studied hard, kept strong social connections, and attended LDOC. You made the Dean's List and enjoyed social events.

## Ending 2
**Criteria:** Attended LDOC (`yes`), `social_points >= 30`, `current_gpa < 3.5`  
**Explanation:** You partied with friends but didn’t make the Dean's List due to a slightly lower GPA.

## Ending 3
**Criteria:** Attended LDOC (`yes`), `social_points < 30`  
**Explanation:** You attended LDOC but didn’t enjoy yourself because you neglected social connections during the semester.

## Ending 4
**Criteria:** Did not attend LDOC (`no`), `stress_level < 70`, `current_gpa >= 3.5`  
**Explanation:** You stayed inside and rested, successfully balancing your work and stress, earning the Dean's List.

## Ending 5
**Criteria:** Did not attend LDOC (`no`), `stress_level < 70`, `current_gpa < 3.5`  
**Explanation:** You stayed inside, missed out socially, and didn’t make the Dean's List.

## Ending 6
**Criteria:** Did not attend LDOC (`no`), `stress_level >= 70`  
**Explanation:** You were too stressed to attend LDOC and missed social opportunities.

## Invalid Input
**Criteria:** Any input other than lowercase `"yes"` or `"no"` for LDOC attendance.  
**Explanation:** The game prompts for a valid lowercase input.


---

## How to Run the Game

1. Ensure you have Python 3 installed.  
2. Open a terminal or command prompt.  
3. Navigate to the folder containing `jdcooper4_assignment_4.py`.  
4. Run the game:

```bash
python jdcooper4_assignment_4.py

GPT-5 Mini was used to assist with code logic, such as if type(final_choice) is not str, helping clarify the membership operator, debugging the commit process as it assisted me with understanding how to connect VS Code to git and ultimately get my commits to run, and assist with writing professional documentation for the game.

# Python Quiz Game
questions = ("How many elements are there in the periodic table?: ",
             "Which animal lays the largest egg?: ",
             "How many bones are there in the human body?: ",
             "Which planet in the solar system is the hottest?: ",
             "Which is the most abundant gas in Earth's atmosphere?: ")
options = ( ("A. 116","B. 119","C. 118","D. 169"),
            ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
            ("A. 206 ","B. 208","C. 221","D. 296"),
            ("A. Mars", "B. Venus", "C. Earth", "D. Mercury"),
            ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"))

answers = ("C", "D", "A", "B", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter your answer (A/B/C/D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is {answers[question_num]}.")
    question_num += 1

print("------- RESULTS -------")
print("Correct Answers: ", end = "")
for answer in answers:
    print(answer, end = " ")
print()

print("Your Answers: ", end = "")
for guess in guesses:
    print(guess, end = " ")
print()

score = int(score / len(questions)*100)
print(f"Your score is {score}%.")


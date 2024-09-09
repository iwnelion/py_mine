print("F1 Quiz!!")
score=0

questions=[
    {
        "question": "Question 1: Who is the current f1 world champion?",
        "options": ["(a) Lewis Hamilton", "(b) Max Verstappen", "(c) Sebastian Vettel", "(d) Charles Leclerc"],
        "correct": "b"
        # max
    },
    {
        "question": "Question 2: Red Bull is leading in the constructor standing for only 14 points",
        "options": ["(a) True", "(b) False"],
        "correct": "b"
        # it's 8pts
    },
    {
        "question": "Question 3: Who is the current team principal of Ferrari?",
        "options": ["(a) Mattia Binotto", "(b) Frederic Vasseur", "(c) Andrea Stella", "(d) Christian Horner"],
        "correct": "b"
        # Frederic Vasseur
    },
    {
        "question": "Question 4: How many world championships has Red Bull won?",
        "options": ["(a) 6", "(b) 3", "(c) 7", "(d) 1"],
        "correct": "a"
        # 6
    },
    {
        "question": "Question 5: Lewis Hamilton has more podiums than Max Verstappen.",
        "options": ["(a) True", "(b) False"],
        "correct": "a"
        # 201, Max has 108
    },
    {
        "question": "Question 6: Who came first (in McLaren)?",
        "options": ["(a) Oscar Piastri", "(b) Lando Norris", "(c) The Chicken", "(d) The Egg", "(e) don't look at me"],
        "correct": "b"
        # landooo
    },
    {
        "question": "Question 7: Which team has only 6 points (until now. probably until of the year as well)?",
        "options": ["(a) Alpine", "(b) Hass", "(c) Williams", "(d) Kick Sauber (the green ones)"],
        "correct": "c"
        # Williams
    },
    {
        "question": "Question 8: Who won in the Hungarian Grand Prix 2024?",
        "options": ["(a) Oscar Piastri", "(b) Lando Norris ofc", "(c) Lewis Hamilton", "(d) Max did not win, don't pick Max"],
        "correct": "a"
        # oscar
    },
    {
        "question": "Question 9: Who did the fastest lap in the Belgium gp?",
        "options": ["(a) Max Verstappen", "(b) Pierre Gasly", "(c) Oscar Piastri", "(d) Sergio Perez"],
        "correct": "d"
        # perez
    },
    {
        "question": "Question 10: Which is my not so favorite driver? (yeah, mine)",
        "options": ["(a) Lando Norris, obviously, i hate that guy", "(b) Carlo Sainz. he's so dumb", "(c) Lewis Hamilton, he's so arrogant", "(d) Fernando Alonso. why is he still driving?"],
        "correct": "c"
        #hamilton
    }
]

for i, question in enumerate(questions, start=1):
    print(f"\nQuestion {i}: {question['question']}")
    for option in question['options']:
        print(option)
    ans=input().lower()
    if ans==question["correct"]:
        score+=1

print("That's all! You scored: ", score, "points!")
if score==0:
    print("Zero points, wow! Bottas and Zhou would be proud of you!")
elif score<=4:
    print("Stroll wishes he could be like you!")
elif score<=7:
    print("You're just like Hamilton! when Mercedes dropped him! Wow!")
elif score==8:
    print("You could win in Monza, but you're like Sainz, so you couldn't really win in Monza.")
elif score==9:
    print("Simply lovely! not in a Max way, but in a Norris way. Good job!")
elif score==10:
    print("You're the best! You're like Norris when he will win 2024 world championship!! Great job!")

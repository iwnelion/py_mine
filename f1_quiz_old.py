print("F1 Quiz!!")
score=0

print("Question 1: Who is the current f1 world champion?")
print("(a) Lewis Hamilton")
print("(b) Max Verstappen")     #dududu
print("(c) Sebastian Vettel")
print("(d) Charles Leclerc")
ans=input().lower()
if ans=="b":
    score+=1

print("Question 2: Red Bull is leading in the constructor standing for only 14 points")
print("(a) True")
print("(b) False")  #it's 8 points
ans=input().lower()
if ans=="b":
    score+=1

print("Question 3: Who is the current team principal of Ferrari?")
print("(a) Mattia Binotto")
print("(b) Frederic Vasseur")  #he is
print("(c) Andrea Stella")
print("(d) Christian Horner")
ans=input().lower()
if ans=="b":
    score+=1

print("Question 4: How many world championships has Red Bull won?")
print("(a) 6")      #it's 6
print("(b) 3")
print("(c) 7")
print("(d) 1")
ans=input().lower()
if ans=="a":
    score+=1

print("Question 5: Lewis Hamilton has more podiums than Max Verstappen")
print("(a) True")       #201, Max has 108
print("(b) False")
ans=input().lower()
if ans=="a":
    score+=1

print("Question 6: Question 6 Who came first (in McLaren)?")
print("(a) Oscar Piastri")
print("(b) Lando Norris")   #landooo
print("(c) The Chicken")
print("(d) The Egg")
print("(e) don't look at me")
ans=input().lower()
if ans=="b":
    score+=1

print("Question 7: Which team has only 6 points (until now. probably until of the year as well)?")
print("(a) Alpine")
print("(b) Hass")
print("(c) Williams")       #it's them
print("(d) Kick Sauber (the green ones)")
ans=input().lower()
if ans=="c":
    score+=1

print("Question 8: Who won in the Hungarian Grand Prix 2024?")
print("(a) Oscar Piastri")          #him
print("(b) Lando Norris ofc")
print("(c) Lewis Hamilton")
print("(d) Max did not win, don't pick Max")
ans=input().lower()
if ans=="a":
    score+=1

print("Question 9: Who did the fastest lap in the Belgium gp?")
print("(a) Max Verstappen")
print("(b) Pierre Gasly")
print("(c) Oscar Piastri")
print("(d) Sergio Perez")       #him
ans=input().lower()
if ans=="d":
    score+=1

print("Question 10: Which is my not so favorite driver? (yeah, mine)")
print("(a) Lando Norris, obviously, i hate that guy")
print("(b) Carlo Sainz. he's so dumb")
print("(c) Lewis Hamilton, he's so arrogant")       #yeah
print("(d) Fernando Alonso. why is he still driving?")
ans=input().lower()
if ans=="c":
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

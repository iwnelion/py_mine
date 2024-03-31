name=input("what's your name? ")
age=int(input("what's your age? "))

#age is int so this can happen
age+=1

print("hello "+name)
print("you'll be "+str(age)+" years old")

print(f"hello {name}, you'll be {age} years old")

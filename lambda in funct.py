def myfunct(n):
    return lambda a:a*n

mydoubler=myfunct(2)
mytripler=myfunct(3)

print(mydoubler(11))
print(mytripler(11))
#22
#33

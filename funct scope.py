#function scope: a funct as a member of another funct
#small can access big's members
def bigFunct():
    x=2
    def smallFunct():
        print(x)
    smallFunct()
bigFunct()

import os
if os.path.exists("new.txt"):
    os.remove("new.txt")
else:
    print("The file does not exist")

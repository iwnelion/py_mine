#in file: myModule.py
def greeting(name):
    print("hello "+name)

#in file: main.py
import myModule
myModule.greeting("jo")

#runs: hello jo

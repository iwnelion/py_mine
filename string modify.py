a="Hello"
print(a.upper())
#HELLO

print(a.lower())
#hello

b="hello world"
print(b.strip())
#hello world

#removes whitespace before and after txt:
b=" hello world "
print(b.strip())
#hello world

a="hello"
print(a.replace("h","j"))
#jello

a="hello, world"
b=a.split(",")
print(b)
['hello', ' world']

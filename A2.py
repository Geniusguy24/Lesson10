str = input("Please Enter a string:")
print("Original String:", str)

revstr = ""

for i in str:
    revstr= i+revstr
print("Reversed string:", revstr)
Z = str(input("write your name...."))
A = str(input("write your father name...."))
E = int(input("write your age...."))
print("my name is",Z)
print("my father name is",A)
print("you are",E,"years old")
if E <= 10 :
    print("you are a child")

if E > 10 and  E <= 20 :
    print("you are a teen")

if E > 20 and E <= 30 :
    print("you are a adult")

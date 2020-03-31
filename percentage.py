print("marksheet of student")
print("..............................................")
maths=int(input("total marks of maths......."))
sci=int(input("total marks of sci.......")) 
eng=int(input("total marks of eng......."))
comp=int(input("total marks of comp........"))
total_marks=maths+sci+eng+comp
print(total_marks)
print("..................................................")
MATHS=int(input("obtain marks in maths......."))
SCI=int(input("obtain marks in sci......"))
ENG=int(input("obtain marks in eng......"))
COMP=int(input("obtain marks in comp......"))
obtain_marks=MATHS+SCI+ENG+COMP
print(obtain_marks)
print(".....................................................")
percentage=(obtain_marks/total_marks)*100
print(percentage)

# name=input("enter your first name:")
# print ("length of first name is :",len(name))

# str1 = ("Hi$, i am a $dollar symbol$ $ 0.99")
# print (str1.count ("$"))

# use of if/elif/else statements
 # WAP that takes input marks and assign grades of students
 
marks= int(input("enter marks of students:"))

if (marks>=80 and marks>90):
    grade="A"
elif (marks>=70 and marks<80):
    grade = "B"
elif (marks >=60 and marks<70):
    grade= "C"
else :
    grade= "F"

print("grade of a student -->",grade)
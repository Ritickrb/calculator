#1St QUESTION
Name = (input("Please Enter Your Name:-"))
print(Name)
print("Now You Have to Enter Your Marks:-")
English = (input("Enter Your Marks Of English:-"))
Hindi = (input("Enter Your Marks Of Hindi:-"))
Mathematics = (input("Enter Your Marks Of Mathematics:-"))
Science = (input("Enter Your Marks Of Science:-"))

allNumbers = {English, Hindi,Mathematics, Science}
print("All of Your Marks are: ",allNumbers)

if (English>Hindi) and (English>Mathematics) and (English>Science):
    print("Your Marks in English  is Highest:-", English)  
elif (Hindi>English) and (Hindi>Mathematics) and (Hindi>Science):
    print(" Your Marks in Hindi is Highest:-", Hindi)
elif (Mathematics>Hindi) and (Mathematics>English) and (Mathematics>Science):
    print(" Your Marks in Mathematics Highest:-", Mathematics)
else:
    print("Your Marks in Science is Highest:-", Science)
#CGPA
print("Write down marks for first semester:-")
eng1 = int(input("Your marks of subject English?"))
hin1 = int(input("Your marks of subject Hindi?"))
maths1 = int(input("Your marks of subject Mathematics?"))
Sci1 = int(input("Your marks of subject Science?"))
total_marks_obtained1 = eng1 + hin1 + maths1 + Sci1
print("your total marks of semester 1:",total_marks_obtained1)
percentage1 = (total_marks_obtained1) / 400*100
print("your percentage of semester 1:",percentage1 )

print("Write down marks for Second semester:")
eng2 = int(input("Your marks of subject English:"))
hin2 = int(input("Your marks of subject Hindi:"))
maths2 = int(input("Your marks of subject Mathematics:"))
Sci2 = int(input("Your marks of subject Science:"))
total_marks_obtained2 = eng2 + hin2 + maths2 + Sci2
print("your total marks of semester 2:",total_marks_obtained2)
percentage2 = (total_marks_obtained2) / 400*100
print("your percentage of semester 2:",percentage2 )

total_marks = total_marks_obtained1 + total_marks_obtained2
percentage = (percentage1 + percentage2) / 2
print("total percentage of your both semesters is-", percentage)

CGPA = percentage/9.5
print("YOUR CGPA OF YOUR BOTH SEMESTERS IS:-", CGPA)



#CALCULATOR
# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")


#else data
n=int(input("How many students in class:: "))
m=int(input("Enter how many subject in your class:: "))
dict={}
for i in range(1,n+1,1):
    p=input("Enter the name of student:: ")
    dict[p]={}
    for j in  range (1,m+1,1):
        k=input("Enter the subject name:: ")
        marks=int(input("Enter the marks in subject:: "))
        dict[p][k]=marks
print(dict)


d={}
for i in range(2):

    Name=input("Enter Student Name = ")
    Marks=[]
    for j in range(1):
        english=int(input("Enter the Marks of English = "))
        hindi=int(input("Enter the Marks of Hindi = "))
        Marks.append(english)
        Marks.append(hindi)
    d[Name]=[english,hindi]
print(d)
print(english)
print(hindi)
Name=input("Enter Student Name = ")
Total=english+hindi
Percentage=(Total)/200*100

if Name in d.keys():
    print('sum',Total)
    print('percentage',Percentage)
else:
    print('NO data')


# question 1
#pasword generator
#question 2
#dice different number between 1 to 6
# question 3
# otp generate
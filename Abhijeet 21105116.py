#Q1

#average of three no.s taken from user.


print("  1st program" , "\n")
#taking input from user
numb1=int(input("enter first number: "))
numb2=int(input("enter second number: "))
numb3=int(input("enter third number: "))
avg=(numb1+numb2+numb3)/3
print("avg of the given numbers is:", avg)


#Q2

# calculating tax in dollars


print(" 2nd program" , "\n")
print(" Kindly enter the values in dollars.")
#taking input from user
gross_income = float(input("enter your gross income "))
dependents = int(input("enter number of dependents"))


tax_rate = 0.2
standard_deduction = 10000
dependent_deduction = 3000

taxable_income = (gross_income - standard_deduction - (dependent_deduction*dependents))
tax = taxable_income*tax_rate
print("the tax comes out to be $" , tax , "\n")


#Q3

#storing data of students.


print(" 3rd program" , "\n")
print( "Student = [ SID , Name , Gender , Course , CGPA]" )
#taking input from user
SID = int(input("Kindly enter your SID "))
Name = input("Kindly enter your name " )
Gender = input("Kindly enter your gender 'M' , 'F' , 'U' for male , female , unknown respectively.")
Course = input("Kindly enter your course name" )
CGPA = float(input("Kindly enter your CGPA "))
student = [SID, Name, Gender, Course, CGPA]   #arranging the data in a list
print ("student's data : " , student , "\n")





#Q4

#storing marks of 5 students and display them in a sorted manner

print(" 4th program" , "\n")
#taking input from user
a= int(input("enter marks of student '1' "))
b= int(input("enter marks of student '2' "))
c= int(input("enter marks of student '3' "))
d= int(input("enter marks of student '4' "))
e= int(input("enter marks of student '5'"))

#converting the input data into list

marks = [a,b,c,d,e]
print("marks of 5 students are " , marks)

#sorting the list in ascending and descending order .
asc = marks.sort()
print("marks in ascending order " , marks)

desc = marks.sort(reverse = True)
print("marks in descending order " , marks , "\n")



#Q5

#removing the elements of a given list.

print("5th program" , "\n")
color = ['Red' , 'Green' , 'White' , 'Black' , 'Pink' , 'Yellow']
print("The given list is " , color , "\n")


#printing the modified list after removing 4th term
color.pop(3)
print("The modified list is color 1 =" , color)

#removing 'Black' and 'Pink' from the list and replacing them with 'Purple'
color2 = ['Red', 'Green' , 'White', 'Black' , 'Pink' , 'Yellow' ]
color2[3:5] = ['Purple']
print("The modified list if color 2=" , color2)

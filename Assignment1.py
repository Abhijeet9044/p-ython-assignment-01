#Q1
#Taking input from the user
input=input("Enter the number whose average is th be calculated:")

input=input.split()
sum=0
number_of_terms=0
for i in input:
    input[input.index(i)]= int(i)
    number_of_terms +=1
    sum +=int(i)
average= sum/number_of_terms

#Making the output presentabe
if average == int(average):
    average = int(average)
else:
    average = round(average, 2)
 
#printing the average
print("\nThe average of the given", number_of_terms, "number is", average,"\n")


#Q2
#Given constants
rate= 0.20
standard_deducation = 10000
dependent_deducation = 3000

#Taking input from the user
gross_income = float(input("\nEnter your gross income:"))
number_of_dependents = int(input("Enter number of dependents:"))

#calculation tax
taxable_income = round(gross_income-standard_deducation-(dependent_deducation*number_of_dependents),1)
tax = taxable_income*rate
if tax <0:
    tax=0

    #output
    print("Your tax is $", tax,"\n")

#Q3
    #Taking input from the user
SID= int(input("\nEnter the SID of the student\n"))
name=input("\nEnter the name of the student\n")
while True:
    gender=input("\nEnter the gender of the syudent\n(Enter F femakle, M FOR male and U for unknown)\n")
    gender=gender.upper()
    if gender in("M","F","U"):
        break
    else:
        print("\nPlease enter the gender in correct format")
        while True:
        course_name= input("\nEnter the course name of the student\n(out of EE, ECE, CSE, Aero, Prod, Civil)\n"
        course_name= course_name.upper()
        if course_name in ("EE", "ECE", "CSE", "AERO", "PROD", "CIVIL"):
            break
        else:
            print("\nPlease enter the course name is correct format")
            while True:
                cgpa=round(float(input("\nEnter the CGPA of the student\n")),1)
                if cpga>=0 and cpga<=10:
                    break
                else:
                    print("\nThe CGPA should be less than 10\n")

                    #creating the list
                    student= [SID, name, gender, course_name, cgpa]

                    #printing thr required list
                    print(student, "\n")


#Q4
         import pandas as pd
name=[]
marks=[]
count=1
#Taking the input from the user
number_of_students= int(input("\nYou want to fill data for how many students?"))
while count<= number_of_students:
    while count==1:
print("\nThe name and marks are to be inputted seperated by a\"-\".For example:\"Abhijeet -05\"\n")
        break
    que_to_be_asked="Enter name and marks of student"+str(count)+":"
    input_value=input(que_to_be_asked)
    input_valu= input_value.split("-",1)
    names.insert(count-1, input_value[0].strip())
    marks.insert(count-1, int(input_value[1]))
    count+=1
    #creation of series
data= pd.series(marks, index=names)

#sorting the data
while true:
    asc_or_dsc=int(input("\nEnter 1 for ascending, 2 for descending:"))
    if asc_or_dsc==1:
    data=data.sort_values()
    break
elif asc_or_dsc==2:
    data=data.sort_values(ascending=False)
    break
else:
    print("Please enter the correct input")
    #output
    print("\nThe marks of students in required format are as follows:\n")
    count=1
    while count<=number_of_students:
        print("Marks of",data.index[count-1],"are",data[count-1],"\n")
        count+=1      


#Q5a
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print("\n",color,"\n")


#Q5b
color=['Red','Green','White', 'Black', 'Pink', 'Yellow']
color[2:5]=[];color.insert(2, "Brown")
print("\n",color,"\n")
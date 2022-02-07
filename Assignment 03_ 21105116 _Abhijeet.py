#Question 1

print("Question 1")
#taking input from user
sentence = input("Please give an input- ")
sentence=sentence.lower().strip()
i=0
#defining empty dictionary to use later to store element, counter pairs and eliminating common letters and words
dict={}

#checking if the string input is a word or a sentence
if " " not in sentence:
     #searching for common elements
     while i<len(sentence):
          counter=0
          k=0
          while k<len(sentence):
               if sentence[i]==sentence[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1
          #storing the values in dictionary
          dict[f"{sentence[i]}"]=counter
          i=i+1

else:
     #making a list of words using split method
     list = str.split(sentence)
     #searching for common words
     while i<len(list):
          counter=0
          k=0
          while k<len(list):
               if list[i]==list[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1
                    #storing the pairs in dictionary
          dict[f"{list[i]}"]=counter
          i=i+1
#Printing the final result
print("Total occurances")
for key,value in dict.items():
    print(f"{key}-{value}")

##########################################################################################
#Q2
print("Question--2")
#Taking data from the user
year = int(input("Enter a year [1800-2025]: "))
#leap year conditions
if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False
#Taking data from the user
month = int(input("Enter a month [1-12]: "))
#For a month of 31 days
if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:   #considering a leap year
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30

#Taking data from user
day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
#printing the output
print("The next date is [dd-mm-yyyy] %d-%d-%d." % (day,month,year))

#######################################################################################
#Q3
print("Question--3")
#taking input from user
num1=int(input("Enter the number 1: "))
num2=int(input("Enter the number 2: "))
num3=int(input("Enter the number 3: "))
num4=int(input("Enter the number 4: "))
l1=[num1,num2,num3,num4]
#arranging list in sorted manner
l1.sort()
#printing list
print(l1)
#printing square of the numbers present in the list
my_result =[(val, pow(val, 2)) for val in l1]
print(my_result)

#########################################################################################
#Q4
print("Question--4")
#Taking input from user
marks=int(input("Enter your Grade Point: "))
#printing conditions
if marks==10:
    grade="A+\n"
    perf="Your Performance is OUTSTANDING"

elif marks==9:
    grade="A\n"
    perf="Your Performance is EXCELLENT"

elif marks==8:
    grade="B+\n"
    perf="Your Performance is VERYGOOD"

elif marks==7:
    grade="B\n"
    perf="Your Performance is GOOD"
    
elif marks==6:
    grade="C+\n"
    perf="Your Performance is AVERAGE"

elif marks==5:
    grade="C\n"
    perf="Your Performance is BELOW AVERAGE"

elif marks==4:
    grade="D\n"
    perf="Your Performance is POOR"
    
else:
    grade="Error message"
    perf="You are fail"
#printing the output
print("Your Grade is " + grade + perf)

#########################################################################################
#Q5
print("Question--5")
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

for row in range(0,6):
    column=0
    counter=0
    while column<11:
        if column<row or column>11-row-1:
            print(" ", end="")

        else:
            print(alphabets[counter], end="")
            counter=counter+1
        column=column+1
    print("")

###########################################################################################
#Q6
print("Question--6")
#Taking input from user
n=int(input("Enter the number of student's data to be stored : "))
myDict = {}
for i in range (n):
      key=input("Enter SID :")
      value=input("Enter Name :")
      myDict.update({key: value})
#Printing A
print(myDict)
#Printing B
print(sorted(myDict.values()))
#Printing C
print(sorted(myDict.keys()))
#Printing D
a=(input("Enter the SID of student\n",))
print("The student is" , myDict[a])

###########################################################################################
#Q7
print("Question--7")
# Program to display the Fibonacci sequence up to n-th term
from tkinter import N
nterms = int(input("Enter the number of Fibonacci sequence that you want: "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
a= (nterms)/2
print("the avg of series is ", a)

##################################################################################################
#Q8 
print("Question--8")
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

#a
print("Elements that are in Set1 and Set2 but not both:",(set1 | set2)- (set1 & set2))
print(set1 & set2 & set3)

#b
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

print("Elements that are in only one of the three sets:",sorted(set1 ^ set2 ^ set3))

#c
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

set4=set1 & set2
set5=set2 & set3
set6=set1 & set3

print("Elements that are exactly two of the sets:",set4 | set5 | set6)

#d
set1=set()
for i in range(1,10):
       set1.add(i)
set2={1,2,3,4,5}
set3=set1-set2
#printying set in sorted manner
print("Set of all integers in the range 1 to 10 that are not in set1:",sorted(set3))

#e
set1=set()
for i in range(1,11):
       set1.add(i)
set2={1,2,3,4,5}
set3={2,4,6,8}
set4={1,5,9,13,17}
set5=set2 | set3 | set4

set6=set1-set5
print("set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3: ",set6)
                        

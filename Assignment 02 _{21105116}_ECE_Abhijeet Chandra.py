#Q1

print('Question 1 : \n')
#filling the input string
given_string = 'Python is a case sensitive language'
#a.Finding the length of the input string 
print('part a :')
print(f"Length of the Given string = {len(given_string)} \n")
#b. Revercing the order of the string in one line code
print('part b :')
print(given_string[::-1])
#c. slicing the given_string and storing/printing it in a new string.
print('\npart c :')
sliced_string = given_string[10:26]
print(sliced_string)
#d. replacing a part and printing the new string.
print('\npart d :')
new_string = given_string.replace('a case sensitive' , 'object oriented')
print(new_string)
#e. finding the index of a substring in the given_string.
print('\npart e:')
print(given_string.index('a'))
#f. replacing blank white spaces with empty string.
print('\npart f:')
print(given_string.replace(' ',''))


#Q2

print('\nQuestion 2: \n')

#filling the required input.
name = 'Abhijeet Chandra'
SID = '21105116'
department = 'ECE'
CGPA = '10'

#printing the statements in the required format.
print(f'Hey, {name.title()} Here! \nMy SID is {SID} \nI am from {department} and my CGPA is {CGPA}')

#Q3

print('\nQuestion 3: \n')
#filling the given input
a=56
b=10
#solving the different parts
print('part a:\n a&b : ', a & b)
print('part b:\n a|b : ', a | b)
print('part c:\n a^b : ', a ^ b)
#left shift both a and b with 2 bits.
print("part d:\n a<<2 : ", a<<2, "\tb<<2 :", b<<2)
#right shift a with 2 bits and b with 4 bits.
print("part e:\n a>>2 :", a>>2, "\tb>>2 :", b>>4)

#Q4

print('\nQuestion 4: \n')
#taking input of 3 numbers from the user.
a= int(input("Enter 1st no. : "))
b= int(input("Enter 2nd no. : "))
c= int(input("Enter 3rd no. : "))
#finding the highest no.
if a>b :
    if a>c:
        highest_number = a
    else :
            highest_number = c
if b>a:
    if b>c:
        highest_number = b
    else :
            highest_number = c
print(f"Highest number = {highest_number}")
            


 #Q5

print('\nQuestio 5: \n')
 #taking input string from the user
input_string = input('Enter input string: ')
if "name" in input_string:
     print('Yes')
else :
     print('No')

#Q6

     print("\nQuestion 6: \n")
#taking input of 3 lengths fromt the user.
     a= int(input('Enter the 1st length :'))
     b= int(input('Enter the 2nd length :'))
     c= int(input('Enter the 3rd length :'))
#checking condition for triangle.
     if a+b>c and a+c>b and b+c>a:
         print('Yes')
     else:
         print('No')

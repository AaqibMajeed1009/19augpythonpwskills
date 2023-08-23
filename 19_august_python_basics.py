#!/usr/bin/env python
# coding: utf-8

# SECTION A QUESTIONS
# 

# In[11]:


"Basic variable based question 1"
a = 50
b = 40
print("Before Swapping: a=",a," and b=",b)
"Swap a and b"
a,b = b,a
print("Before Swapping: a=",a," and b=",b)


# In[12]:


"Basic variable based question 2"
#take inputs from the user
length = float(input("Length of Rectangle: ")) 
width = float(input("width of Rectangle: "))
area = length * width
print("The area of Rectangle is:",area)


# In[13]:


"Basic variable based question 3"
#take input from the user
celsius = int(input("Temperature in Celsius: "))
fahrenheit = celsius * (9/5) + 32
print("The provided celsius temperature in fahrenheit is:",fahrenheit)


# SECTION B QUESTIONS

# In[14]:


"String based question 1"
#take inputs from the user
string1 = input("Enter the string: ")
print("The length of the provided string is",len(string1))


# In[33]:


"String based question 2"

# take input from the user
input_string = input("Enter a string: ")

# make it suitable for caseless comparisions
input_string = input_string.casefold()
#print(input_string)

# count the vowels
count = {x:sum([1 for char in input_string if char == x]) for x in 'aeiou'}

print("The number of vowels in the string:-",count)







# In[6]:


"String Based Question 3"
#print the reversal string
#take input from user
s = input("Enter the string that you want to reverse:-")
#s1="my name is aaqib majeed bhat from chadoora kashmir"
s2=s[::-1] # we are saving the reversal of string in s3 variable
print("Reverse of the input string:-",s2) #print the reversal of alphabets


# In[5]:


"String Based Question 4"
#Input is palindrome
def is_palindrome(s): # function to check palindrome
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

def check_palindrome(s): 
    if is_palindrome(s): #condition to check the palindrome
        return "The input is a palindrome."
    else:
        return "The input is not a palindrome."
#take input from user
s = input("Enter the string: ")
result = check_palindrome(s)
print(result)


# In[4]:


"String Based Question 4"
#Input is not palindrome
def is_palindrome(s): # function to check palindrome
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

def check_palindrome(s): 
    if is_palindrome(s): #condition to check the palindrome
        return "The input is a palindrome."
    else:
        return "The input is not a palindrome."
#take input from user
s = input("Enter the string: ")
result = check_palindrome(s)
print(result)


# In[28]:


"String Based Question 5"
#Print the modified string without spaces.
s = input("Enter a string: ")
s1 = s.replace(" ", "") #replaces the spaces with no spaces
print("Modified string without spaces:", s1)


# In[ ]:





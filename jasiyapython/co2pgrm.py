'''def factorial(n):
 if n == 0:
    return 1
 else:
     return n * factorial(n - 1)
num = int(input("Enter a number:"))
if num < 0:
    print("Factorial is not defined for negative numbers")
elif num == 0:
    print(f"{num}!=1")
else:
    fact=factorial(num)
    print(f"{num}!= {fact}")'''

'''def fib(n):
    f1=0
    f2=1
    print(f1)
    print(f2)
    for i in range(3,n+1):
        f3=f1+f2
        print(f3)
        f1=f2
        f2=f3
num=int(input("Enter the limit:"))
fib(num)'''

'''def sumList(list1):
    total=0
    for i in list1:
        total += i
    return total
list1=[1,2,3,4,5]
result=sumList(list1)
print("Sum of the list:",result)'''

'''def Even_PerfectSq(start,end):
    evenSq = []
    for num in range(start,end+1):
        if all(int(digit) % 2 == 0
               for digit in str(num)):
            sqrt=int(num ** 0.5)
            if sqrt * sqrt ==num:
                evenSq.append(num)
                return evenSq

start=1000
end=9999
result=Even_PerfectSq(start,end)
print(result)'''


'''n=5;
for i in range(n):
    for j in range(i):
        print('x',end="")
        print("")
for i in range(n,0,-1):
    for j in range(i):
        print('x',end="")
        print("")'''




'''def disp_pyramid(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i*j,end=" ")
        print()
n=int(input("Enter the number of steps:"))
if n<1:
    print("please enter a positive integer")
else:
    disp_pyramid(n)'''

'''def countChar(inputString):
    Count = {}
    for char in inputString:
        if char in Count:
            Count[char] += 1
        else:
            Count[char] = 1
        return Count
str2 = input("Enter a string:")
result = countChar(str2)
print(result)'''

'''def modifyStr(str1):
 if str1.endswith("ing"):
     return str1+"ly"
 else:
     return str1+"ing"
str1=input("Enter a string:")
result=modifyStr(str1)
print(result)'''

'''def longestWord(word):
    max_length=len(word[0])
  for item in word:
      length = len(item)
     if length > max_length:
         max_length = length
return max_length
words=input("Enter a list of words separated by spaces:")
word=words.split()
result=longestWord(word)
print(f"The length of the longest word is:{result}")'''


'''def pattern(n):
 for i in range(n):
     for j in range(i):
         print('*',end=" ")
     print(' ')
for i in range(n,0,-1):
    for j in range(i):
     print('*',end=" ")
    print(' ')
n = int(input(int("Enter the number of rows:"))
pattern(n)'''


'''def find_factors(number):
    factors=[]
    for i in range(1,number+1):
        if number %i==0:
            factors.append(i)
    return factors
num=int(input("Enter the number of rows:"))
result=find_factors(num)
print(f"The factors of {num} are:{result}")'''



     
            
            

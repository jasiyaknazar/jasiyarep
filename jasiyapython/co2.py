'''num=int(input("Enter a number:"))
factorial=1
if n >= 1:
    for i in range(1,n+1):
        factorial=factorial *1
print("factorial of the  number is",factorial)'''

num=10
n1=0
n2=1
print("fibonacci series:",n1,n2,end=" ")
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
    print()

'''list1=[11,5,17,18,23]
total=sum(list1)
print("sum of all elements in given list:",total)'''
    
'''num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1 < num2:
    min=num1
else:
    min=num2
gcd=1
for i in range(1,min+1):
    if num1 % i==0  and num2 % i ==0:
        gcd=i
print(f"The GCD of {num1} and {num2} is {gcd}")'''

'''list1=[1,2,3,4,5,6,7,8,9,10]
print(f"Original List:{list1}")
list2=[x for x in list1 if x % 2 != 0]
print(f"List of odd numbers:{list2}")'''

'''string="hello"
print("string",string)
character_count=len(string)
print("number of characters:",character_count)'''
































         

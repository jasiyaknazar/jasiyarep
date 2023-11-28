'''s=input("Enter a sentence:");
print(s)
wordsList=s.split()
print(wordsList)
for i in wordsList:
    print(f"{i}occurs{wordsList.count(i)}times")'''

'''n=int(input("Total number of integers:"))
list1=[]
for i in range (n):
    a=int(input("Enter an integer:"))
    if a<100:
        list1.append(a)
    else:
        list1.append("over")
print(list1)'''

'''name=['kichu','sanam','minnu','saira']
for i in name:
    print("'a' occurs in",i,"-",i.count('a'),"times")'''

'''list1=[8,6,7,4,5]
list2=[5,4,3,2,1]
#a.Check if the lists have the  same length
if len(list1)==len(list2):
    print("a.the lists have the  same length.")
else:
    print("a.the lists have the  different length.")
#b.Check if the lists have the  same sum
print(f"b.sum of list1:{sum(list1)}&sum of list2:{sum(list2)}")
if sum(list1)==sum(list2):
    print("The lists sum to the same value.")
else:
    print("The lists do not sum to the same value.")
#c.Check if there are any common values in both lists
common_values=set(list1)&set(list2)
if common_values:
    print(f"c.Common values in both lists:{common_values}")
else:
    print(f"c.There are no common values in both lists.")'''

'''s=input("Enter a word:")
c=s[0]
str1=s.replace(s[0],'$') #
c+str1[1:]'''

'''str1=input("Enter a string:")
print(str1[-1]+str1[1:-1]+str1[0])'''

'''r=int("input("Enter the radius:"))
area=3.14*r**2
print("Area of circle=",area)'''

'''n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
n3=int(input("Enter number 3:"))
if n1>n2 and n1>n3:
    print(f"largest no:is {n1}")
elif n2>n1 and n2>n3:
    print(f"largest no:is {n2}")
else:
    print(f"largest no:is {n3}")'''


'''filename=input("enter the filename:")
extension=filename.split(".")
print("The extension of the file is:",extension[-1])'''

'''color=[]
n=int(input("Enter total number of colors:"))
for i in range(n):
    ch=input()
    color.append(ch)
    print(f"First color is: {color[0]} \nLast color is:{color[-1]}")'''

'''n=int(input("Enter an integer n:"))
nn=n*11
nnn=n*111
s=n+nn+nnn
print(f"{n}+{nn}+{nnn}={s}")'''

'''list1=set(['Blue','Black','Green','Red','Orange'])
list2=set(['Red','Brown','Orange','Pink'])
list1.difference(list2)'''

'''s1=input("Enter first string:")
s2=input("Enter second string:")
print(s2[0]+s1[1:],"",s1[0]+s2[1:])'''

'''#Sample dictionar
my_dict={'banana':3, 'apple':1, 'cherry':2,'date':4}
print("Original list:",my_dict)
#Sort in ascending order based on keys
asorted_dict=dict(sorted(my_dict.items()))
print("Ascending order:",asorted_dict)
#sort in descending order based on keys
dsorted_dict=dict(sorted(my_dict.items(),reverse=True))
print("Descending order:",dsorted_dict)'''

dict1={"name":"Alice","age":25}
dict2={"name":"Ammu","occupation":"Software engineer","hobbies":["reading","writing"]}\#Merge dict2 into dict1
       dict1.update(dict2)
       print(dict1)

                         
    











            

capital=["A","B","C","D","E"]
small=["a","b","c","d","e"]
capital.extend(small)
print(capital)#
capital.append("F")
capital.sort(reverse=True)
print(capital)#
print(capital.count("a"))#
print(capital.index("c"))#
print(small.pop(-1))
print(small)#
small.insert(2,"e")
print(small)


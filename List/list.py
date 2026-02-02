l1 = []
l2 = [10, 20, "Bulbul", 30.5]
l3 = [300, 200, 800, 100]
l4 = ["Apple", "Banana", "Mango", "Orange"]
l5 = [4.5, 8.9, 6.9, 7.8]

print(type(l1))
print(6.9 in l5)
l1.append(50)
print(l1)
l2.extend(l5)
print(l2)
l4.reverse()
print(l4)
l3.sort()
print(l3)
print(l2.index("Bulbul"))
print(l5.count(7.8))
print(len(l4))
print(sum(l3))
print(min(l3))   
print(max(l5))
print(l3.pop())
print(sorted(l4))
print(len(l1))

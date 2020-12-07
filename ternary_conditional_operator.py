'''
base = 30
if base > 25:
    name = "admin"
else:
    name = "visitor"
print(name)

base = 20
name = "admin" if base > 25 else "visitor"
print(name)
''' 
"""
 x, y = 5, 6
print("x" if x > y else "y")
"""
def find_max(a,b):
  return a if (a>b) else b 
find_max(5, 6)
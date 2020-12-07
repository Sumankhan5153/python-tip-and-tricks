age = 20
print('age' in locals(), 'age' in globals())
del age
print('age' in locals(), 'age' in globals())

age = None
print('age' in locals(), 'age' in globals())
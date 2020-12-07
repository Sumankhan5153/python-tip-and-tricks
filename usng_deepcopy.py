from copy import deepcopy

tech = ['c', 'c++', 'python', ['html', 'css', 'pics']]
learning = tech.copy()
print(id(tech) == id(learning))
print(id(tech[-1]) == id(learning[-1]))

learning = deepcopy(tech)
print(id(tech) == id(learning))
print(id(tech[-1]) == id(learning[-1]))
def replace_list(data):
    data = ['new']

def replace_list_content(data):
    data[:] = ['new']

language = ['c++', 'go', 'python']

print(language)
replace_list(language)
print(language)
replace_list_content(language)
print(language)
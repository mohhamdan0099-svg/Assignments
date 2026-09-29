x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)

students[0]['last_name']='Bryant'
print(students)


sports_directory[ 'soccer'][0]='andres'
print(sports_directory)

z[0]['y']=30
print(z)



def iterateDictionary(some_list):
    for item in some_list:
        output = []
        for key, value in item.items():
            output.append(f"{key} - {value}")
        print(", ".join(output))


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(students)





def iterateDictionary2(key_name, some_list):
    for item in some_list:
        if key_name in item:
            print(item[key_name])

# Test Example:
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)






def printInfo(some_dict):
    for key, val_list in some_dict.items():
        print(f"{len(val_list)} {key.upper()}")
        for val in val_list:
            print(val)
        print()  

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
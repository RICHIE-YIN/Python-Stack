x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print (x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]["last_name"] = "Bryant"
print (students[0])

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = "Andres"
print(sports_directory['soccer'][0])

z = [ {'x': 10, 'y': 20} ]
z[0]["y"] = 30
print(z[0]["y"])


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary (students):
    for i in range(len(students)):
        print("first_name - "+students[i]['first_name']+", last_name - "+students[i]['last_name'])
iterateDictionary(students)

def iterateDictionary2 (key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key)
        for i in range(len(some_dict[key])):
            print(some_dict[key][i])

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #boolean
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary
fruit = ('blueberry', 'strawberry', 'banana')  #tuples
print(type(fruit)) #initialize
print(pizza_toppings[1]) #initialize
pizza_toppings.append('Mushrooms') #add value
print(person['name']) #initialize
person['name'] = 'George' #add value
person['eye_color'] = 'blue' #add value
print(fruit[2]) #initialize

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
    """
    16-26 conditional
    """

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1
"""
31-40 for loop and while loop
"""

pizza_toppings.pop() #list delete value
pizza_toppings.pop(1) #list delete value

print(person) #initialize
person.pop('eye_color') #dictionary delete value
print(person) #initialize

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
    """
    52-57 for and conditional statements
    """

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)
"""
62-79 functions
"""


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
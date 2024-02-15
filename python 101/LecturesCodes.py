#to print u can use '' or ""
print('Welcome back')

#---------------------------------------

#Variables : there is 2 ways to define a variable

#one
name1 = 'sarah'
age1 = 23

#two
name2 , age2 = 'sarah' , 24

#---------------------------------------

#inputs and outputs

#inputs : u can add a mesage to describe what the user should enter or leave it empty "input()"
user_name = input('Enter your user name please : ')

#outputs
print('yaaayy',user_name)

#---------------------------------------

#Operators :

addition = 4 + 5

subtraction = 9 - 10

multiplication = 3 * 3

division = 81 / 9

modulus = 10 % 3

#if we already have a number that is stored in an variable and we want to use some mathmical oprations on it
stored_num = 19
stored_num = stored_num - 10

print(stored_num)

#or we can do this short cut
stored_num_short = 19
stored_num_short -= 10

print(stored_num_short)

#---------------------------------------

#comprations : if equal then it will print true if not it will print false

compration_of_2_values = 9 == 0

opposite_comptation = 0 != 9

greater_than = 9 > 0

smaller_than_or_equal = 9 <= 0

#---------------------------------------

#logical operators :

#AND : both values should be true for the and to be true
not_raining = True
not_foggy = True
is_sunny = not_raining and not_foggy

#OR : only one of the values should be true or both values are true to get a true result at the end
is_raining = True
is_foggy = False
not_sunny = is_raining or is_foggy

#NOT: used to get the opposite of the result u already have
is_student = True
print(not is_student)

#an example of all the logical operators :
first, second = True, False
and_result = first and second  # False
or_result = first or second  # True
not_result = not first  # False
print(and_result)
print(or_result)
print(not_result)

#---------------------------------------

#data types :

#string
name = 'sarah'

#integer
age = 45

#float
weight = 46.5

#comlex number
comlex_number = 10j

#boolean
is_married = False

#none
driving_livense = None

#to print the data tybe of a variable
print(type(comlex_number))

#change a number type intger to a float number it will assign the new float number to a new variable
int_to_float = float(age)
print(type(int_to_float))
print(int_to_float)

#to change a float value to intger
float_to_int = int(weight)
print(type(float_to_int))
print(float_to_int)

#change a value to string
type_to_string = str(weight)
print(type(type_to_string))
print(type_to_string)

#---------------------------------------

#Sequence is when u store more than one value in one variable
#sequence types :

#1 lists
# u can use more than 1 data type in one list and lists is considered as a data type
color = 'blue'
colors = ['red' , 1 , 'white']
print(colors)

#u can access a list content using index starting with index 0
print(colors[2])

#change an index content
colors[0]="black"
print(colors)

#add more content to the end of the list
colors.append('gray')
print(colors)

#u can add the new content in an index of your choice
colors.insert(0,'pink')
print(colors)

#to delet an index
colors.remove('gray')
print(colors)

#delet evry elment in the list
colors.clear()
print(colors)

#tubles :

#store data but u can not change or remove anything u can use () as phonenum = (0 , 9 , 6) or without () as phonenum = 0 , 9 , 6 its the same
phonenum = (0 , 9 , 6)
print(type(phonenum))

#to read tuble index content
print(phonenum[1])

#dictionary
#we use dictionary when we have too much data to store so we can access the data needed easily u cant add more than 1 value to each key
game_one = {'name':'omori' , 'price':'gifted' , 'playtime':2 }
print(type(game_one))

#to access a dictionary index we use keys
print(game_one['name'])

#to print all dictiionay values
print(game_one.values())

#to print all keys of dictiionay
print(game_one.keys())

#---------------------------------------

#if else
#one condtion and u can just delete else so u would just have the conition result
age = 5
if age >= 18:
    print("you are an old enough")

else:
    print("you are just a kid go away")

#elif
#u can add more than one condtion
path = 'ios'

if path == 'web development':
    print('javascript')

elif path == 'ios':
    print('swift')

elif path == 'android':
    print('kotlin')

else:
    print('we dont have this language yet sorry')

# ---------------------------------------

#loops
# print i value if smaller or equal to 5 and add 1 to i in each loop
i = 1
while i <= 5:
    print(i)
    i += 1

#for loop
# c stands for each element of the list
colors = ['red' , 1 , 'white']
for c in colors:
    print(c)

#for loop ranges
#print 0 to 2
for n in range(3):
    print(n)

# print 5 to 8
for n in range(5, 9):
    print(n)

# ---------------------------------------

#function
def movie_night():
    movie_name = input('what is the movie name: ')
    movie_time = input('what time should we watch the movie ? ')
    print('i like ' + movie_name + ' ok lets watch it at ' + movie_time + ' (: ')

#call the function to work u can call the function multible times and any where at any time
movie_night()

#function with parameters
def print_num(num):
    for i in range(num):
        print(i)

#call the function with parameters
print_num(1)
print_num(2)

#function with 2 parameters
def print_num_2(num1,num2):
    print(num1+num2)

#call the function with parameters
print_num_2(1,9)
print_num_2( 'hello ',' good morning ')

#function with 2 parameters and return the return will send the result of the function to the call and store it in the variable of the call which in this case value
def add_num(num1,num2):
    result = num1+num2
    return result

#call the function with parameters
# the result of the return is 9 - 6
value = add_num(2,7) - add_num(2,4)
print(value)

#we can use return like this too it shorter
def minus_num(fnum,snum):
    return fnum - snum

#the result of the minus finction is now use as a parameter in onther function
value_min = minus_num(7,5)
print_num(value_min)

#or in a shorter form
print_num(minus_num(7,5))
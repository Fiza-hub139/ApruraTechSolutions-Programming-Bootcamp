# Lists
list= [1,2,3,4,5,1,2]
print(type(list))
list[4]= "4one"
print(list)

# Tuple
tup = ('T1' , 2 , 30.3 , "Str" , True)
print(type(tup))

# sets
set= { 12 ,34,90 ,23, 30.45 }
set1=()
print(type(set1))

# Dictionary 
dic={"Student_name":"Ayesha" , "Class": 10 , "hobbies": {'Coding','Training'}}
type(dic)
print(dic['Student_name'])
print(dic['hobbies'])


# Simple function example
def sum(a,b):
  # print(a+b)
  return a+b
sum(12,34)

# Function I/O operations 
def std(id, name):
  print("Student id is: ", id)
  print("Student name is: " , name)

std_id=input("Enter your id:")
std_name=input("Your name is: ")

std(std_id , std_name)
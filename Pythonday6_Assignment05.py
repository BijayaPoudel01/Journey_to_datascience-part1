# 1.Create a dictionary with the following details:
#     python
#     student = {"name": "Alice", "age": 20, "grade": "A"}
#     - Access the value of "age".
python_student = {"name": "Alice", "age": 20, "grade": "A"}
print(python_student['age'])

#     - Change the value of "grade"  to "A+".
python_student["grade"]="A+"
print(python_student)
#     - Add  a  new  key "city" with the value "New York".
python_student["city"]="New York"
print(python_student)
#     - Remove the "age" key from the dictionary.
del python_student['age']
print(python_student)

# 2.Merging two dictionaries **
# Given:python
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# - Merge dict2 into dict1 withoutusing a loop.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)

# 3.Accessing nested dictionary values **
# Given:python
# data = {"person": {"name": "John", "info": {"age": 25, "city": "London"}}}
# - Retrieve "London" from the dictionary.
data={
    "person":{
        "name":"jhon"
    },
    "info":{
        "age":25,
        "city":"london"
    }
}
print(data)
print(data['info']['city'])
# - Retrieve "25"from the dictionary.
print(data['info']['age'])

# 4.Updating multiple values at once **
# Given:python
# student_info = {"name": "Emily", "age": 21, "city": "Paris"}
# - Update`"age"`to `22` and `"city"`to`"Berlin"` in a single line.
student_info={"name":"Emily", "age":21, "city": "paris"}
updated_std_info ={"age":22,"city":"paris"}
student_info.update(updated_std_info)
print(student_info)

# 5.Create a dictionary from variables **
# Given:python
# name = "Sophia"
# age = 28
# country = "USA"
# - Create a dictionary where keys are variable names and values
# are the values of those variables.
name="sophia"
age=28
country="usa"
a={
    'name':name,
    'age':age,
    'country':country
}
print(a)

# 6)Given the dictionary person = {'name': 'John', 'age': 28, 'city': 'Chicago'},
# add a new key-value pair 'job':'Teacher' to the dictionary.
# Then update the value of the 'age' key to 29.
person = {'name': 'John', 'age': 28, 'city': 'Chicago'}
person["job"]="teacher"
print(person)

person["age"]=29
print(person)

# 7)Given the dictionary :
# person = {'name': 'Sarah', 'age': 35, 'city': 'Miami', 'job': 'Lawyer'},
# remove the key-value pair with the key 'city
person = {'name': 'Sarah', 'age': 35, 'city': 'Miami', 'job': 'Lawyer'}
del person['city']
print(person)

# 8).Create a dictionary named employee with keys
#     "name", "id", and "salary" and assign values to them.
employee={
    "name":"ram",
    "id":1,
    "salary": 30000
}
print(employee)

# 10).Given the dictionary:
# product = {"name": "Laptop", "price": 800, "brand": "Dell"}
# -Print the "brand" of the product.
product = {"name": "Laptop", "price": 800, "brand": "Dell"}
print(product["brand"])
# -Change the "price" of product to 900.
product["price"]=900
print(product)
# -Add a new key-value pair
product["stock"]=200
print(product)
# Add "stock": 50 to the product dictionary.
product["stock"]=50
print(product)
# -Remove a key-value pair-Remove "brand" from the product dictionary.
product.pop("brand")
print(product)
# Get the length of a dictionary
print(len(product))

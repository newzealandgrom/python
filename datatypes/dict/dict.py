dog = {
    'name': 'Samanta',
    'breed': 'Doberman',
    'color': 'Black',
}
print(dog)

# add value to dict
dog['age'] = 5
print(dog)
# update
dog['age'] = 1
print(dog)

# pop method
age = dog.pop('age')
print(age)
print(dog)

# get method
age = dog.get('age')
print(f'age is {age}')


# clear method
dog.clear()
print(dog)
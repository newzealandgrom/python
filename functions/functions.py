def say_hello(name, age, location='Novosibirsk'):
    print(f'Hello {name}, you are {age} today and you are from {location}')
    
    """print hello
    """

say_hello('Vladimir', 32, 'Russia')
say_hello('Mister', 23, 'USA')
say_hello(location='Canada', age=22, name='Google')
say_hello(age=22, name='Googles')
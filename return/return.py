def create_greeting(name, age, location):
    """create and return"""
    msg = f'Hello dear {name}. In two month you are going to be {age} and you are still live not in {location}'
    
    return msg

greeting = create_greeting('Vladimir', 33, 'New Zealand')

print(f'greeting:{greeting}')
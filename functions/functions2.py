def welcome(name, returning_user=True):
    """welcome"""
    if returning_user:
        message = f'Welcome back {name}'
    else:
        message = f'Welcome {name}'
    print(message)
    

welcome('Vladimir')
welcome('Vlad', False)
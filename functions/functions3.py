def userprofile(first_name,
                last_name,
                age,
                location,
                returning_user=True):
    """ user hello"""
    if returning_user:
        msg = f' Wellcome back {first_name} {last_name}'
    else:
        msg = f'Welcome {first_name} {last_name}'
    message = f'{msg} You are {age} and from {location}'
    print(message) 
    
    
userprofile('Vladimir', 'Mikhailov', 32, 'Novosiborsk')




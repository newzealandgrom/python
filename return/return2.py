def is_old_enough(age,  location):
    """is old enough"""
    if age >= 18 and location == 'Russia':
        return True
    
    if age >= 16 and location == 'US':
        return True
    
    return False

def status(age, location, test):
    """status"""
    old_enough = is_old_enough(age, location)
    if old_enough is False:
        print('You are not old enough')
        return
    
    if test is False:
        print('You need to learn to drive')
    else:
        print('You can drive')

status(12, "Russia", True)
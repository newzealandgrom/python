def hello(name):
    """Hello name"""
    msg = f'Hello {name}'
    
    def full_hello():
        """full hello"""
    print(msg)
    
    full_hello()

hello('Vladimir')
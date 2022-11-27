class User:
    """User"""
    def __init__(self, name, password):
        """initialize data or user"""
        self._name = name
        self._password = password
        self._logged_in = False
        
    def login(self, password):
        """check password and log user in"""
        if password == self._password:
            self._logged_in = True
        else:
            print('Incorect password.')
    
    def show_status(self):
        """print the status of user"""
        if self._logged_in:
            print(f'{self._name} is logged in.')
        else:
            print(f'{self._name} is NOT logged in.')
    
customer = User(
    name = 'Vladimir',
    password = 'goodpassword',
)
customer.login('Incorrect password')
customer.show_status()
customer.login('goodpassword')
customer.show_status()

class Admin(User):
    """admin"""
    
    def __init__(self, name, password, staff_id):
        """initialize data for admin"""
        super().__init__(name, password)
        self._staff_id = staff_id
    
    def add_product(self, name): 
        """add a new producr"""
        if self._logged_in:
            print(f'{self._name} ({self._staff_id}) added product {name}')
        else:
            print('Login to add product')
            
staff = Admin(
    name = 'Vladimir',
    password = 'good',
    staff_id = 1,
)
staff.add_product('Coffee')
staff.login('good')
staff.add_product('Coffee')
            


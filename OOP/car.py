class Car:
    """объекты машины"""
    
    def __init__(self, colour, make, model, miles=0):
        """ set details of car"""
        self.colour = colour
        self.make = make
        self.model = model
        self.miles = miles
        
    def add_miles(self, miles):
        """add miles"""
        self.miles += miles
        
    def display_miles(self):
        """показать текущее число миль"""
        print(
            f'{self.make} {self.model} ({self.colour}) '
            f'has driven {self.miles} miles.'
        )
    
astra = Car('Red', 'Vauxhall', 'Astra')
astra.display_miles()
astra.add_miles(100)
astra.display_miles()

Prius = Car('blue', 'Toyota', 'Prius', 1000)
Prius.display_miles()
Prius.add_miles(505)
Prius.display_miles()
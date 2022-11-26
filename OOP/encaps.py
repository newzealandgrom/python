class Student:
    """Represents students"""
    
    def __init__(self, name):
        """initialize data"""
        self._name = name
        self._years = []
        self._results = []
    
    def _calc_predicted_result(self):
        """calculate"""
        return sum(self._results) / len(self._years)
    
    def add_results(self, year, result):
        """add result for student"""
        self.years.append(year)
        self._results.append(result)
    
    def display_predicted_result(self):
        """display"""
        result = self._calc_predicted_result()
        print(f'Student {self._name} is predicted: {result}')

s = Student('One')
s.add_result(2020, 66)
s.add_result(2022, 55)
s.add_result(2021, 100)
s.display_predicted_result()







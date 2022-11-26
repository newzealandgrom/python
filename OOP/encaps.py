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
    
    def add_result(self, year, result):
        """add result for student"""
        self._years.append(year)
        self._results.append(result)
    
    def display_predicted_result(self):
        """display"""
        result = self._calc_predicted_result()
        print(f'Student {self._name} is predicted: {result}')


s = Student('One')
s.add_result(2020, 88)
s.add_result(2019, 76)
s.add_result(2018, 22)
s.display_predicted_result()














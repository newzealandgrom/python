class tempMixin:
    """convert"""
    
    def f_to_c(self, f):
        return (f - 32) / 1.8
    
    def c_to_f(self, c):
        return (c * 1.8) + 32

class DistanceMixin:
    
    def m_to_km(self, m):
        return m * 1.60934
    
    def km_to_m(self, km):
        return km * 0.6213712
    
class DigitalMixing:
    
    def gb_to_mb(self, gb):
       return gb * 1000 
    
    def mb_to_gb(self, mb):
        return mb / 1000

class Weather(tempMixin, DistanceMixin):
    
    def __init__(self, cel, kmph):
        self._cel = cel
        self._kmph = kmph
    
    def display(self, metric=True):
        if metric:
            temp = self._cel
            wind = self._kmph
        else:
            temp = self.c_to_f(self._cel)
            wind = self.km_to_m(self._kmph)
        print(f'Temp: {temp}, Wind {wind}')
        print('---END---')
    
london = Weather(12, 5)
london.display()
london.display(metric=False)

class HardDrive(tempMixin, DigitalMixing):
    def __init__(self, space, cel):
        self._space = space
        self._cel = cel
    
    def status(self, metric=True):
        if metric:
            temp = self._cel
        else:
            temp = celf._c_to_f(self._cel)
            
        space = self.mb_to_gb(self._space)
        print(f'space: {space}gb, temp: {temp}')
        print('---END---')

hd = HardDrive(6008000, 22)
hd.status()


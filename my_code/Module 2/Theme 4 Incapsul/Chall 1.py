class Temperature:
    def __init__(self, _celsius):
        self._celsius = _celsius
    
    @property
    def fahrenheit(self):
        F = (self._celsius * 9 / 5) + 32
        return F
    
    @fahrenheit.setter
    def fahrenheit(self, new_temp):
        self._celsius = (new_temp - 32) * 5/9
        

    


temp = Temperature(25)
print(temp.fahrenheit)
temp.fahrenheit = 100
print(temp._celsius)
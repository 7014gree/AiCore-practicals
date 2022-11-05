from dataclasses import dataclass

@dataclass(order=True)
class Temperature():
    #def __init__(self, temp: int):
    #    self.temp = temp
    temp: int

    def conv_to_far(self):
        return self.temp * 9  / 5 + 32
    
    @staticmethod
    def static_conv_to_celc(temp_as_far):
        return (temp_as_far - 32) * 5 / 9

    @staticmethod
    def is_temp_valid(temp_as_celc):
        return -273 < temp_as_celc < 3000

    @classmethod
    def temp_as_far(cls, temp):
        return cls(cls.static_conv_to_celc(temp))

    @classmethod
    def temp_zero(cls):
        return cls(0)

    @property
    def temp(self):
        print("Getting temperature value")
        return self._temp

    @temp.setter
    def temp(self, temp):
        if not self.is_temp_valid(temp):
            raise ValueError("Temperature must be between -273 and 3,000.")
        self._temp = temp
        
    @temp.deleter
    def temp(self):
        print("Deleting temperature value.")
        del self._temp


a = Temperature.temp_as_far(12)
print(a)
print(a.temp)
print(a.conv_to_far())
del(a.temp)
print(a)


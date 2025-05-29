class TV:
    def __init__(self, is_on = False, current_channel = None):
        self.is_on = is_on
        self.current_channel = current_channel
    
    def turn_on(self):
        self.is_on = True
      

    def turn_off(self):
        self.is_on = False
      

    def switch_channel(self, current_channel):
        if self.is_on == False:
            print('Телевизо выключен!')
        else:
            self.current_channel = current_channel
            return self.current_channel
        
tv = TV()
tv.turn_on()
tv.switch_channel(5)
print(tv.current_channel)  # 5
tv.turn_off()
tv.switch_channel(10)  # Должен вывести ошибку "Телевизор выключен!"
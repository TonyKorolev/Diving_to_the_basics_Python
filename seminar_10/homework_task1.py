class Fauna:

    def __init__(self, name: str, blood_color: str):
        self.name = name
        self.blood_color = blood_color

    def eat(self):
        print('I need food!')


class Birds(Fauna):
    def __init__(self, name: str, blood_color: str, feathers: bool):
        super().__init__(name, blood_color)
        self.feathers = feathers

    def fly(self):
        print('I can fly!')


class Fishes(Fauna):
    def __init__(self, name: str, blood_color: str, gills: bool):
        super().__init__(name, blood_color)
        self.gills = gills
        
    def breathe(self):
        print('I can breathe under water!')


class Reptiles(Fauna):
    def __init__(self, name: str, blood_color: str, scales: bool):
        super().__init__(name, blood_color)
        self.scales = scales
    
    def tail_falls_off(self):
        if self.name == 'Lizard Curt':
            print('My tail might fall off!')


class Factory:

    def __init__(self, name, *args):
        self.name = name
        self.args = args
        self.instance = self.__create_instance()

    def __create_instance(self):
        instance = globals()[self.name](*self.args)
        return instance

    # def get_attributes(self):
    #     return self.instance


if __name__ == '__main__':
    a = Factory('Reptiles', 'Lizard Curt', 'green', False).instance
    print(a.name)
    a.eat()
    a.tail_falls_off()
class Cars:
    '''
    A class for cars
    '''
    __reg_no = 100

    def __init__(self, brand, model, colour, engine_no):
        '''
        the constructor for cars
        '''
        self.brand = brand
        self.model = model
        self.colour = colour
        self.engine_no = engine_no

    def register(self):
        Cars.__reg_no += 1
        self.__reg_no = Cars.__reg_no
        return (f'KY {self.__reg_no} XQ')

class CarOwner(Cars):
    '''
    A class for car owners
    '''
    def __init__(self, brand, colour, owner, address):
        '''
         constructor for car owner
        '''
        super().__init__(brand, colour)
        self.owner = owner
        self.address = address
        self.email = f'{owner.lower()}@motor.com'

    def fname(self):
        fnm, snm = self.owner.split()
        return (fnm)

class CarVendor(Cars):
    pass

# car1 = Cars('Toyota', 'TX', 'black', 'CM 80098Z')

# print(f'the colour of car1 is {car1.colour}')

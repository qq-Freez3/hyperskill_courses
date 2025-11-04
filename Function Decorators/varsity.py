class CharType:

    @staticmethod
    def get_type(char):
        if char.isalpha():
            return 'letter'
        elif char.isdigit():
            return 'digit'
        else:
            return 'other'

class User:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return self.name + ' ' + self.surname

    @classmethod
    def from_string(cls, data): #alternate constructor
        name, surname = data.split(' ') #could use error catching here
        return cls(name, surname)  # passing the string values to the initialization call

if __name__ == '__main__':
    print(CharType.get_type('a'))  # letter
    print(CharType().get_type('1'))  # digit

    user = User.from_string('Santa Claus')  # using the class name to call the method
    user2 = User("Dante", "Inferno")
    print(user.full_name)  # Santa (Claus)
    print(user2.full_name)

    #random dancing
    ip = "124.595.382.21"
    oct1, oct2, oct3, oct4 = ip.split('.')
    print(oct3)
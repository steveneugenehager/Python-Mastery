class Vegetable():

    def __init__(self, in_name):
        self.name = in_name  # Naming with _ by convention means "private"

    def __str__(self):
        return(f'< OBJECT: name = \'' + self.name + '\' >')

    @property
    def name(self):
        """Getter for the name attribute"""
        return self._name

    @name.setter
    def name(self, in_name):
        """Setter for the name attribute with validation / formatting / etc."""
        #print("DEBUG: in name.setter")
        if not isinstance(in_name, str):
            raise ValueError("Vegetable.name must be a string")
        self._name = in_name.title()

vegetables = []
strings_to_test = ('pea', 1 , 1.23 , None , True, False )

# Build the objects
for string_to_test in strings_to_test:
    try:
        vegetables.append(Vegetable(string_to_test))
    except ValueError as ve:
        print("Warning!".upper() , ve)
    else:
        print('INFO|Object created.')
#Process the objects
for vegetable in vegetables:
    print(vegetable)
    print('\t' , 'before' , vegetable , f"{vegetable.name=}" , f"{vegetable._name=}" )
    vegetable.name = 'junk'
    print('\t' , 'after1' , vegetable , f"{vegetable.name=}" , f"{vegetable._name=}" )
    #The following is just used to demonstrate the setter can be bypassed vy breaking the convention of using a _var directly.
    vegetable._name = 'more junk'
    print('\t' , 'after2' , vegetable , f"{vegetable.name=}" , f"{vegetable._name=}" )
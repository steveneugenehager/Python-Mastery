class Vegetable():

    _names = []  #An example of a class.variable. Used here to store list of existing names

    def __init__(self, in_name):
        self.name = in_name   
        self.update_is_small()
        self.update_is_green()

    def __str__(self):
        return(f'< OBJECT: name = \'' + self.name + '\'; is_small = '+ str(self.is_small) + 
               '; is_green = '+ str(self.is_green) + ' >')
 
    @property
    def is_small(self):
        return self._is_small
    
    def update_is_small(self):
        match self.name:
            case 'Pea' | 'Cherry':
                self._is_small = True
            case 'Watermelon' | 'Pumpkin':
                self._is_small = False
            case _:
                self._is_small = None
    
    @property
    def is_green(self):
        return self._is_green
    

    def update_is_green(self):
        match self.name:
            case 'Pea' | 'Watermelon':
                self._is_green = True
            case 'Cherry' | 'Pumpkin':
                self._is_green = False
            case _:
                self._is_green = None
        
    @property
    def name(self):
        """Getter for the name attribute"""
        return self._name


    @name.setter
    def name(self, in_name):
        """Setter for the name attribute with validation / formatting / etc."""
        #Confirm input is a string.
        if not isinstance(in_name, str):
            raise ValueError(f"Vegetable.name must be a string. Found {type(in_name)}")
        #Strip whitespace and format the string.
        formatted_name = in_name.strip().title()
        #Confirm string is not empty.
        if not formatted_name:
            raise ValueError("Vegetable.name must not be blank.")
        #Confirm this is a unique vegetable.
        if formatted_name in Vegetable._names:
            raise ValueError(f"Vegetable with that name ('{formatted_name}') already exists.") 
        #Set the name
        self._name = formatted_name
        #Add the new vegetable to the list of existing vegetables
        Vegetable._names.append(self.name)

DEBUG=False
WARN=False
QUIET=False

vegetables = []
strings_to_test = ('pea', ' PEA  ' , 'cherry', 'watermelon' , 'pumpkin' , 'plum' , "" , 1 , True , None  , [] , ['cat'])
# Build the objects
for string_to_test in strings_to_test:
    try:
        vegetables.append(Vegetable(string_to_test))
    except ValueError as ve:
        print("WARNING." , ve) if WARN else None
    else:
        print(f"SUCCESS: Object ('{vegetables[-1].name}') created.") if DEBUG else None

if not QUIET:
    print('INFO: The following were created:')
    #Process the objects
    for vegetable in vegetables:
        print('\t' , vegetable)
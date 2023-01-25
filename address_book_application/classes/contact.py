class Contact():
    #TODO: Documentation
    '''
    Placeholder for doc
    '''

    def __init__(self, name, address, phone_number, e_mail) -> None:
        # TODO: Characterize inputs
        '''
        Placeholder for characterization
        '''
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
        self.__e_mail = e_mail

    # Getters
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

    def get_e_mail(self):
        return self.__e_mail

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_e_mail(self, e_mail):
        self.__e_mail = e_mail



from contact import Contact

class AddressBook():
    # TODO: Documentation
    '''
    Placeholder for doc
    '''

    __contact_list = [] # nem biztos, hogy használni kell privátot

    def __init__(self, contact_list) -> None:
        self.__contact_list = contact_list
    
    # Getter
    def get_contact_list(self):
        return self.__contact_list

    def set_contact_list(self, contact_list):
        self.__contact_list = contact_list
    
    # Methods
    def add_contact(self, contact: Contact):
        '''
        Add new contact to the address book
        :params:
        contact: the contact instance, will be added to the list, 
            type: Contact
        '''
        if contact not in self.__contact_list:
            self.__contact_list.append(contact)
        else:
            return

    def remove_contact(self, contact: Contact):
        '''
        Remove the given contact from the address book
        :params:
        contact: the contact instance, will be removed from the list,
            type: Contact
        '''
        self.__contact_list.remove(contact)

    def search_contact(self, contact: Contact):
        '''
        Search the given contact in the address book.
        If the contact in the list, return its results
        :params:
        contact: the contact instance, will be searched in the list,
            type: Contact
        '''
        if contact in self.__contact_list:
            return self.__contact_list[contact]
        else:
            return "The given contact can't be found, Check if the given name is correct!"

    def modify_contact(self, contact: Contact, changes: list):
        # TODO: Documentation
        '''
        Placeholder for doc
        '''
        if contact in self.__contact_list:
            contact.set_name(changes[0])
            contact.set_address(changes[1])
            contact.set_phone_number(changes[2])
            contact.set_e_mail(changes[3])

            return contact
        else:
            return 'Nothing to modify!'
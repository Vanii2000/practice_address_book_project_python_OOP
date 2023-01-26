import streamlit as st

from address_book import AddressBook
from contact import Contact

st.write('Hi User!')

address_book = AddressBook([1,2])

st.write('Your contacts:')

#st.expander('Valami'):
st.write('You still do not have any contacts!')

col1, col2, col3 = st.columns(3)

with col1:
    st.button('Create contact', on_click=add_contact_ui())

with col2:
    st.button(
        'Remove contact'
    )

with col3:
    st.button(
        'Edit'
    )

def add_contact_ui():
    new_contact = Contact() 
    with st.form('add_contact_form'):
        st.write('Add new contact for your address book')
        first_name = st.text_input(label='First name', max_chars=25)
        last_name = st.text_input(label='Last name', max_chars=25)
        
        city = st.text_input(label='City/town', max_chars=50)
        zip_code = st.number_input(label='Zip code', min_value=4, max_value=4)
        street = st.text_input(label='Street name', max_chars=50)
        house_number = st.number_input(label='House number', min_value=1, max_value=999)


        
    new_contact.set_name(first_name+ ', ' +last_name)
    new_contact.set_address(city + ', ' + zip_code + ' ' + street + ' ' + house_number)
    address_book.add_contact(new_contact)
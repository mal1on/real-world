import streamlit as st


def converter():
    '''Web app that converts kilometers to miles and vice-versa.'''

    options = ['Kilometers to miles', 'Miles to kilometers']
    st.title('Kilometers ⇔ Miles Converter')
    selected = st.radio('Choose the conversion direction:', options)

    match selected:
        case 'Kilometers to miles':
            units = 'kilometers'
            o_units = 'miles'
            conversion = 0.621371192

        case 'Miles to kilometers':
            units = 'miles'
            o_units = 'kilometers'
            conversion = 1.609344

    distance = st.number_input(
        f'Enter the distance in {units}:', min_value=0.0, step=0.1)

    if st.button('Convert'):
        result = distance * conversion
        st.write(f'{distance:.2f} {units} is equal {result:.2f} {o_units}.')


if __name__ == '__main__':
    converter()

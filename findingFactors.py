import streamlit as st

st.title('Finding the factors of a number...')
st.markdown("***")
st.text('')

st.subheader('Here is example of finding the factors of first 20 numbers...')
if st.checkbox('Show Example...'):
    numbers = 20
    n = 1
    while n <= numbers:
        factor = 1
        result = ''
        while factor <= n:
            if n % factor == 0:
                result += str(factor) + ' '
            factor += 1
        st.write(str(n) + ' : ' + result)
        n += 1
st.markdown("***")

st.subheader('Try testing with a number you like...')
st.text('')

number = int(st.number_input('Enter a number only.', step = 1))
if number < 0:
    st.error('Oops, number should not be less than zero! Please re-enter.')
else:
    factor = 1
    result = ''
    count = 0
    while factor <= number:
        if number % factor == 0:
            count += 1
            result += str(factor) + '  ' + '  '
        factor += 1
    if count == 0:
        st.write('Start testing  :sunglasses:  :sunglasses:')
    elif count == 1:
        st.write("The factor of the number " , number , " is " + result)
    else:
        st.write("The factors of the number " , number , " are " + result)

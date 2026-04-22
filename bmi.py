import streamlit as st
st.title("Welcome to the BMI calculator")

weight = st.number_input("enter your weight in kgs")
status = st.radio("select your height format", ("cm", "meters", "feet"))

try:
    if status == "cm":
        height = st.number_input("cm")
        bmi = weight / (height/100)**2
    elif status == "meters":
        height = st.number_input("meters")
        bmi = weight / height**2
    elif status == "feet":
        height = st.number_input("feet")
        bmi = weight / (height/3.2808)**2
except ZeroDivisionError:
    print("zero division error")

if(st.button("calculate BMI")):
    st.write(f"your BMI index is {bmi:.2f}")
    
    if bmi < 16:
        st.write("you are extremely underweight")
    elif bmi >= 16 and bmi < 18.5:
        st.write("you are underweight")
    elif bmi >= 18.5 and bmi < 25:
        st.write("you are healthy")
    elif bmi >= 25 and bmi < 30:
        st.write("you are overweight")
    else:
        st.write("you are extremely overweight")
    st.balloons()
import streamlit as st
# --------------------------------------------
# The title of the page
st.set_page_config(page_title="Engineering calc")
# --------------------------------------------

# creates a blue box of text for info
st.info(" <- Click on the top left arrow to choose a performance car")


# -----------------------------------------------------------------------------------------------------------------
# The following gives a collection of text for the user to read about the calculator
st.title("Welcome to the EngineeringCalc!")

st.write(
        "An Educational calculator created to optimize efficiency and speed for solving simple Engineering problems")
st.subheader("ABOUT:")
st.write("This is an Educational tool helping"
         " aspiring automotive engineers understand more about cars, equations and general automotive engineering; where you can choose different"
         " settings to calculate some essential equations such as g-forces that can be experienced in high speeds and rapid acceleration from 0-60 mph"
         " in the following performance cars:")
st.write("Sports cars - balance everyday usability with enjoyable performance; relatively accessible and affordable.")
st.write("f1 cars - the center of motorsport racing where precision is critical and small errors can cost a win")
# -----------------------------------------------------------------------------------------------------------------
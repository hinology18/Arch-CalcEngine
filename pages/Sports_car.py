import streamlit as st
import math

# title of page
st.title("SPORTS CAR")

# Formulas for different objectives in a sports car --> (force, power, torque)
def force_equation():
    # st.latex() displays numbers better than plain images off google
    st.latex(r"Force = Mass \times Acceleration")
    # asks for the Mass in an input box
    mass = st.number_input("Mass:")
    # st.number_input() asks for a specific value to be placed in an input box
    acceleration = st.number_input("Acceleration:")
    # this calculates the force
    force = mass * acceleration
    # default unit as Newtons
    units = "Newtons"
    force_conversion = st.selectbox("Select units to convert to", ["Newtons", "Dyne"])
    if force_conversion == "Dyne":
        # multiplies the current answer from Newtons to dyne by 10 to the power of -5
        force = force * (10**-5)
        # unit name change which happens for all unit conversions in other equations too
        units = "Dyne"
    # displays the result and the units
    st.success(f"The result is: {force} {units}")
def power_equation():
    st.latex(r"P = \frac{w}{t}")
    try:
        work_done = st.number_input("Work done:")
        time = st.number_input("Time:")
        power = work_done / time
        units = "watts"
        power_conversion = st.selectbox("Select units to convert to", ["watt","Horsepower","Megawatt","Gigawatt","Kilowatt"])
        if power_conversion == "Horsepower":
            power = power / 745.7
            units = "Horsepower"
        elif power_conversion == "Megawatt":
            power = power / 1000000
            units = "Megawatt"
        elif power_conversion == "Kilowatt":
            power = power / 1000
            units = "Kilowatt"
        elif power_conversion == "Gigawatt":
            power = power / 1000000000
            units = "Gigawatt"
        st.success(f"The result is: {power} {units}")
    except ZeroDivisionError:
        st.error("Enter a value that is NOT divisible by zero before you continue...")
def torque_equation():
    try: # checks for an error in this specific block of code
        st.latex(r" T = \frac {60 \times P} {2\pi \times RPM}")
        power = st.number_input("Power:")
        rpm = st.number_input("Revolutions per minute:")
        numerator = 60 * power
        denominator = (2 * math.pi) * rpm
        torque = numerator / denominator
        units = "Newton meters"
        torque_conversion = st.selectbox("Select units to convert to",
                                       ["Newton meters", "Newton cm", "newton mm"])
        if torque_conversion == "Newton cm":
            torque = torque * 100
            units = "Newton cm"
        elif torque_conversion == "Newton mm":
            torque = torque * 1000
            units = "Newton mm"
        st.success(f"The result is {torque} {units}")
    except ZeroDivisionError: # creates an exception which displays text in a red box instead of crashing the program
        st.error("Enter a value that is NOT divisible by zero")
        # each tab makes the others non-visible displaying unique block of code
tab1, tab2, tab3, tab4 = st.tabs(["[Main tab]","[Force calculator]","[Power calculator]","[Torque calculator]"])

with tab1:
    if st.button("<- Back to menu"):
        # goes back to the main menu of the website
        st.switch_page("Main.py")
    st.subheader("Info:")
    st.write("The following sections above in square brackets covers equations that help calculate and give information"
             " on common problems found specifically in sports cars")
    st.subheader("What are Sports Cars? :")
    st.write("Sports cars are a nice mix of speed, usability and affordability in engineering. They aim to still have some"
             " thrill that other more extreme cars have without investing heavily into absolutely world class performance. "
             "They're a nice way to test aerodynamics and engine setups which may influence more general commuter cars.")
with tab2:
    Force_Explanation,Force_equation = st.columns(2) # specifies what each side of the page contains as text
    with Force_Explanation: # with col
        st.subheader("What even is Force?")
        st.write("Force is a push/pull, the result of an object’s mass multiplied by its acceleration. In sports cars, this means the greater the mass or the faster"
                 " the change in speed (acceleration), the larger the forces involved. In a more practical setting like the road, aerodynamic force can press down"
                 " onto the tires of sports cars creating downforce. Increasing normal force on tires, which can improve handling without adding excessive"
                 " mass and staying street legal unlike f1 cars")
        st.subheader("Extra facts about sports cars:")
        st.write("We can actually rearrange the equation so that acceleration = force/mass (See more of this in the f1 car section)"
                " For sports cars, this means that a lighter car lead to faster acceleration on the road.")
    with Force_equation:
        force_equation() # calls the name of the function allowing the equation to be visible and used
with tab3:
        Power_explanation, Power_equation = st.columns(2)
        with Power_explanation:
            # subheader as a mini - title
            st.subheader("What is power and how do you apply it to cars?")
            st.write("Power is the rate of work being done. In simple terms, it's how fast chemical energy from the engine can be converted"
                    " to kinetic energy to make the car accelerate. Work done is the energy being transferred from the car's fuel to make the car move;"
                    " this directly links back to mass because, lighter cars made of carbon fiber for example have smaller inertia. Which in result, leads to less time being"
                    " spent getting the car to reach top speed.")
        with Power_equation:
          power_equation()
with tab4:
    Torque_explanation, Torque_equation  = st.columns(2)
    with Torque_explanation:
        st.subheader("What even is Torque and how does it compare to horsepower?")
        st.write("Torque is the turning force in the engine transferred to the wheels that helps a car accelerate rapidly. However, for balanced performance in"
                " sports cars such as the Porsche 911, horsepower is also needed to achieve high speeds on the motorway.")
        st.subheader("Low gear VS High gear")
        st.write("In low gears, torque is strongest, making it perfect for quick launches and climbing hills. In high gears, horsepower dominates, keeping the car flying"
                " at top speed. Sports cars are engineered to strike a balance, delivering both explosive "
                "acceleration and top-end performance.")
    with Torque_equation:
        torque_equation()
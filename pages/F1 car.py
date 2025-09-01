import streamlit as st

st.title("F1 Car")

# Formulas for different objectives in a sports car --> (Downforce, Acceleration, G-Force)
def downforce_equation():
    # st.latex() displays numbers better than plain images off google
    st.latex(r"Downforce = \frac {1}{2} \times p \times v^2 \times C_L \times a")
    # asks for the air density in the input box
    p = st.number_input("p = Air density:")
    # st.number_input() asks for a specific value to be placed in an input box that matches the description
    v = st.number_input("v = Velocity:")
    cl = st.number_input("CL = lift coefficient:")
    a = st.number_input("a = reference area of the wing or body generating downforce:")
    # this calculates the downforce
    downforce = 1/2 * p * pow(v,2) * cl * a
    units = "N"
    downforce_conversion = st.selectbox("Select units to convert to", ["Newtons","Kilonewtons", "Kilogram-force"])
    if downforce_conversion == "Kilonewtons":
        downforce = downforce * 0.001
        units = "KN"
    elif downforce_conversion == "Kilogram-force":
        downforce = downforce * (1/9.81)
        units = "Kgf"
    st.success(f"The result is: {downforce} {units}")
def acceleration_equation():
    st.latex(r"A = \frac{f}{m}")
    try:
        force = st.number_input("Force:")
        mass = st.number_input("Mass:")
        # this calculates the acceleration
        acceleration = force / mass
        units = "m/s squared"
        acceleration_conversion = st.selectbox("Select units to convert to", ["m/s squared","km/h per second","mph per second","g-force"])
        if acceleration_conversion == "km/h per second":
            acceleration = acceleration * 3.6
            units = "km/h per second"
        elif acceleration_conversion == "mph per second":
            acceleration = acceleration * 2.237
            units = "mph/h"
        elif acceleration_conversion == "g-force":
            acceleration = acceleration * 0.102
            units = "gs"

        st.success(f"The result is: {acceleration} {units}")
    except ZeroDivisionError:
        st.error("Enter a value that is NOT divisible by zero before you continue...")
def g_force_equation():
    try: # checks for an error in this specific block of code
        st.latex(r" n_g = \frac{v^2} {r \times 9.81}")
        v = st.number_input("speed of the car (v) :")
        r = st.number_input("Radius of the turn (r):")

        # this calculates the downforce
        g_force = v/(r*9.81)

        st.success(f"The result is {g_force} Gs")
    except ZeroDivisionError: # creates an exception which displays text in a red box instead of crashing the program
        st.error("Enter a value that is NOT divisible by zero")

# TABS HERE...

tab1, tab2, tab3, tab4 = st.tabs(["[F1 car main tab]","[Acceleration calculator]","[Downforce calculator]","[G-Force calculator]"])

with tab1:
    if st.button("<- Back to menu"):
        # goes back to the main menu of the website
        st.switch_page("Main.py")
    st.subheader("Info:")
    st.write("The following sections above in square brackets covers equations that help calculate and give information"
             " on common problems found specifically in F1 cars")
    # subheader as a mini - title
    st.subheader("F1 Cars:")
    st.write("F1 is the pinnacle of motorsport, crafting cars using highly advanced technology to not just win races but push the limits of general "
             "automotive and mechanical engineering on a global scale. However, usability and affordability have to be sacrificed to make sure that the ultimate goal is reached. it's the amalgamation of driver expertise and handling along with the critical"
             " scientific thinking of engineers. You'll find out in this section about the extreme downforce these automobiles experience, some regulations by the FIA and much more.")

with tab2:
    acceleration_explanation, acceleration_calculation = st.columns(2)

    with acceleration_explanation:
        st.subheader("Acceleration in an F1 Car:")
        st.write("Acceleration is change in velocity over time or in this case, can also be dependent on the car's force/mass."
                 " As of 2025 since acceleration is critical for performance and to enhance fairness, the FIA "
                 " decided that the minimum weight an F1 car must be to qualify is 800 Kg with no rules on maximum weight. But as you'll"
                 " begin to notice when you use the equation, you'd want your car to be as light as possible according to regulations for optimal speed")
        st.subheader("Limiting factors of acceleration")
        st.write("F1 car's rely on good tyre grip to transfer torque onto the wheels for forward motion. However, if the engine generates more torque than the tyres can handle acceleration can be lost.")
        st.write("Downforce despite improving tire grip, comes with drag limiting acceleration on the straights. Which is crucial for overtaking")


    with acceleration_calculation:
        # ACCELERATION EQUATION
        acceleration_equation()

with tab3:
    downforce_explanation, downforce_calculator = st.columns(2)

    with downforce_explanation:
        st.subheader("What's downforce and it's benefits:")
        st.write("Downforce is an aerodynamic force that increases with the square of speed, pushing down vertically on the car as it accelerates."
                 " This improves tyre grip allowing the f1 car to maintain speeds on the corners. It's the opposite of lift on a plane pushing the car"
                 " downwards instead of upwards; that way it has a lower center of gravity.")
        st.subheader("The disadvantages of downforce:")

        st.write("With more downforce on the automobile, there's an increase in drag which can slow the car down limiting top speed on the straights. To counter this from 2011,"
                 " the FIA introduced a system known as the DRS which only activates in designated zones ensuring safety"
                 ". This is being changed for 2026 with MOM (manual overdrive mode). As an alternative to a movable car wing, MOM gives the pursuing driver"
                 " access to additional battery power. However the defending driver can't use the same boost.")
    with downforce_calculator:
        # DOWNFORCE Equation
        downforce_equation()
    with tab4:
        G_force_Explanation, G_force_calculator = st.columns(2)

        with G_force_Explanation:
            st.subheader("What's (Lateral) G-force:")
            st.write("G-force is the acceleration experienced relative to the gravity of earth (1g being Earth's normal gravity)."
                 " drivers can experience up to 6g on corners laterally. This can help determine how much a driver can keep on"
                     " pushing which prevents a list of things: reduced reaction time, blacking out, fatigue. In case these "
                     " things do go horribly wrong, the HANS can stabilize the diver's neck during high collision.")
            st.subheader("Crash G-Force (Deceleration):")
            st.write("F1 car's are designed to absorb massive crash forces (crumple zones and survival shell)."
                     " Crash g is not a joke and can reach up to 50g such as the crash Max Verstappen experienced in 2021."
                     " This is why the FIA requires F1 cars to pass multiple crash tests including: ")
            st.write("frontal impact - Sees if the cockpit can survive")
            st.write("nose crash test - Ensures the front absorbs energy efficiently such as the HANS")

        with G_force_calculator:
            # G-FORCE Equation
            g_force_equation()
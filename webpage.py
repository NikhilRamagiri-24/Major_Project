import streamlit as st
import warnings
import pickle
import numpy as np

warnings.filterwarnings('ignore')

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

file1 = open('scaling1.pkl', 'rb')
file2 = open('svc.pkl', 'rb')

scale = pickle.load(file1)
svc = pickle.load(file2)

st.write("Damage Propagation Modeling for Aircraft Engine Run-to-Failure Simulation")
st.image('aircraft.jpg')
st.write("== Please Enter Sensor Reading Values")

a = st.number_input('(LPC Outlet Temperature) (R)', step=0.01, format='%2f')
b = st.number_input('(HPC Outlet Temperature) (R)', step=0.01, format='%2f')
c = st.number_input('(LPT Outlet Temperature) (R)', step=0.01, format='%2f')
d = st.number_input('(HPC Outlet Pressure) (psia)', step=0.01, format='%2f')
e = st.number_input('(Physical Fan Speed) (rpm)', step=0.01, format='%2f')
f = st.number_input('(HPC Outlet Static Pressure) (psia)', step=0.01, format='%2f')
g = st.number_input('(Ratio of Fuel Flow to Ps38) (pps/psia)', step=0.01, format='%2f')
h = st.number_input('(Corrected Fan Speed) (rpm)', step=0.01, format='%2f')
i = st.number_input('(Bypass Ratio)', step=0.01, format='%2f')
j = st.number_input('(Bleed Enthalpy)', step=0.01, format='%2f')
k = st.number_input('(High-Pressure Turbines Cool Air Flow)', step=0.01, format='%2f')
l = st.number_input('(Low-Pressure Turbines Cool Air Flow)', step=0.01, format='%2f')

if st.button('Predict'):
    # Check if any field is left empty
    if any([a == 0, b == 0, c == 0, d == 0, e == 0, f == 0, g == 0, h == 0, i == 0, j == 0, k == 0, l == 0]):
        st.warning("Please fill in all the fields before predicting.")
    else:
        X = [a, b, c, d, e, f, g, h, i, j, k, l]
        features = np.array([X])
        X_scaled = scale.transform(features)
        Y_pred = svc.predict(X_scaled)[0]

        if Y_pred == 1:
            st.image('sign1.jpg')
            st.write('Preventive maintenance is required for the jet engine')
            st.write('30 or less cycles are left before damage of engine')
        else:
            st.image('sign_else.jpg')
            st.write('Preventive maintenance is not required for the jet engine')
            st.write('more than 30 cycles are left before damage of engine')

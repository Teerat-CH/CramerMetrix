import streamlit as st
st.write("""
### Cramer's Metrix

""")
st.write("please enter each value in order")

st.write("""
--     --
|a, b, c|\n
|d, e, f|\n
|g, h, i|\n
--     --
""")
print("a",",","b",",","c")
print("d",",","e",",","f")
print("g",",","h",",","i")

a = st.number_input("please enter the value of a : ",min_value=0, max_value=10, step=1)
b = st.number_input("please enter the value of b : ",min_value=0, max_value=10, step=1)
c = st.number_input("please enter the value of c : ",min_value=0, max_value=10, step=1)
d = st.number_input("please enter the value of d : ",min_value=0, max_value=10, step=1)
e = st.number_input("please enter the value of e : ",min_value=0, max_value=10, step=1)
f = st.number_input("please enter the value of f : ",min_value=0, max_value=10, step=1)
g = st.number_input("please enter the value of g : ",min_value=0, max_value=10, step=1)
h = st.number_input("please enter the value of h : ",min_value=0, max_value=10, step=1)
i = st.number_input("please enter the value of i : ",min_value=0, max_value=10, step=1)


detA = ((a*e*i)+(b*f*g)+(d*h*c))-((g*e*c)+(a*h*f)+(d*b*i))

st.write("please enter each value in order")
st.write("""
--  --
| A1 |\n
| A2 |\n
| A3 |\n
--  --
""")

A1 = st.number_input("please enter the value of A1 : ",min_value=0, max_value=10, step=1)
A2 = st.number_input("please enter the value of A2 : ",min_value=0, max_value=10, step=1)
A3 = st.number_input("please enter the value of A3 : ",min_value=0, max_value=10, step=1)

detX = ((A1*e*i)+(b*f*A3)+(A2*h*c))-((A3*e*c)+(A1*h*f)+(A2*b*i))
detY = ((a*A2*i)+(A1*f*g)+(d*A3*c))-((g*A2*c)+(a*A3*f)+(d*A1*i))
detZ = ((a*e*A3)+(b*A2*g)+(d*h*A1))-((g*e*A1)+(a*h*A2)+(d*b*A3))

X = detX/detA
Y = detY/detA
Z = detZ/detA

st.write("det A = ",detA)
st.write("det X = ",detX)
st.write("det Y = ",detY)
st.write("det Z = ",detZ)

st.write("the answer of X is : ",X)
st.write("the answer of Y is : ",Y)
st.write("the answer of Z is : ",Z)
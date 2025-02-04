import streamlit as st

st.title("2D Design")
st.write("""I started diving into 2D/graphic design when I installed Adobe Illustrator as a kid, I would simply
         try to create an idea and when I didn't know how to do something I would look on the internet.  
         These are some examples of the things I have created:""")

col1, col2, col3 = st.columns(3)

col1.image("images/2d_design/gvlogo.jpg", width=300, caption="Logo for my climbing association")
col2.image("images/2d_design/cami.png", width=300, caption="Design for a t-shirt")
col3.image("images/2d_design/pezleon.png", width=300, caption="Tattoo design of a lionfish")


import streamlit as st

st.title("Photography") 
st.write("""I've always liked fidling with cameras, I normally take photos because I like how they look, without 
         any hidden message. These are some of the pictures that I have taken over the years that I like the most:""")

image_folder = "images/photography/"
image_files = [
    "_MG_7220.JPG",
    "PAF (1 of 1)-2.JPG",
    "_MG_8607.JPG",
    "_MG_8764.JPG",
    "_MG_8550.JPG",
    "rojo.jpg",
    "vlcsnap-2016-08-21-11h28m54s479.png",
    "White.jpg",
]

cols = st.columns(3) 

for index, filename in enumerate(image_files):
    with cols[index % 3]:
        st.image(image_folder + filename, use_column_width=True)
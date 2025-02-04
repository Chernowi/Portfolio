import streamlit as st

st.title("Climbing")
st.write("""Throughout the years climbing has taken me to incredible places 
        with incredible people that are now my friends :)""")

image_folder = "images/climbing/"
image_files = [
    "IMG_0365.HEIC",
    "IMG_1665.PNG",
    "IMG_3533.jpeg",
    "IMG_20230611_191611.jpg",
    "E8695430-BDB4-44E4-8706-B85D58D3225A.JPG",
    "3204261F-154C-4E52-8B3D-65A645238CE5.JPG",
]

cols = st.columns(3) 

for index, filename in enumerate(image_files):
    with cols[index % 3]: 
        st.image(image_folder + filename, use_container_width=True)
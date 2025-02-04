import streamlit as st

st.title("3D Design")
st.write("""A few years ago I bought a 3D printer to learn how to design and print parts, I have ended up using it
         way more than what I would've imagined, it turns out there are a lot of things that are easier to 3D print
         than to buy, from small motorbike parts, to household items that break, and of course small inventions.
         Overall I have designed and printed more than a hundred parts, its been a great way to learn how to 
         design in 3D.""")

st.image("images/3d_design/printer.jpg", width=350, caption="My 3d printer, printing a fin for my surfboard")

image_folder = "images/3d_design/"
image_files = [
    ("cana.png", "Climbing clip-stick"),
    ("fisu1.png", "Climbing nut inspired keychain holder"),
    ("fisu2.png", "Another, bigger keychain holder"),
    ("molde.png", "A mold for casting the keychain holders in cement"),
    ("moto.png", "One of my motorbike's footpegs broke so I printed a replacement"),
    ("pegatas.png", "A contraption I made to use a selfie stick to place stickers in high places"),
]

cols = st.columns(3)

for index, (filename, caption) in enumerate(image_files):
    with cols[index % 3]: 
        st.image(image_folder + filename, caption=caption, use_container_width=True)

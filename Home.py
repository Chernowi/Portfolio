import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")

st.title("Welcome to my Blog/Portfolio")
st.image("images/home/mi_careto.jpg", width=300)
st.write("""Hi, I'm Pedro Agundez Fernandez, I have created this blog/portfolio to show everything
         I would not include in my programmer's CV, as of now this blog includes my 2D and 3D design projects,
         some photographies I have done and a bit of my climbing journey.  
         I believe creativity and curiosity are fundamental tools for both personal enjoyment and 
         professional development, this is an attempt to show a bit of both.  
         None of the things I show here are big projects but rather the result of my self-taught journey into
         different disciplines.""")

st.markdown(
        """
        ### 📸 Image Usage & License  

        All images on this page are licensed under the **Creative Commons Attribution (CC BY 4.0) License**.  
        This means you are **free to share and adapt** the images as long as you **give appropriate credit** to the author.  

        #### ✅ You are free to:  
        - **Share** – Copy and redistribute the images in any medium or format.  
        - **Adapt** – Remix, transform, and build upon the images for any purpose, even commercially.  

        #### ⚠️ Under the following terms:  
        - **Attribution** – You must give appropriate credit, provide a link to the license, and indicate if changes were made.  

        [🔗 Learn more about CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)  
        """,
        unsafe_allow_html=True
    )

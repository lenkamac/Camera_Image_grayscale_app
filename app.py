import streamlit as st
from PIL import Image
from io import BytesIO


st.title('Color to Grayscale Converter')

# Create a file uploader component allowing the user upload a file

uploaded_image = st.file_uploader('Choose an image')

with st.expander('Start Camera'):
    # Start the camera
    camera_image = st.camera_input('Camera')

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)
    # Convert pillow img to gray scale
    gray_img = img.convert('L')
    # Render the gray image on the webpage
    st.image(gray_img)

    buf = BytesIO()
    gray_img.save(buf, format='JPEG')
    byte_img = buf.getvalue()

    st.download_button('Download Image',
                       data=byte_img, key='camera_image',
                       file_name='Download Image')

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert('L')
    st.image(gray_img)

    buf = BytesIO()
    gray_img.save(buf, format='JPEG')
    byte_img = buf.getvalue()

    st.download_button('Download Image',
                       data=byte_img, key='upload_image',
                       file_name='Download Image')

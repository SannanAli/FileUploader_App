import streamlit as st
from PIL import Image


#image load method
def loadImg(image):
    img = Image.open(image)
    return img


def run_image_app():

    st.subheader('Image')
    image_Fileuploaded = st.file_uploader('Upload An Image', type=['png', ' jpg' , 'jpeg']) 

    if image_Fileuploaded is not None:
            
            st.subheader('Image Details')
            #to see Details/type
            st.write(type(image_Fileuploaded))

            #to see Attributes and Methods
            #st.write(dir(image_Fileuploaded))

            image_FileDetails = {
                'Image Name':image_Fileuploaded.name,
                'Type':image_Fileuploaded.type,
                'Size' : image_Fileuploaded.size
            }
            st.json(image_FileDetails)

            st.subheader(image_Fileuploaded.name)

            st.image(loadImg(image_Fileuploaded))



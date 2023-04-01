import streamlit as st
from app_image import  run_image_app
from app_datasets import run_dataset_app
from app_Docx import run_Docx_app

PAGE_CONFIG = {
    'page_title':'FileUploader',
    'page_icon':'random',
    'layout':'centered',
    'initial_sidebar_state':'expanded'
}

st.set_page_config(**PAGE_CONFIG)


def main():
    st.title('Upload Your Files Here 📁')

    menu = ['Image', 'Datasets', 'Doc Files', 'About']
    choices = st.sidebar.selectbox("Menu",menu)

    if choices == 'Image':
        run_image_app()

    elif choices == 'Datasets':
        run_dataset_app()

    elif choices == 'Doc Files':
        run_Docx_app()
    
    else:
        st.subheader('About')


if __name__ == '__main__':
    main()
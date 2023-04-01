import streamlit as st
import pandas as pd

#Data load method
def loadDatafile(Datafile):
    data = pd.read_csv(Datafile)
    return data

def run_dataset_app():
    st.subheader('Datasets')

    data_fileUploaded = st.file_uploader('Upload CSV File',type='CSV')

    if data_fileUploaded is not None:

            st.subheader('Datafile Details')

            st.write(type(data_fileUploaded))

            #st.write(dir(data_fileUploaded))

            data_fileDetails = {
                'File Name' : data_fileUploaded.name,
                'Type' : data_fileUploaded.type,
                'Size' : data_fileUploaded.size
            }

            st.json(data_fileDetails)

            st.subheader(data_fileUploaded.name)
            st.dataframe(loadDatafile(data_fileUploaded))

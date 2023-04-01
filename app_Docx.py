import streamlit as st
import docx2txt
from PyPDF2 import PdfReader
import pdfplumber


#Docx loadPDF method
def loadPDF(PdfFile):
    pdfFile = PdfReader(PdfFile)
    count = len(pdfFile.pages)
    all_pages_text = ''
    for i in range(count):
        pages = pdfFile.pages[i]
        all_pages_text += pages.extract_text()
    return all_pages_text

def run_Docx_app():

    st.subheader('Doc Files')

    dox_fileUploaded = st.file_uploader('Upload a Document File' , type=['pdf', 'docx' , 'txt'])

    if st.button('Process'):
            if dox_fileUploaded is not None:
                data_fileDetails = {
                'Document Name' : dox_fileUploaded.name,
                'Type' : dox_fileUploaded.type,
                'Size' : dox_fileUploaded.size
            }
                
                st.json(data_fileDetails)

                if dox_fileUploaded.type == "text/plain":
                    #Read as Bytes
                    # text_file = dox_fileUploaded.read()
                    # st.write(text_file) # is reads as in bytes

                    #st.text(text_file) this will not work only st.write will work for text file

                    #Read as string (Decode byte to string)
                    string_text = str(dox_fileUploaded.read(),'utf-8')
                    #st.write(string_text) #works
                    st.text(string_text) #also works
                
                elif dox_fileUploaded.type == "application/pdf":
                    # try:
                    #     with pdfplumber.open(dox_fileUploaded) as pdf:
                    #         pages = pdf.pages[0]
                    #         st.write(pages.extract_text())
                    # except:
                    #     st.warning('Exception Occured')

                    #Using PyPDF2
                    st.subheader(dox_fileUploaded.name)
                    pdf_file = loadPDF(dox_fileUploaded)
                    st.write(pdf_file)


                else:
                    docx_file = docx2txt.process(dox_fileUploaded)

                    st.write(docx_file) #works

                    #st.text(docx_file) #works




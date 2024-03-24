import streamlit as st
import google.generativeai as genai
from apikey import gemini_api_key
import streamlit as st
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

genai.configure(gemini_api_key)

def get_pdf_text(url):
    # Extract text from PDF using a PDF parsing library
    # You can use libraries like PyPDF2 or pdfminer.six
    # and return the extracted text
    pass

def get_paper_summary(url):
    # Fetch the PDF file from the given URL
    response = requests.get(url)
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the link to the PDF file
    pdf_link = soup.find('a', href=True, text='PDF')
    if pdf_link:
        # Get the URL of the PDF file
        pdf_url = pdf_link['href']
        # Extract text from the PDF file
        pdf_text = get_pdf_text(pdf_url)
        # Generate a summary of the paper using gensim's summarize function
        summary = summarize(pdf_text)
        return summary
    else:
        return None

def main():
    st.title("Research Paper Summary Generator")
    url = st.text_input("Enter the URL of a research paper PDF:")
    if st.button("Generate Summary"):
        if url:
            summary = get_paper_summary(url)
            if summary:
                st.success(summary)
            else:
                st.error("Failed to extract PDF or generate summary.")
        else:
            st.warning("Please enter a valid URL.")

if __name__ == "__main__":
    main()
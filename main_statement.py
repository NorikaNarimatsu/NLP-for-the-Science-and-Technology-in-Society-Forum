import requests
from PyPDF2 import PdfReader
import os
import pandas as pd

# Ensure the downloads directory exists
DOWNLOAD_DIR = "downloads_statement"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_pdf(url, filename):
    response = requests.get(url)
    response.raise_for_status()  # Check that the request was successful
    filepath = os.path.join(DOWNLOAD_DIR, filename)
    with open(filepath, 'wb') as f:
        f.write(response.content)
    return filepath

def pdf_to_text(filepath):
    with open(filepath, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

def extract_year_from_url(url):
    # Extract the year from the URL
    try:
        year = url.split('/')[4]
    except IndexError:
        year = "Unknown"
    return year

def process_pdfs(urls):
    data = []
    starting_year = 2005

    for i, url in enumerate(urls):
        try:
            filename = url.split('/')[-1]
            year = starting_year + i
            print(f"Processing {filename} from year {year}...")

            # Download the PDF from the URL
            filepath = download_pdf(url, filename)

            # Process the downloaded PDF
            text = pdf_to_text(filepath)
            data.append({"Year": year, "Text": text})

            # # Optionally, clean up the downloaded PDF file
            # os.remove(filepath)

        except Exception as e:
            print(f"Failed to process {url}: {e}")

    return data

urls = [
	"https://www.stsforum.org/file/2018/07/2005_Statement.pdf",
	"https://www.stsforum.org/file/2018/07/2006_Statement.pdf",
	"https://www.stsforum.org/file/2018/07/2007_Statement.pdf",
	"https://www.stsforum.org/file/2018/07/2008_Statement.pdf",
	"https://www.stsforum.org/file/2018/07/2009_Statement.pdf",
	"https://www.stsforum.org/file/2018/07/2010_Statement.pdf",
    "https://www.stsforum.org/file/2018/07/2011_Statement.pdf",
	"https://www.stsforum.org/file/2018/07/2012_Statement.pdf",
	"https://www.stsforum.org/file/2018/07/2013_Statement.pdf",
	"https://www.stsforum.org/file/2018/07/2014_Statement.pdf",
	"https://www.stsforum.org/file/2018/07/2015_Statement.pdf",
    "https://www.stsforum.org/file/2018/07/2016_Statement.pdf",
	"https://www.stsforum.org/file/2018/07/2017_Statement.pdf",
	"https://www.stsforum.org/file/2018/10/STS-Statement-2018.pdf",
	"https://www.stsforum.org/file/2019/10/Statement-2019.pdf",
	"https://www.stsforum.org/file/2020/10/Statement-2020.pdf",
    "https://www.stsforum.org/file/2021/10/18th-Annual-Meeting-Statement.pdf",
	"https://www.stsforum.org/file/2022/11/19th_Annual_Meeting_Statement.pdf",
	"https://www.stsforum.org/file/2023/11/the_20th_Annual_Meeting_Statement.pdf",
]



data = process_pdfs(urls)

# Create a DataFrame and save it as a CSV
df = pd.DataFrame(data)
df.to_csv("summaries_statement.csv", index=False)

print("CSV file saved as summaries_statement.csv")

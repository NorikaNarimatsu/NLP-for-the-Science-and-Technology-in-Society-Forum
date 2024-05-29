import requests
from PyPDF2 import PdfReader
import os
import pandas as pd

# Ensure the downloads directory exists
DOWNLOAD_DIR = "downloads"
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
    starting_year = 2004

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
	"https://www.stsforum.org/file/2018/07/2004_Summary.pdf",
	"https://www.stsforum.org/file/2018/07/2005_Summary.pdf",
	"https://www.stsforum.org/file/2018/07/2006_Summary.pdf",
	"https://www.stsforum.org/file/2018/07/2007_Summary.pdf",
	"https://www.stsforum.org/file/2018/07/2008_Summary.pdf",
	"https://www.stsforum.org/file/2018/07/2009_Summary.pdf",
	"https://www.stsforum.org/file/2018/07/2010_Summary.pdf",
    "https://www.stsforum.org/file/2018/07/2011_Summary.pdf",
	"https://www.stsforum.org/file/2018/07/2012_Summary.pdf",
	"https://www.stsforum.org/file/2018/07/2013_Summary-.pdf",
	"https://www.stsforum.org/file/2018/12/Summary-2014-for-web.pdf",
	"https://www.stsforum.org/file/2018/12/Summary-2015-for-web.pdf",
	"https://www.stsforum.org/file/2018/12/Summary-2016-for-web-Link.pdf",
	"https://www.stsforum.org/file/2018/12/Summary-2017-for-web-Link.pdf",
    "https://www.stsforum.org/file/2018/12/Summary-2018-for-web-Link.pdf",
    "https://www.stsforum.org/file/2019/11/Summary-2019-for-web-Link.pdf",
    "https://www.stsforum.org/file/2020/12/STS-forum-2020-Summary.pdf",
    "https://www.stsforum.org/file/2021/12/STS-forum-2021-Summary.pdf",
    "https://www.stsforum.org/file/2022/11/STS-forum-2022-Summary.pdf",
    "https://www.stsforum.org/file/2023/11/STS2023_Summary.pdf"
]


data = process_pdfs(urls)

# Create a DataFrame and save it as a CSV
df = pd.DataFrame(data)
df.to_csv("test.csv", index=False)

print("CSV file saved as summaries.csv")

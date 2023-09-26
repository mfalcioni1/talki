import requests
import PyPDF2 as pdf
import os

def download_pdf(url, save_path):
    response = requests.get(url)
    
    # Ensure the response contains a PDF document
    if response.headers['content-type'] == 'application/pdf':
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"PDF downloaded and saved to {save_path}")
    else:
        print("Failed to download the PDF")

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = pdf.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

def save_text(text, save_path):
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Text saved to {save_path}")

def main():
    # Example usage
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', '-u', type=str, required=True)
    parser.add_argument('--save_path', '-p', type=str, default="paper")
    
    args = parser.parse_args()
    url = args.url
    save_path = args.save_path
    pdf_save_path = os.path.join(os.getcwd(), f"{save_path}.pdf")
    download_pdf(url, pdf_save_path)

    pdf_text = extract_text_from_pdf(f"{save_path}.pdf")
    text_save_path = os.path.join(os.getcwd(), f"{save_path}.txt")
    save_text(pdf_text, text_save_path)

if __name__ == "__main__":
    main()
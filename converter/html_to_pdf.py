import pdfkit

def convert_html_to_pdf(html_path: str, pdf_path: str) -> None:
    try:
        pdfkit.from_file(html_path, pdf_path)
    except Exception as e:
        print(f"❌ Failed to convert HTML to PDF: {e}")


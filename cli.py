import argparse
from converter.html_to_pdf import convert_html_to_pdf

def main():
    parser = argparse.ArgumentParser(description="Convert HTML to PDF")
    parser.add_argument("html_path", help="Path to the input HTML file")
    parser.add_argument("--output", help="Path to save output PDF")
    args = parser.parse_args()

    pdf_path = args.output or args.html_path.replace(".html", ".pdf")
    convert_html_to_pdf(args.html_path, pdf_path)
    print(f"✅ PDF saved to: {pdf_path}")

if __name__ == "__main__":
    main()

# HTML to PDF Converter

A simple command-line tool to convert HTML files to PDF using pdfkit and wkhtmltopdf.

## Install Dependencies
```bash
pip install -r requirements.txt
# Also install wkhtmltopdf: https://wkhtmltopdf.org/downloads.html
```

## Usage
```bash
python cli.py example.html
python cli.py example.html --output custom.pdf
```

## Notes
- Requires wkhtmltopdf to be installed and in your system path.

import argparse
from markdown_pdf import MarkdownPdf, Section

# Set up argument parser
parser = argparse.ArgumentParser(description='Convert a Markdown file to a PDF.')
parser.add_argument('-i', '--input', required=True, help='Input Markdown file')
parser.add_argument('-o', '--output', required=True, help='Output PDF file')

# Parse arguments
args = parser.parse_args()

# Create a MarkdownPdf object
pdf = MarkdownPdf(toc_level=5)

try:
    with open(args.input, "r") as file:
        content = file.read()

        css = "table, th, td {border: 1px solid black;}"
        # Add a section with Markdown content
        pdf.add_section(Section(content), user_css=css)

        # Save the PDF
        pdf.save(args.output)
        print(f"Successfully converted '{args.input}' to '{args.output}'")

except FileNotFoundError:
    print(f"Error: The file '{args.input}' was not found.")
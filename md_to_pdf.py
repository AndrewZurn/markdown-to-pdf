from markdown_pdf import MarkdownPdf, Section

# Create a MarkdownPdf object
pdf = MarkdownPdf(toc_level=5)

try:
    with open("summary.md", "r") as file:
        content = file.read()

        css = "table, th, td {border: 1px solid black;}"
        # Add a section with Markdown content
        pdf.add_section(Section(content), user_css=css)

        # Save the PDF
        pdf.save("output.pdf")
except FileNotFoundError:
    print("Error: The file 'example.txt' was not found.")

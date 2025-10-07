# Markdown to PDF Converter

A simple Python script to convert Markdown files to PDF using the `markdown_pdf` library.

## Description

This project provides a script (`md_to_pdf.py`) that takes a Markdown file as input and generates a PDF file.

## Setup and Usage

### 1. Python Virtual Environment with `pyenv`

It is recommended to use a virtual environment to manage the project's dependencies.

**Create a Virtual Environment:**

First, ensure you have a compatible Python version installed via `pyenv`. If not, you can install one (e.g., 3.11.0):

```bash
pyenv install 3.11.0
```

Then, create a virtual environment for this project:

```bash
pyenv virtualenv 3.11.0 md-to-pdf-env
```

**Activate the Virtual Environment:**

To activate the environment, run:

```bash
pyenv activate md-to-pdf-env
```

You should see the environment name (e.g., `(md-to-pdf-env)`) in your shell prompt.

To deactivate the environment when you are finished, simply run:

```bash
pyenv deactivate
```

### 2. Install Dependencies

With your virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Run the Script

To convert a Markdown file to PDF, use the `-i` flag for the input file and the `-o` flag for the output file.

**Example:**

```bash
python md_to_pdf.py -i summary.md -o output.pdf
```

This will convert `summary.md` to `output.pdf`.


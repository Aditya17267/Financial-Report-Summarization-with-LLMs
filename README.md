# Financial Report Summarization Project

This project is designed to extract and summarize financial data from PDF reports using a LangChain-based summarization approach. It involves extracting text from PDF files, processing the text, setting up a vector database, and generating summaries using a pre-trained language model.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Project Structure](#project-structure)
4. [Usage](#usage)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a machine running Windows, macOS, or Linux.
- You have installed Python 3.11 or later.
- You have installed `pip` (Python package installer).

## Installation

1. **Install Required Python Packages**

   Open a terminal and navigate to the project directory, then install the required packages using `pip`:

   ```sh
   pip install -r requirements.txt
   ```

2. **Set Up Environment Variables**

   Create a `.env` file in the root directory of the project and add your OpenAI API key:

   ```env
   OPENAI_API_KEY='your_openai_api_key'
   ```
    You can run the following command to setup the `.env` file
    ```sh
    echo "OPENAI_API_KEY='your_openai_api_key'" > .env
    ```
    
## Project Structure

Here's an overview of the project's structure:

```plaintext
financial-report-summarization/
│
├── utils/
│ ├── text_extraction/
│ │ ├── pdf_extraction.py
│ │ ├── file_operations.py
│ ├── openai/
│ │ ├── document_loader.py
│ │ ├── database_setup.py
│ │ ├── prompt_template.py
│ │ ├── text_processing.py
│ │ ├── text_splitting.py
│ ├── config/
│ │ ├── environment.py
│ │ ├── paths.py
│
├── requirements.txt
├── main.py
└── README.md
```

## Usage

Follow these steps to use the project:

1. **Prepare the PDF Files**

   Place all the PDF files you want to process in a directory.

2. **Run the Project**

   Execute the `main.py` script to start the process. The script will prompt you to enter the paths for the input PDF directory, extracted text storage file, output 2 page summary DOCX file and output 1 page summary DOCX file.

   ```sh
   python main.py
   ```

3. **Provide Required Paths**

   When prompted, provide the paths for:

   - Input PDF directory: Directory containing the PDF files.
   - Extracted text storage file: Path to the file where extracted text will be saved.
   - Output 2 page summary DOCX file: Path to the Word document where the two page summary will be stored.
   - Output 1 page summary DOCX file: Path to the Word document where the one page summary will be stored.

4. **Review the Output**

   The script will process the PDF files, extract and summarize the financial data, and save the summarized data to the specified DOCX file.

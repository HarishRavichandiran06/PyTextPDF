import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

def get_files_in_directory(dir_path):
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    return files

def select_input_file(files):
    if not files:
        print("No files found in the specified directory.")
        return None
    print("Available files:")
    for idx, file_name in enumerate(files, start=1):
        print(f"{idx}. {file_name}")
    file_idx = int(input("Enter the index of the input text file: ")) - 1
    return files[file_idx]

def text_to_pdf(input_file, output_dir, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        pdf_path = os.path.join(output_dir, output_file)
        pdf = SimpleDocTemplate(
            pdf_path,
            pagesize=letter,
            rightMargin=30,
            leftMargin=30,
            topMargin=30,
            bottomMargin=18
        )

        styles = getSampleStyleSheet()
        if 'Normal' not in styles:
            styles.add(styles['Normal'])

        elements = [Paragraph(line, styles["Normal"]) for line in lines]

        pdf.build(elements)
        print(f"PDF successfully created: {pdf_path}")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    dir_path = input("Enter the directory path where the input text file is stored: ")
    files = get_files_in_directory(dir_path)
    
    input_file = select_input_file(files)
    if input_file:
        output_dir = input("Enter the directory path where you want to save the output PDF file: ")
        output_file = input("Enter the name of the output PDF file (e.g., output.pdf): ")
        text_to_pdf(os.path.join(dir_path, input_file), output_dir, output_file)

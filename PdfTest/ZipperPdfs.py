from PyPDF2 import PdfReader, PdfWriter
from tkinter import Tk, filedialog


root = Tk()
root.withdraw()

# Pick PDFs
pdf1_path = filedialog.askopenfilename(
    title="Select FIRST PDF",
    filetypes=[("PDF files", "*.pdf")]
)
pdf2_path = filedialog.askopenfilename(
    title="Select SECOND PDF",
    filetypes=[("PDF files", "*.pdf")]
)

output_path = filedialog.asksaveasfilename(
    title="Save Interleave File",
    defaultextension=".pdf",
    filetypes=[("PDF files","*.pdf")]
)
# Cancel check
if not pdf1_path or not pdf2_path:
    print("File selection cancelled.")
    exit()

#print(pdf1_path)

pdf1 = PdfReader(pdf1_path)
pdf2 = PdfReader(pdf2_path)

reader1 = PdfReader(pdf1_path)
reader2 = PdfReader(pdf2_path)

writer = PdfWriter()

# Number of pages to zip (stops at the shorter PDF)
max_pages = min(len(reader1.pages), len(reader2.pages))

for i in range(max_pages):
    writer.add_page(reader1.pages[i])
    writer.add_page(reader2.pages[i])

# Optional: append remaining pages if PDFs are different lengths
if len(reader1.pages) > max_pages:
    for i in range(max_pages, len(reader1.pages)):
        writer.add_page(reader1.pages[i])

if len(reader2.pages) > max_pages:
    for i in range(max_pages, len(reader2.pages)):
        writer.add_page(reader2.pages[i])

with open(output_path, "wb") as f:
    writer.write(f)

print("Done! Created:", output_path)

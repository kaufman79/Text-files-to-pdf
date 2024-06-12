from fpdf import FPDF
from pathlib import Path
import glob

filepaths = glob.glob("files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    with open(filepath, 'r') as file:
        content = file.read()
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    name = Path(filepath).stem
    pdf.cell(w=50, h=12, txt=name.title(), align="L",
             ln=1, border=0)
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("output.pdf")

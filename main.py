from fpdf import FPDF
from pathlib import Path
import glob

filepaths = glob.glob("files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    name = Path(filepath).stem
    pdf.cell(w=50, h=12, txt=name.title(), align="L",
             ln=1, border=0)

pdf.output("output.pdf")

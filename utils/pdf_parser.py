import os
from fpdf import FPDF

def export_sop_to_pdf(content, filename="sop.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    pdf.output(filename)

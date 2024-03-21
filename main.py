from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    for i in range(row["Pages"]):
        pdf.add_page()
        pdf.set_font("Arial", size=14)
        if i == 0:
            pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
            pdf.line(10, 22, 200, 22)

pdf.output("output.pdf")
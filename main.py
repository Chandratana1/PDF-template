from tkinter.ttk import Style

from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation= "P", unit ="mm", format="A4")
pdf.set_auto_page_break(auto = False, margin=0)
df = pd.read_csv("topics.csv")


for index, row in df.iterrows():
        pdf.add_page()
        pdf.set_font(family= "Times", style="B", size = 24)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0, h=12, txt = row["Topic"], align = "L",
                 ln = 1, border =0)
        #pdf.line(10,21,200,21)

        for y in range(0, 298, 10):
            pdf.line(10, y, 200, y)

         #pdf.line(10, 21, 200, 21)

        #Set the footer
        pdf.ln(265)

        # Set the Footer for master Page
        pdf.set_font(family= "Times", style="I", size = 8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R",
                 ln=1, border=0)

        for i in range(row["Pages"]-1):
            pdf.add_page()
            pdf.ln(255)
            # Set the Footer for sub Pages
            pdf.set_font(family="Times", style="I", size=8)

            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=12, txt=row["Topic"], align="R",
                     ln=1, border=0)
           # for  i in range(278):
            # pdf.line(10, 278, 200, 278)
        for y in range(0, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")




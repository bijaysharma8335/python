from fpdf import FPDF
  
  
# save FPDF() class into a 
# variable pdf
pdf = FPDF()
print(pdf)
# Add a page
pdf.add_page()
   
# set style and size of font 
# that you want in the pdf
pdf.set_font("Arial", size = 15)
  
# create a cell
pdf.cell(200, 10, txt = "GeeksforGeeks", 
         ln = 1, align = 'C')
  
# add another cell

pdf.cell(200, 10, txt = "A Computer Science portal for geeks.",
         ln = 2, align = 'C')
pdf.cell(200, 10, txt = "B Computer Science portal for geeks.",
         ln = 3, align = 'C')
pdf.cell(200, 10, txt = "C Computer Science portal for dciceficgeeks.",
         ln = 4, align = 'C')
print(pdf) 
# save the pdf with name .pdf
pdf.output("samplepdf.pdf")   
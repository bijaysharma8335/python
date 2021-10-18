# from fpdf import FPDF
# class PDF(FPDF):
#      pass # nothing happens when it is executed.pdf=PDF(orientation='L') 
# # pdf=PDF(unit='mm') #unit of measurement
# pdf = PDF(format='A4') #page format. A4 is the default value of the format, you don't have to specify it.
# # full syntax
# PDF(orientation={'P' or 'L'}, measure{'mm','cm','pt','in'}, format{'A4','A3','A5','Letter','Legal')
# #default
# pdf = PDF(orientation='P', unit='mm', format='A4')
# pdf.add_page()
# pdf.output('test.pdf','F')


# import numpy as np
# import pandas as pd
# from fpdf import FPDF
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# from matplotlib.ticker import ScalarFormatter

# pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
# pdf.add_page()
# pdf.set_font('helvetica', 'bold', 10)
# pdf.set_text_color(255, 255, 255)
import math,cairo

width, height = 768,768
surface = cairo.PDFSurface ("circle.pdf", width, height)
ctx = cairo.Context (surface)
ctx.add_page()
ctx.set_source_rgb(1,1,1)
ctx.rectangle(0,0,width,height)
ctx.fill()
ctx.set_source_rgb(1,0,0)
ctx.move_to(width/2,height/2)
ctx.arc(width/2,height/2,512*0.25,0,math.pi*2)
ctx.fill()
# ctx.show_page()
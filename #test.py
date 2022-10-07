from mmap import PAGESIZE
from fpdf import FPDF

from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics
import Functions as func

from pdf import PDF
import PIL

list = ["Marea Sistemi" ,"Via Rossi 100,Volla,Napoli,80040" ,"Tel. 081 051 3214  -   P. IVA 08181461214" ,"www.mareasistemi.it  -   " + "amministrazione@mareasistemi.it"]
pdf = PDF("test1.pdf")
#print(pdf.getAvailableFonts())
path = "test1.png"
pdf.__headerFattura__(list ,'Courier-BoldOblique' ,20 ,"Times-Roman" ,10 ,path)


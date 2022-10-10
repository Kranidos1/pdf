from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PDFClass import PDF
import wx
from PersonalDialog import PersonalizedDialog
from Frame import MainFrame
width ,height = A4

#app = wx.App()
#mainFrame = MainFrame()
#mainFrame.Show()
fontsInfo = [(('Bauhaus 93', 'BAUHS93.TTF'), (255, 0, 0, 255), 24) ,(('Times New Roman', 'TIMES.TTF'), (0, 0, 0, 255), 14) ,(('Times New Roman', 'TIMES.TTF'),
                                                                                (0, 0, 0, 255), 32) ,(('Times New Roman', 'TIMES.TTF'), (0, 0, 0, 255), 14)]

pdf = PDF("test1.pdf")
pdf.__headerFattura__(["Qualcosa Titolo" ,"Via Rossi 100,Volla,Napoli,80040","Num Cell 3398210976 PIVA 848484","qualcosa.it - qualcosa@gmail.com"] ,"test6.png" ,"r" ,fontsInfo)
#personal = PersonalizedDialog()
#personal.ShowModal()
#app.MainLoop()




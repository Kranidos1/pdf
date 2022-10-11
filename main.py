from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PDFClass import PDF
import wx
from PersonalDialog import PersonalizedDialog
from Frame import MainFrame

width ,height = A4

app = wx.App()
mainFrame = MainFrame()
mainFrame.Show()
#diciamo che il max e' 27
#fontsInfo = [(('Bauhaus 93', 'BAUHS93.TTF'), (255, 0, 0, 255), 20) ,(('Times New Roman', 'TIMES.TTF'), (0, 0, 0, 255), 14) ,(('Times New Roman', 'TIMES.TTF'),
                                           #                                   (0, 0, 0, 255), 14) ,(('Times New Roman', 'TIMES.TTF'), (0, 0, 0, 255), 14)]

#pdf = PDF("test1.pdf")
#pdf.__headerFattura__(["Qualcosa fdsfdsfdsfdsTitolo" ,"Via Rossfdsfdsfdsfdsi 100,Vollfddsa,Napoli,80040","Num Cell 339821dfsdsfds0976 PIVA 848484","qualcosa.ifdfdsfsdfdssfdsfdsfdst - qualcosa@gmail.com"] ,"test6.png" ,"s" ,fontsInfo)
#personal = PersonalizedDialog()
#personal.ShowModal()
app.MainLoop()




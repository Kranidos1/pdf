from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
import wx
from FrameFolder.Frame import MainFrame
from PDFFolder.PDFClass import PDF
width ,height = A4
import os

app = wx.App()
mainFrame = MainFrame()
mainFrame.Show()
#diciamo che il max e' 27
#fontsInfo = [(('Bauhaus 93', 'BAUHS93.TTF'), (255, 0, 0, 255), 23) ,(('Times New Roman', 'TIMES.TTF'), (0, 0, 0, 255), 14) ,(('Times New Roman', 'TIMES.TTF'),
                              #                                               (0, 0, 0, 255), 22) ,(('Times New Roman', 'TIMES.TTF'), (0, 0, 0, 255), 28)]
#save_name = os.path.join(os.path.expanduser("~"), "Desktop/", "test1.pdf")
#pdf = PDF(save_name)
##pdf.__headerFattura__(["Qualcosa fdsfdsfdsfdsTitolo" ,"Via Rossfdsfdsfdsfdsi 100,Vollfddsa,Napoli,80040","Num Cell 339820976 PIVA 848484","qualcosa.ifdfdsfsdfdssfdsfdsfdst - qualcosa@gmail.com"] ,"test1.jpg" ,"s" ,fontsInfo)
#personal = PersonalizedDialog()
#personal.ShowModal()
app.MainLoop()







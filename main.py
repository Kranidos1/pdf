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

#personal = PersonalizedDialog()
#personal.ShowModal()
app.MainLoop()




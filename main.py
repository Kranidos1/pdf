from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
import wx
from FrameFolder.Frame import MainFrame
from PDFFolder.PDFClass import PDF
from FrameFolder.PersonalDialog import PersonalizedDialog
width ,height = A4
import os

app = wx.App()
mainFrame = MainFrame()
mainFrame.Show()
app.MainLoop()







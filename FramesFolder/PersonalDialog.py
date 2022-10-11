
import wx
import matplotlib.font_manager
import matplotlib.ft2font as ft2font

class PersonalizedDialog(wx.Dialog):
    
    def __init__(self ,info):
        
        #trick per permettere resizare un dialog
        super().__init__(parent = None ,title = "Scelta font" ,style = wx.RESIZE_BORDER | wx.DEFAULT_DIALOG_STYLE | wx.ID_OK)
        
        #(faceName ,path.ttf),rgb,pointsize di default
        self.info = list(info)
        
        self.Centre()
        self.SetMinSize((500,300))
        self.SetMaxSize((500,300))
        
        self.panel = wx.Panel(self)
        
        self.boxAll = wx.BoxSizer(wx.HORIZONTAL)
        
        self.boxFonts = wx.StaticBoxSizer(wx.VERTICAL ,self.panel ,label = "Fonts disponibili :")
        
        #listChoices = ["Courier" ,"Courier-Bold" ,"Courier-Bold Italic" ,"Courier-Italic" ,"Times" ,"Times-Bold" ,"Times-Bold Italic" 
                       #,"Times-Italic" ,"Bauhaus 93" ,"Arial" ,"Arial-Bold" ,"Arial-Bold Italic" ,"Arial-Italic" ,"Bernard" ,"Cooper" ,"Elephant" ,"Elephant-Italic"]
        
        self.listChoices = sorted(matplotlib.font_manager.get_font_names())
        self.listaFonts = wx.ListBox(self.panel ,choices = self.listChoices ,size = (250,250) ,style = wx.LB_SINGLE)
        self.boxFonts.Add(self.listaFonts ,proportion = 0 ,flag = wx.ALL ,border = 5)
        
        self.SetEscapeId(wx.ID_CLOSE)
        self.boxScelte = wx.BoxSizer(wx.VERTICAL)
        #da migliorare
        self.labelSample = wx.StaticText(self.panel ,label = "Esempio font" )
        
        #DEFAULT FONT
        font = wx.Font(12, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,
                      underline = False, faceName = "Courier", encoding = wx.FONTENCODING_DEFAULT)
        self.labelSample.SetFont(font)
        
        self.labelSize = wx.StaticText(self.panel ,label = "PointSize" )
        
        self.spin = wx.SpinCtrl(self.panel ,value = "14")
        self.spin.SetRange(10 ,32)
        self.spin.SetIncrement(1)
        
        self.buttonColore = wx.Button(self.panel ,label = "Scegli Colore")
        
        self.buttonScelto = wx.Button(self.panel ,wx.ID_OK ,label = "Scelto!" )
        
        self.boxScelte.Add(self.labelSample ,proportion = 0 ,flag =  wx.TOP | wx.BOTTOM,border = 25)
        self.boxScelte.Add(self.labelSize ,proportion = 0 ,flag = wx.BOTTOM  ,border = 0)
        self.boxScelte.Add(self.spin ,proportion = 0 ,flag = wx.LEFT | wx.BOTTOM  ,border = 10)
        self.boxScelte.Add(self.buttonColore ,proportion = 0 ,flag = wx.TOP | wx.BOTTOM ,border = 25)
        self.boxScelte.Add(self.buttonScelto ,proportion = 0 ,flag = wx.TOP ,border = 40)
        
        self.boxAll.Add(self.boxFonts ,proportion = 0 ,flag = wx.ALL ,border = 5)
        self.boxAll.Add(self.boxScelte ,proportion = 0 ,flag = wx.ALL ,border = 5)
        
        
        self.panel.SetSizerAndFit(self.boxAll)
        
        self.spin.Bind(wx.EVT_SPINCTRL ,self.raccogliSize)
        self.buttonColore.Bind(wx.EVT_BUTTON ,self.cambiaColore)
        self.listaFonts.Bind(wx.EVT_LISTBOX ,self.cambiaFont)
        
        self.Fit()
        
    def raccogliSize(self ,evt):
        
        self.info[2] = self.spin.GetValue()
        
        
    def cambiaColore(self ,evt):
        
        dialog = wx.ColourDialog(self)
                
        if dialog.ShowModal() == wx.ID_OK:
                    
        #prendi colore
            colore = dialog.GetColourData()
            self.info[1] = colore.GetColour()
            
     #font handling       
    def cambiaFont(self ,evt):
        
        try:
            posFont = self.listaFonts.GetSelection()
            faceName = self.listChoices[posFont]
            
            font = wx.Font(12, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,
                        underline = False, faceName = faceName, encoding = wx.FONTENCODING_DEFAULT)
            
            path = matplotlib.font_manager.findfont(faceName)
            self.labelSample.SetFont(font)
            self.info[0] = (faceName ,path)
            
        except ValueError:
            
            #font non viene modificato. Problema con i font con -
            dial = wx.MessageDialog(self.panel ,"Font non disponibile." , caption = "Font error.", style = wx.ICON_EXCLAMATION | wx.OK )
            dial.ShowModal()              
            
                
    def GetData(self):
        
        return tuple(self.info)

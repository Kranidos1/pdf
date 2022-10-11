
import wx
from PDFClass import PDF

class PersonalizedDialog(wx.Dialog):
    
    def __init__(self ,info):
        
        #trick per permettere resizare un dialog
        super().__init__(parent = None ,title = "PersonalizedDialog" ,style = wx.RESIZE_BORDER | wx.DEFAULT_DIALOG_STYLE | wx.ID_OK)
        
        #(faceName ,path.ttf),rgb,pointsize di default
        self.info = list(info)
        
        self.Centre()
        self.SetMinSize((500,300))
        self.SetMaxSize((500,300))
        
        self.panel = wx.Panel(self)
        
        self.boxAll = wx.BoxSizer(wx.HORIZONTAL)
        
        self.boxFonts = wx.StaticBoxSizer(wx.VERTICAL ,self.panel ,label = "Fonts disponibili :")
        
        listChoices = ["Courier" ,"Courier-Bold" ,"Courier-Bold Italic" ,"Courier-Italic" ,"Times" ,"Times-Bold" ,"Times-Bold Italic" 
                       ,"Times-Italic" ,"Bauhaus 93" ,"Arial" ,"Arial-Bold" ,"Arial-Bold Italic" ,"Arial-Italic" ,"Bernard" ,"Cooper" ,"Elephant" ,"Elephant-Italic"]
        
        self.listaFonts = wx.ListBox(self.panel ,choices = listChoices ,size = (250,250) ,style = wx.LB_SINGLE)
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
        
        posFont = self.listaFonts.GetSelection()
        
        if(posFont == 0 or posFont == 1 or posFont == 2 or posFont == 3):
            
            faceName = "Courier"
            font = wx.Font(12, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,
                    underline = False, faceName = faceName, encoding = wx.FONTENCODING_DEFAULT)
            #COUR.TTF
            if(posFont == 0):
                
                #Courier
                path = "COUR.TTF"
                self.labelSample.SetFont(font) 
                self.info[0] = (faceName ,path)
                              
            if(posFont == 1):
                
                #Courier-Bold COURBD.TTF
                path = "COURBD.TTF"
                
                self.info[0] = (faceName ,path)
                self.labelSample.SetFont(font.Bold())
            
            if(posFont == 2):
                
                #Courier-BoldItalic COURBI.TTF
                path = "COURBI.TTF"
                self.info[0] = (faceName ,path)
                self.labelSample.SetFont(font.Bold().Italic())
                
            if(posFont == 3):
                
                #Courier-BoldItalic COURI.TTF
                path = "COURI.TTF"
                self.info[0] = (faceName ,path)
                self.labelSample.SetFont(font.Italic())             
            
        if(posFont == 4 or posFont == 5 or posFont == 6 or posFont == 7):
            
            faceName = "Times New Roman"
            font = wx.Font(12, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,
                    underline = False, faceName = faceName, encoding = wx.FONTENCODING_DEFAULT) 
            
            if(posFont == 4):
                #Times New Roman TIMES.TTF
                path = "TIMES.TTF"
                self.info[0] = (faceName ,path)
                self.labelSample.SetFont(font)        
            
            if(posFont == 5):
                
                #Times New Roman-Bold TIMESBD.TTF
                path = "TIMESBD.TTF"
                self.info[0] = (faceName ,path)
                self.labelSample.SetFont(font.Bold())       
                             
            if(posFont == 6):
                
                #Times New Roman-BoldItalic TIMESBI.TTF
                path = "TIMESBI.TTF"
                self.info[0] = (faceName ,path)
                self.labelSample.SetFont(font.Bold().Italic())  
                             
            if(posFont == 7):
                
                #Times New Roman-Italic TIMESI.TTF
                path = "TIMESI.TTF"
                self.info[0] = (faceName ,path)
                self.labelSample.SetFont(font.Italic())   
                
        if(posFont == 8):
                
                #Bauhaus 93      BAUHS93.TTF
                faceName = "Bauhaus 93"
                font = wx.Font(12, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,
                    underline = False, faceName = faceName ,encoding = wx.FONTENCODING_DEFAULT)
                path = "BAUHS93.TTF"
                self.info[0] = (faceName ,path)
                self.labelSample.SetFont(font)
        
        if(posFont == 9 or posFont == 10 or posFont == 11 or posFont == 12):
            
                #Arial     ARIAL.TTF
                faceName = "Arial"
                font = wx.Font(12, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,
                    underline = False, faceName = faceName, encoding = wx.FONTENCODING_DEFAULT)  
                          
                if(posFont == 9):
                    
                    #Arial
                    path = "ARIAL.TTF"
                    self.info[0] = (faceName ,path)
                    self.labelSample.SetFont(font) 
                
                if(posFont == 10):
                    #Arial-Bold ARIALBD.TTF
                    path = "ARIALBD.TTF"
                    self.info[0] = (faceName ,path)
                    self.labelSample.SetFont(font.Bold())
                    
                if(posFont == 11):
                    
                    #Arial-BoldItalic ARIALBI.TTF
                    path = "ARIALBI.TTF"
                    self.info[0] = (faceName ,path)
                    self.labelSample.SetFont(font.Bold().Italic())
                    
                if(posFont == 12):
                    
                    #Arial-Italic ARIALI.TTF
                    path = "ARIALI.TTF"
                    self.info[0] = (faceName ,path)
                    self.labelSample.SetFont(font.Italic())
        
        if(posFont == 13):
            #Bernard Mt BERNHC.TTF
            faceName = "Bernard MT Condensed"
            font = wx.Font(12, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,
                    underline = False, faceName = faceName ,encoding = wx.FONTENCODING_DEFAULT)  

            path = "BERNHC.TTF"
            self.info[0] = (faceName ,path)
            self.labelSample.SetFont(font)   
        
        if(posFont == 14):
            #Cooper COOPBL.TTF
            faceName = "Cooper"
            font = wx.Font(12, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,
                    underline = False, faceName = faceName ,encoding = wx.FONTENCODING_DEFAULT)  

            path = "COOPBL.TTF"
            self.info[0] = (faceName ,path)
            self.labelSample.SetFont(font)        
            
        if(posFont == 15 or posFont == 16):
            #Elephant
            faceName = "Elephant"
            font = wx.Font(12, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,
                underline = False, faceName = faceName ,encoding = wx.FONTENCODING_DEFAULT)  
    
            if(posFont == 15):
                #Elephant ELEPHNT.TTF
                path = "ELEPHNT.TTF"
                self.info[0] = (faceName ,path)
                self.labelSample.SetFont(font)
                
            if(posFont == 16):
                #Elephant-Italic ELEPHNTI.TTF
                path = "ELEPHNTI.TTF"
                self.info[0] = (faceName ,path)
                self.labelSample.SetFont(font.Italic())
                
    def GetData(self):
        
        return tuple(self.info)
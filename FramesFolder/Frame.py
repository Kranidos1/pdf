from multiprocessing.sharedctypes import Value
import wx
from PDFFolder.PDFClass import PDF

from FramesFolder.PersonalDialog import PersonalizedDialog

class MainFrame(wx.Frame):
    
    
    def __init__(self):
        

        super().__init__(parent = None ,title = "HeaderCreator")
        
        #default fonts
        self.infoFonts = [(('Times New Roman', 'TIMES.TTF'), (0, 0, 0, 255), 24) ,(('Times New Roman', 'TIMES.TTF'), (0, 0, 0, 255), 14) ,(('Times New Roman', 'TIMES.TTF'),
                                                                                (0, 0, 0, 255), 14) ,(('Times New Roman', 'TIMES.TTF'), (0, 0, 0, 255), 14)]
        self.values = []
        self.path = None
        self.Centre()
        
        self.panel = wx.Panel(self)
        
        #TODO: gestisci eventi
        mainBox = wx.BoxSizer(wx.VERTICAL)
        
        #funzione che ritorna un box con label + field come formato
        #NOMEAZIENDA
        boxNomeAzienda = wx.BoxSizer(wx.HORIZONTAL)
    
        self.fieldNomeAzienda = wx.TextCtrl(parent = self.panel ,size = (250,25))
        labelFormat = wx.StaticText(parent = self.panel ,label = ("Nome Azienda :"))
        
        boxNomeAzienda.Add(labelFormat ,proportion = 0 ,flag = wx.ALL ,border = 3)
        boxNomeAzienda.Add(self.fieldNomeAzienda ,proportion = 0 ,flag = wx.ALL ,border = 2)
        
        self.checkFontNomeAzienda = wx.CheckBox(self.panel, label = "Scelta Font")
        boxNomeAzienda.Add(self.checkFontNomeAzienda ,proportion = 0 ,flag = wx.ALL ,border = 5)
        
        self.checkFontNomeAzienda.Bind(wx.EVT_CHECKBOX, self.cambiaFont)
        
        #Bottoni brutti
        #pulsante = wx.Button(panel, label="Scegli Font" ,size = (100,25))
        #boxNomeAzienda.Add(pulsante ,proportion = 0 ,flag = wx.ALL ,border = 5)
        
        #INDIRIZZO
        boxIndirizzo =  wx.BoxSizer(wx.HORIZONTAL)
    
        self.fieldIndirizzo = wx.TextCtrl(parent = self.panel ,size = (250,25))
        labelFormat = wx.StaticText(parent = self.panel ,label = ("Indirizzo :"))
        
        boxIndirizzo.Add(labelFormat ,proportion = 0 ,flag = wx.ALL ,border = 3)
        boxIndirizzo.Add(self.fieldIndirizzo ,proportion = 0 ,flag = wx.ALL ,border = 2) 
        
        self.checkFontIndirizzo= wx.CheckBox(self.panel, label="Scelta Font")
        boxIndirizzo.Add(self.checkFontIndirizzo ,proportion = 0 ,flag = wx.ALL ,border = 5)
        
        self.checkFontIndirizzo.Bind(wx.EVT_CHECKBOX, self.cambiaFont)   
        #NUM TELEFONO
        boxNumTelefono = wx.BoxSizer(wx.HORIZONTAL)
    
        self.fieldNumTelefono = wx.TextCtrl(parent = self.panel ,size = (250,25))
        labelFormat = wx.StaticText(parent = self.panel ,label = ("Telefono :"))
        
        boxNumTelefono.Add(labelFormat ,proportion = 0 ,flag = wx.ALL ,border = 3)
        boxNumTelefono.Add(self.fieldNumTelefono ,proportion = 0 ,flag = wx.ALL ,border = 2)
        
        #PARTITA IVA
        boxPIVA = wx.BoxSizer(wx.HORIZONTAL)
    
        self.fieldPIVA = wx.TextCtrl(parent = self.panel ,size = (250,25))
        labelFormat = wx.StaticText(parent = self.panel ,label = ("P. IVA :"))
        
        boxPIVA.Add(labelFormat ,proportion = 0 ,flag = wx.ALL ,border = 3)
        boxPIVA.Add(self.fieldPIVA ,proportion = 0 ,flag = wx.ALL ,border = 2)
        
        boxNumTelefonoPIVA = wx.BoxSizer(wx.HORIZONTAL)
        boxNumTelefonoPIVA.Add(boxNumTelefono ,proportion = 0 ,flag = wx.ALL  ,border = 5)
        boxNumTelefonoPIVA.Add(boxPIVA ,proportion = 0 ,flag = wx.ALL  ,border = 5)      
        
        self.checkFontNumTelefonoPIVA = wx.CheckBox(self.panel, label = "Scelta Font")
        boxNumTelefonoPIVA.Add(self.checkFontNumTelefonoPIVA ,proportion = 0 ,flag = wx.ALL ,border = 5)
        
        self.checkFontNumTelefonoPIVA.Bind(wx.EVT_CHECKBOX, self.cambiaFont)
             
        #SITO
        boxSito = wx.BoxSizer(wx.HORIZONTAL)
    
        self.fieldSito = wx.TextCtrl(parent = self.panel ,size = (250,25))
        labelFormat = wx.StaticText(parent = self.panel ,label = ("Sito :"))
        
        boxSito.Add(labelFormat ,proportion = 0 ,flag = wx.ALL ,border = 3)
        boxSito.Add(self.fieldSito ,proportion = 0 ,flag = wx.ALL ,border = 2)
        
        #EMAIL
        boxEmail = wx.BoxSizer(wx.HORIZONTAL)
    
        self.fieldEmail = wx.TextCtrl(parent = self.panel ,size = (250,25))
        labelFormat = wx.StaticText(parent = self.panel ,label = ("Email :"))
        
        boxEmail.Add(labelFormat ,proportion = 0 ,flag = wx.ALL ,border = 3)
        boxEmail.Add(self.fieldEmail ,proportion = 0 ,flag = wx.ALL ,border = 2)
        
        boxSitoEmail = wx.BoxSizer(wx.HORIZONTAL)
        boxSitoEmail.Add(boxSito ,proportion = 0 ,flag = wx.ALL  ,border = 5)
        boxSitoEmail.Add(boxEmail ,proportion = 0 ,flag = wx.ALL  ,border = 5)             
        
        self.checkFontSitoEmail = wx.CheckBox(self.panel, label = "Scelta Font")
        boxSitoEmail.Add(self.checkFontSitoEmail ,proportion = 0 ,flag = wx.ALL ,border = 5)
        
        self.checkFontSitoEmail.Bind(wx.EVT_CHECKBOX, self.cambiaFont)       
        
        #Box cose immagine
        boxImmagine = wx.StaticBoxSizer(wx.VERTICAL ,self.panel ,"Settings immagine :")
        
        labelLato = wx.StaticText(self.panel ,label = "Lato immagine :")
        self.listaScelte = wx.ListBox(self.panel ,choices = ["r","s"] ,size=(25,50) ,style = wx.LB_SINGLE)
        
        bottoneSceltaImmagine = wx.Button(self.panel ,label = "Scegli immagine" ,size = (100,30))
        bottoneSceltaImmagine.Bind(wx.EVT_BUTTON ,self.sceltaImmagine)
        
        boxSceltaLato = wx.BoxSizer(wx.HORIZONTAL)
        boxSceltaLato.Add(labelLato ,proportion = 0 ,flag = wx.ALL ,border = 3)
        boxSceltaLato.Add(self.listaScelte ,proportion = 0 ,flag = wx.ALL ,border = 2)
        
        boxImmagine.Add(boxSceltaLato ,proportion = 0 ,flag = wx.ALL ,border = 5)
        boxImmagine.Add(bottoneSceltaImmagine ,proportion = 0 ,flag = wx.ALL ,border = 5)
        
        #boxImmagine + bottone
        boxSettingsEInserimento = wx.BoxSizer(wx.HORIZONTAL)
        
        boxSettingsEInserimento.Add(boxImmagine ,proportion = 0 ,flag = wx.ALL | wx.EXPAND ,border = 5)
        
        self.bottoneInserimento = wx.Button(self.panel ,label = "Crea PDF" ,size = (100,30)) 
        labelFantasma = wx.StaticText(self.panel ,label = "                                                            ")
        boxSettingsEInserimento.Add(labelFantasma ,proportion = 0 ,flag = wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        boxSettingsEInserimento.Add(self.bottoneInserimento ,proportion = 0 ,flag = wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        
        self.bottoneInserimento.Bind(wx.EVT_BUTTON ,self.crea)
        
        mainBox.Add(boxNomeAzienda ,proportion = 0 ,flag = wx.ALL | wx.EXPAND ,border = 5)
        mainBox.Add(boxIndirizzo ,proportion = 0 ,flag = wx.ALL | wx.EXPAND  ,border = 5)       
        mainBox.Add(boxNumTelefonoPIVA ,proportion = 0 ,flag = wx.ALL | wx.EXPAND ,border = 5)
        mainBox.Add(boxSitoEmail ,proportion = 0 ,flag = wx.ALL | wx.EXPAND ,border = 5)
        mainBox.Add(boxSettingsEInserimento ,proportion = 0 ,flag = wx.ALL ,border = 5)
        
        self.panel.SetSizerAndFit(mainBox)
        self.Fit()
        
        self.SetSize((748, 355))
        self.SetMinSize((748, 355))
        self.SetMaxSize((748, 355))    
                
    def cambiaFont(self ,evt):
             #non appare mai la V
            if evt.Id == self.checkFontNomeAzienda.Id :

                obj = self.checkFontNomeAzienda
                indice = 0
            
            if evt.Id == self.checkFontIndirizzo.Id :

                obj = self.checkFontNomeAzienda
                indice = 1
            
            if evt.Id == self.checkFontNumTelefonoPIVA.Id :

                obj = self.checkFontNumTelefonoPIVA
                indice = 2
            
            if evt.Id == self.checkFontSitoEmail.Id :

                obj = self.checkFontSitoEmail
                indice = 3
                
            obj.Set3StateValue(False)
            #dialogo scelta font
            dialog = PersonalizedDialog(self.infoFonts[indice])
            dialog.ShowModal()
            #prendi font
            info = dialog.GetData()
            dialog.Destroy()
                
            self.infoFonts[indice] = tuple(info)

                    
    def sceltaImmagine(self ,evt):
        
        dlg = wx.FileDialog(None, "Scegli immagine", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST ,wildcard = ".jpg (*.jpg)|*.jpg|.JPEG (*.JPEG)|*.JPEG")
        if dlg.ShowModal() == wx.ID_CANCEL:
            
            dial = wx.MessageDialog(self.panel ,"Non hai scelto nessuna immagine." , caption = "No image selected.", style = wx.ICON_EXCLAMATION | wx.OK )
            dial.ShowModal()
            
        else:
            
            self.path = str(dlg.GetPath())
            
    def crea(self ,evt):
        
        nomeAzienda = self.fieldNomeAzienda.GetValue()
        if(nomeAzienda != ""):
            
            self.values.append(nomeAzienda)
            indirizzo = self.fieldIndirizzo.GetValue()
            
            
            if(indirizzo != ""):
                
                self.values.append(indirizzo)
                telefono = self.fieldNumTelefono.GetValue()

                #controllo su tel se vuoto
                if(telefono != "") :

                    tel = "Tel :" + telefono + "  -  "

                else :

                    tel = ""

                iva = self.fieldPIVA.GetValue()
                #altrimenti nulla
                    
                if(iva != ""):
                        
                        self.values.append(tel + "P. IVA : " + iva)

                        #prendo email e sito
                        email = self.fieldEmail.GetValue()
                        sito = self.fieldSito.GetValue()

                        if(email != "" and sito != "") :

                            self.values.append("Email : " + email + " Sito :" + sito)  

                        elif(email != "" and sito == "") :
                            
                            self.values.append("Email : " + email)  

                        elif(email == "" and sito != "") :

                            self.values.append("Sito: " + sito)

                        else :

                            self.values.append("")
                                
                    #gestione nessuna scelta fissando come flagside s di default
                        try:
                                    
                            flagSide = self.listaScelte.GetString(self.listaScelte.GetSelection())
                                    
                        except wx._core.wxAssertionError:
                            #default
                            flagSide = "s"
                                    
                        if(self.path != None):
                                    
                            #self.infoFonts
                            dlg = wx.FileDialog(self.panel ,"Scegli titolo e cartella del pdf." ,"" ,"" ,"PDF files|.pdf" ,wx.FD_SAVE)

                            if dlg.ShowModal() == wx.ID_OK:
                                                                            
                                pathPDF = dlg.GetPath()
                                pdf = PDF(pathPDF)
                                pdf.__headerFattura__(self.values ,self.path ,flagSide ,self.infoFonts)
                                        
                                dial = wx.MessageDialog(self.panel ,"PDF creato nella cartella selezionata." , caption = "Successo!.", style = wx.ICON_INFORMATION | wx.OK )
                                dial.ShowModal()

                                self.Close()
                                        
                            else:

                                dial = wx.MessageDialog(self.panel ,"Non hai scelto nessun titolo/cartella." , caption = "Cartella non selezionata.", style = wx.ICON_EXCLAMATION | wx.OK )
                                dial.ShowModal()
                                
                        else:
                                    
                            dial = wx.MessageDialog(self.panel ,"Non hai scelto nessuna immagine." , caption = "Immagine non selezionata.", style = wx.ICON_EXCLAMATION | wx.OK )
                            dial.ShowModal()
                       
                else:
                    dial = wx.MessageDialog(self.panel ,"Inserire la P. IVA." , caption = "Field vuoto.", style = wx.ICON_EXCLAMATION | wx.OK )
                    dial.ShowModal()
            else:
                dial = wx.MessageDialog(self.panel ,"Inserire l'indirizzo." , caption = "Field vuoto.", style = wx.ICON_EXCLAMATION | wx.OK )
                dial.ShowModal()  
                              
        else:
            dial = wx.MessageDialog(self.panel ,"Inserire il nome dell'Azienda." , caption = "Field vuoto.", style = wx.ICON_EXCLAMATION | wx.OK )
            dial.ShowModal()   
            
 
               

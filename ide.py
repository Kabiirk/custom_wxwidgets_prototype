# import wx
# import wx.stc as stc

# class XmlSTC(stc.StyledTextCtrl):

#     def __init__(self, parent):
#         stc.StyledTextCtrl.__init__(self, parent)

#         self.SetLexer(stc.STC_LEX_PYTHON)
#         self.StyleSetSpec(stc.STC_STYLE_DEFAULT,
#                           "size:10,face:Courier New")
#         faces = { 'mono' : 'Courier New',
#                   'helv' : 'Arial',
#                   'size' : 10,
#                   }

#         self.SetMarginType(0, wx.stc.STC_MARGIN_NUMBER)
#         # XML styles
#         # Default
#         self.StyleSetSpec(stc.STC_H_DEFAULT, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)

#         # Number
#         self.StyleSetSpec(stc.STC_H_NUMBER, "fore:#007F7F,size:%(size)d" % faces)
#         # Tag
#         self.StyleSetSpec(stc.STC_H_TAG, "fore:#007F7F,bold,size:%(size)d" % faces)
#         # Value
#         self.StyleSetSpec(stc.STC_H_VALUE, "fore:#7F0000,size:%(size)d" % faces)

#         # Python styles
#         self.StyleSetSpec(wx.stc.STC_P_DEFAULT, 'fore:#000000')
#         # Comments
#         self.StyleSetSpec(wx.stc.STC_P_COMMENTLINE,  'fore:#008000,back:#F0FFF0')
#         self.StyleSetSpec(wx.stc.STC_P_COMMENTBLOCK, 'fore:#008000,back:#F0FFF0')
#         # Numbers
#         self.StyleSetSpec(wx.stc.STC_P_NUMBER, 'fore:#008080')
#         # Strings and characters
#         self.StyleSetSpec(wx.stc.STC_P_STRING, 'fore:#800080')
#         self.StyleSetSpec(wx.stc.STC_P_CHARACTER, 'fore:#800080')
#         # Keywords
#         self.StyleSetSpec(wx.stc.STC_P_WORD, 'fore:#000080,bold')
#         # Triple quotes
#         self.StyleSetSpec(wx.stc.STC_P_TRIPLE, 'fore:#800080,back:#FFFFEA')
#         self.StyleSetSpec(wx.stc.STC_P_TRIPLEDOUBLE, 'fore:#800080,back:#FFFFEA')
#         # Class names
#         self.StyleSetSpec(wx.stc.STC_P_CLASSNAME, 'fore:#0000FF,bold')
#         # Function names
#         self.StyleSetSpec(wx.stc.STC_P_DEFNAME, 'fore:#008080,bold')
#         # Operators
#         self.StyleSetSpec(wx.stc.STC_P_OPERATOR, 'fore:#800000,bold')
#         # Identifiers. I leave this as not bold because everything seems
#         # to be an identifier if it doesn't match the above criterae
#         self.StyleSetSpec(wx.stc.STC_P_IDENTIFIER, 'fore:#000000')
        

#         # Caret color
#         self.SetCaretForeground("BLUE")
#         # Selection background
#         self.SetSelBackground(1, '#66CCFF')

#         with open('test.py') as fobj:
#             text = fobj.read()

#         self.SetText(text)


# class XmlPanel(wx.Panel):

#     def __init__(self, parent):
#         wx.Panel.__init__(self, parent)

#         self.xml_view = XmlSTC(self)

#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(self.xml_view, 1, wx.EXPAND)
#         self.SetSizer(sizer)

# class XmlFrame(wx.Frame):

#     def __init__(self):
#         wx.Frame.__init__(self, None, title='Script View')
#         panel = XmlPanel(self)
#         self.Show()

# if __name__ == '__main__':
#     app = wx.App(False)
#     frame = XmlFrame()
#     app.MainLoop()

# sample_one.py


# REF : https://wiki.wxpython.org/How%20to%20create%20a%20simple%20text%20editor%20%28Phoenix%29
import sys
import os.path
import wx
from wx.core import Icon
import wx.stc as stc

# class MyFrame
# class MyApp

keywords = 'False class from  or None continue global pass True def if raise and del import return as elif in try assert else is while async except lambda with await finally nonlocal yield break for not'

class PySTC(stc.StyledTextCtrl):

    def __init__(self, parent):
        stc.StyledTextCtrl.__init__(self, parent)

        self.SetLexer(stc.STC_LEX_PYTHON)
        self.StyleSetSpec(stc.STC_STYLE_DEFAULT,
                          "size:10,face:Courier New")
        faces = { 'mono' : 'Courier New',
                  'helv' : 'Arial',
                  'size' : 10,
                  }

        # Allow Margin to show line Numbers
        self.SetMarginType(1, wx.stc.STC_MARGIN_NUMBER)
        # Change width of margin
        self.SetMarginWidth(1, 35)
        # Line numbers in margin colours
        # ref : https://stackoverflow.com/questions/61461839/how-to-change-the-background-of-a-wxpython-styledtextctrl-margin
        self.StyleSetSpec(wx.stc.STC_STYLE_LINENUMBER,'fore:#F2F2F2,back:#46464E')
        # Indentation guides
        self.SetIndentationGuides(1)
        # Width of Tab = 4 spaces
        self.SetTabWidth(4)
        #Highlighting Specific Keywords (Pyhton only for now)
        self.SetKeyWords(0, keyWords=keywords)



        # # XML styles
        # # Default
        # self.StyleSetSpec(stc.STC_H_DEFAULT, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)

        # # Number
        # self.StyleSetSpec(stc.STC_H_NUMBER, "fore:#007F7F,size:%(size)d" % faces)
        # # Tag
        # self.StyleSetSpec(stc.STC_H_TAG, "fore:#007F7F,bold,size:%(size)d" % faces)
        # # Value
        # self.StyleSetSpec(stc.STC_H_VALUE, "fore:#7F0000,size:%(size)d" % faces)

        # Python styles
        self.StyleSetSpec(wx.stc.STC_P_DEFAULT, 'fore:#000000')
        # Comments
        self.StyleSetSpec(wx.stc.STC_P_COMMENTLINE,  'fore:#008000,back:#F0FFF0')
        self.StyleSetSpec(wx.stc.STC_P_COMMENTBLOCK, 'fore:#008000,back:#F0FFF0')
        # Numbers
        self.StyleSetSpec(wx.stc.STC_P_NUMBER, 'fore:#008080')
        # Strings and characters
        self.StyleSetSpec(wx.stc.STC_P_STRING, 'fore:#800080')
        self.StyleSetSpec(wx.stc.STC_P_CHARACTER, 'fore:#800080')
        # Keywords
        self.StyleSetSpec(wx.stc.STC_P_WORD, 'fore:#000080,bold')
        # Triple quotes
        self.StyleSetSpec(wx.stc.STC_P_TRIPLE, 'fore:#800080,back:#FFFFEA')
        self.StyleSetSpec(wx.stc.STC_P_TRIPLEDOUBLE, 'fore:#800080,back:#FFFFEA')
        # Class names
        self.StyleSetSpec(wx.stc.STC_P_CLASSNAME, 'fore:#0000FF,bold')
        # Function names
        self.StyleSetSpec(wx.stc.STC_P_DEFNAME, 'fore:#008080,bold')
        # Operators
        self.StyleSetSpec(wx.stc.STC_P_OPERATOR, 'fore:#800000,bold')
        # Identifiers. I leave this as not bold because everything seems
        # to be an identifier if it doesn't match the above criterae
        self.StyleSetSpec(wx.stc.STC_P_IDENTIFIER, 'fore:#000000')
        

        # Caret color
        self.SetCaretForeground("BLUE")
        # Selection background
        self.SetSelBackground(1, '#66CCFF')

        # with open('test.py') as fobj:
        #     text = fobj.read()

        # self.SetText(text)

#-------------------------------------------------------------------------------

# This is how you pre-establish a file filter so that the
# dialog only shows the extension(s) you want it to.

wildcard = "Text (*.txt)|*.txt|"        \
           "Executable (*.exe)|*.exe|"  \
           "Library (*.dll)|*.dll|"     \
           "Driver (*.sys)|*.sys|"      \
           "ActiveX (*.ocx)|*.ocx|"     \
           "Python (*.py)|*.py|"        \
           "Python (*.pyw)|*.pyw|"      \
           "All (*.*)|*.*"

#-------------------------------------------------------------------------------

class MyFrame(wx.Frame):
    def __init__(self, filename="Editor"):
        super(MyFrame, self).__init__(None)
        locale = wx.Locale(wx.LANGUAGE_ENGLISH)

        #------------

        # Return icons folder.

        #------------

        self.filename = filename
        self.dirname  = "."

        #------------

        # Simplified init method.
        self.CreateInteriorWindowComponents()
        self.CreateExteriorWindowComponents()

        #------------

        self.CenterOnScreen()

    #---------------------------------------------------------------------------

    def SetTitle(self):
        # MyFrame.SetTitle overrides wx.Frame.SetTitle,
        # so we have to call it using super :
        super(MyFrame, self).SetTitle("%s" % self.filename)


    def CreateInteriorWindowComponents(self):
        """
        Create "interior" window components. In this case
        it is just a simple multiline text control.
        """
        # self.control = wx.TextCtrl(self, -1, value="", style=wx.TE_MULTILINE)
        self.control = PySTC(self)


    def CreateExteriorWindowComponents(self):
        """
        Create "exterior" window components, such as menu and status bar.
        """

        # Simplified init method.
        self.SetTitle()

        #------------

        #------------

        self.CreateMenu()
        self.CreateToolBar()
        self.CreateStatusBar()
        self.BindEvents()


    def CreateMenu(self):
        """
        Create menu and menu bar.
        """

        menuBar = wx.MenuBar()
        #------------

        fileMenu = wx.Menu()

        for id, label, helpText, handler in \
            [(wx.ID_ABOUT, "&About",
              "Information about this program.", self.OnAbout),
             (None, None, None, None),
             (wx.ID_OPEN, "&Open",
              "Open a new file.", self.OnOpen),
             (wx.ID_SAVE, "&Save",
              "Save the current file.", self.OnSave),
             (wx.ID_SAVEAS, "Save &as",
              "Save the file under a different name.", self.OnSaveAs),
             (None, None, None, None),
             (wx.ID_EXIT, "E&xit",
              "Terminate the program.", self.OnCloseMe)]:

            if id == None:
                fileMenu.AppendSeparator()
            else:
                item = fileMenu.Append(id, label, helpText)

                #------------

                # Bind some events to an events handler.
                self.Bind(wx.EVT_MENU, handler, item)

        #------------

        # Add the fileMenu to the menuBar.
        menuBar.Append(fileMenu, "&File")

        #------------

        # Add the menuBar to the frame.
        self.SetMenuBar(menuBar)

    def CreateToolBar(self):
        tb = wx.ToolBar(self, style=wx.TB_TEXT|wx.HORIZONTAL)
        tb.SetToolBitmapSize((10, 10))

        tb.AddTool(1, u'Open', wx.Bitmap( r"icons\open.png"))
        tb.AddTool(2, u'Save', wx.Bitmap( r"icons\save.png"))
        tb.AddTool(3, u'Save As', wx.Bitmap( r"icons\save-as.png"))
        tb.AddTool(4, u'Exit', wx.Bitmap( r"icons\exit.png"))
        tb.AddTool(5, u'Run', wx.Bitmap( r"icons\run.png"))
        tb.Realize()

        tb.Bind(wx.EVT_TOOL, self.OnOpen, id=1)
        tb.Bind(wx.EVT_TOOL, self.OnSave, id=2)
        tb.Bind(wx.EVT_TOOL, self.OnSaveAs, id=3)
        tb.Bind(wx.EVT_TOOL, self.OnCloseMe, id=4)
        tb.Bind(wx.EVT_TOOL, self.OnRun, id=5)

   

  
        self.SetToolBar(tb)

    def BindEvents(self):
        """
        ...
        """

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)


    def DefaultFileDialogOptions(self):
        """
        Return a dictionary with file dialog options that can be
        used in both the save file dialog as well as in the open
        file dialog.
        """

        return dict(message="Choose a file :",
                    defaultDir=self.dirname,
                    wildcard=wildcard)


    def AskUserForFilename(self, **dialogOptions):
        """
        ...
        """

        dialog = wx.FileDialog(self, **dialogOptions)

        if dialog.ShowModal() == wx.ID_OK:
            userProvidedFilename = True
            self.filename = dialog.GetFilename()
            self.dirname = dialog.GetDirectory()
            # Update the window title with the new filename.
            self.SetTitle()
        else:
            userProvidedFilename = False

        dialog.Destroy()

        return userProvidedFilename


    def OnOpen(self, event):
        """
        Open file.
        """

        if self.AskUserForFilename(style=wx.FD_OPEN,
                                   **self.DefaultFileDialogOptions()):
            file = open(os.path.join(self.dirname, self.filename), 'r', encoding='utf-8')
            self.control.SetValue(file.read())
            file.close()

    def OnRun(self, event):
        print("Executing file @ : " + os.path.join(self.dirname, self.filename))

    def OnSave(self, event):
        """
        Save file.
        """

        with open(os.path.join(self.dirname, self.filename), 'w', encoding='utf-8') as file:
            file.write(self.control.GetValue())


    def OnSaveAs(self, event):
        """
        Save file as.
        """

        if self.AskUserForFilename(defaultFile=self.filename, style=wx.FD_SAVE,
                                   **self.DefaultFileDialogOptions()):
            self.OnSave(event)


    def OnAbout(self, event):
        """
        About dialog.
        """

        dialog = wx.MessageDialog(self,
                                  "A sample editor in wxPython.",
                                  "About sample editor",
                                  wx.OK)
        dialog.ShowModal()
        dialog.Destroy()


    def OnCloseMe(self, event):
        """
        Close the main window.
        """

        self.Close(True)


    def OnCloseWindow(self, event):
        """
        Quit and destroy application.
        """

        self.Destroy()

#-------------------------------------------------------------------------------

class MyApp(wx.App):
    """
    ....
    """
    def OnInit(self):

        #------------

        self.installDir = os.path.split(os.path.abspath(sys.argv[0]))[0]

        #------------

        frame = MyFrame()
        self.SetTopWindow(frame)
        frame.Show(True)

        return True

    #---------------------------------------------------------------------------

    def GetInstallDir(self):
        """
        Returns the installation directory for my application.
        """

        return self.installDir


    def GetIconsDir(self):
        """
        Returns the icons directory for my application.
        """

        icons_dir = os.path.join(self.installDir, "icons")
        return icons_dir

#-------------------------------------------------------------------------------

def main():
    app = MyApp(False)
    app.MainLoop()

#-------------------------------------------------------------------------------

if __name__ == "__main__" :
    main()
import wx
import wx.stc as stc

class XmlSTC(stc.StyledTextCtrl):

    def __init__(self, parent):
        stc.StyledTextCtrl.__init__(self, parent)

        self.SetLexer(stc.STC_LEX_PYTHON)
        self.StyleSetSpec(stc.STC_STYLE_DEFAULT,
                          "size:10,face:Courier New")
        faces = { 'mono' : 'Courier New',
                  'helv' : 'Arial',
                  'size' : 10,
                  }

        self.SetMarginType(0, wx.stc.STC_MARGIN_NUMBER)
        # XML styles
        # Default
        self.StyleSetSpec(stc.STC_H_DEFAULT, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)

        # Number
        self.StyleSetSpec(stc.STC_H_NUMBER, "fore:#007F7F,size:%(size)d" % faces)
        # Tag
        self.StyleSetSpec(stc.STC_H_TAG, "fore:#007F7F,bold,size:%(size)d" % faces)
        # Value
        self.StyleSetSpec(stc.STC_H_VALUE, "fore:#7F0000,size:%(size)d" % faces)

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

        with open('test.py') as fobj:
            text = fobj.read()

        self.SetText(text)


class XmlPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.xml_view = XmlSTC(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.xml_view, 1, wx.EXPAND)
        self.SetSizer(sizer)

class XmlFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Script View')
        panel = XmlPanel(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App(False)
    frame = XmlFrame()
    app.MainLoop()
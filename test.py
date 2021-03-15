# REF :
# https://docs.wxwidgets.org/3.0/overview_customwidgets.html
# http://infinity77.net/pycon/tutorial/pybr/wxpython.html -> a good primer for wxpython and Sizers
# https://www.blog.pythonlibrary.org/2012/05/05/wxpython-adding-and-removing-widgets-dynamically/ -> Add widgets on the click of a button
# https://stackoverflow.com/questions/6745463/exit-frame-and-panel-from-panel-method -> Close parent frame from a button in the panel
# https://www.programcreek.com/python/example/4469/wx.ComboBox a good wesite for examples
# https://zetcode.com/gui/wxwidgets/widgetsII/ -> for listboxes
# https://www.programcreek.com/python/example/97212/wx.ColourDialog -> Examples of colorpickerctrl 
import wx


template = [['A','B','C'], ['D','E'], ['F'], ['G','H']]

class MyPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.number_of_buttons = 0
        self.templates = [['A','B','C'], ['D','E'], ['F'], ['G','H']]
        
        self.frame = parent
        
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        widgetSizer = wx.BoxSizer(wx.VERTICAL)
        bottomSizer = wx.BoxSizer(wx.HORIZONTAL)

        # WIDGETSIZER
        for i in range(0,len(self.templates)):
            static_text = wx.StaticText(self, -1, style = wx.ALIGN_LEFT)
            static_text.SetLabel("Plot"+str(i+1))
            widgetSizer.Add(static_text, 0, wx.CENTER|wx.ALL, 5)
            
            for j in range(0,len(self.templates[i])):
                hsizer = wx.BoxSizer(wx.HORIZONTAL)
                color_picker = wx.ColourPickerCtrl(self, id=wx.ID_ANY, colour=wx.BLACK, style=wx.CLRP_DEFAULT_STYLE, validator=wx.DefaultValidator, name=self.templates[i][j])
                static_text = wx.StaticText(self, -1, style = wx.ALIGN_LEFT)
                static_text.SetLabel("Color of "+self.templates[i][j])
                hsizer.Add(static_text, 0, wx.EXPAND | wx.RIGHT, 5)
                hsizer.Add(color_picker, 0, wx.EXPAND | wx.LEFT, 5)

                widgetSizer.Add(hsizer, flag=wx.ALL|wx.ALIGN_CENTER, border=5)
        # BOTTOM SIZER
        closeBtn = wx.Button(self, label="Cancel")
        closeBtn.Bind(wx.EVT_BUTTON, self.onClose)
        bottomSizer.Add(closeBtn,  0, wx.CENTER|wx.ALL, 5)

        self.plotBtn = wx.Button(self, label="Plot")
        self.plotBtn.Bind(wx.EVT_BUTTON, self.onPlot)
        bottomSizer.Add(self.plotBtn,  0, wx.CENTER|wx.ALL, 5)
        
        self.mainSizer.Add(widgetSizer, 0, wx.CENTER|wx.ALL, 10)
        self.mainSizer.Add(bottomSizer, 0, wx.CENTER|wx.ALL, 10)
        
        self.SetSizer(self.mainSizer)
        
    #----------------------------------------------------------------------
    def onAddWidget(self, event):
        self.number_of_buttons += 2
        
        text_box_name = "properties"+str(self.number_of_buttons)

        #self.choose_property = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sampleList, 0 )
        self.choose_property = wx.ListBox(self, style=wx.LB_MULTIPLE, choices=self.sampleList)
        # self.choose_property = wx.TextCtrl(self, -1, "", name=text_box_name)
        # self.choose_property.SetHint('Add Properties, separated by comma')

        self.widgetSizer.Add(self.choose_property, 0, wx.ALL, 5)
        self.frame.fSizer.Layout()
        self.frame.Fit()
    
    #----------------------------------------------------------------------
    def onRemoveWidget(self, event):
        if self.widgetSizer.GetChildren():
            sizer_item = self.widgetSizer.GetItem(self.number_of_buttons-1)
            widget = sizer_item.GetWindow()
            self.widgetSizer.Hide(widget)
            widget.Destroy()
            self.number_of_buttons -= 1
            self.frame.fSizer.Layout()
            self.frame.Fit()

        else:
            mssg_box = wx.MessageBox("No Plots to remove !", "Message" ,wx.OK | wx.ICON_INFORMATION)  

    #----------------------------------------------------------------------
    def onClose(self, event):
        frame = self.GetParent()
        frame.Close()

    #----------------------------------------------------------------------
    def onPlot(self, event):
        all_colors = []

        ColorPicker_objects = [widget for widget in self.GetChildren() ]#if isinstance(widget, wx.ColourPickerCtrl)]

        # for ColorPicker_object in ColorPicker_objects:
        #     all_colors.append(ColorPicker_objects.GetColour())
        print(ColorPicker_objects)

    def setTemplate(self, template_list):
        self.templates = template_list
            
                
########################################################################
class MyFrame(wx.Frame):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="Add / Remove Buttons")
        self.fSizer = wx.BoxSizer(wx.VERTICAL)
        panel = MyPanel(self)
        self.fSizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(self.fSizer)
        self.Fit()
        self.Show()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
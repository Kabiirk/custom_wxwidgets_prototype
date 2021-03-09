# REF :
# https://zetcode.com/wxpython/advanced/ -> some useful info on advanced widgets
# https://docs.wxwidgets.org/3.0/overview_customwidgets.html
# http://infinity77.net/pycon/tutorial/pybr/wxpython.html -> a good primer for wxpython and Sizers
# https://www.blog.pythonlibrary.org/2012/05/05/wxpython-adding-and-removing-widgets-dynamically/ -> Add widgets on the click of a button
# https://stackoverflow.com/questions/6745463/exit-frame-and-panel-from-panel-method -> Close parent frame from a button in the panel
# https://stackoverflow.com/questions/15665022/how-do-i-get-the-values-of-textctrl-created-during-a-loop-in-wxpython -> Useful Link to track Textbox IDs
# https://zetcode.com/wxpython/dialogs/ -> build custom dialogs



import wx
########################################################################
class MyPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.number_of_buttons = 0
        self.text_boxes_info = []
        
        
        self.frame = parent
        
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        controlSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.widgetSizer = wx.BoxSizer(wx.VERTICAL)
        bottomSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.addButton = wx.Button(self, label="Add")
        self.addButton.Bind(wx.EVT_BUTTON, self.onAddWidget)
        controlSizer.Add(self.addButton, 0, wx.CENTER|wx.ALL, 5)
        
        self.removeButton = wx.Button(self, label="Remove")
        self.removeButton.Bind(wx.EVT_BUTTON, self.onRemoveWidget)
        controlSizer.Add(self.removeButton, 0, wx.CENTER|wx.ALL, 5)

        closeBtn = wx.Button(self, label="Cancel")
        closeBtn.Bind(wx.EVT_BUTTON, self.onClose)
        bottomSizer.Add(closeBtn,  0, wx.CENTER|wx.ALL, 5)

        self.plotBtn = wx.Button(self, label="Plot")
        self.plotBtn.Bind(wx.EVT_BUTTON, self.onPlot)
        bottomSizer.Add(self.plotBtn,  0, wx.CENTER|wx.ALL, 5)
        
        self.mainSizer.Add(controlSizer, 0, wx.CENTER)
        self.mainSizer.Add(self.widgetSizer, 0, wx.CENTER|wx.ALL, 10)
        self.mainSizer.Add(bottomSizer, 0, wx.CENTER|wx.ALL, 10)
        
        self.SetSizer(self.mainSizer)
        
    #----------------------------------------------------------------------
    def onAddWidget(self, event):
        """"""
        sampleList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
        self.number_of_buttons += 1

        # label = "Button %s" %  self.number_of_buttons
        # name = "button%s" % self.number_of_buttons

        # new_button = wx.Button(self, label=label, name=name)
        # lb = wx.ListBox(self, size=(200, 150), style=wx.LB_MULTIPLE, choices=sampleList)
        text_box_name = "properties"+str(self.number_of_buttons)
        # self.text_boxes_info[text_box_name] = []

        self.choose_property = wx.TextCtrl(self, -1, "", name=text_box_name)
        self.choose_property.SetHint('Add Properties, separated by comma')

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
        all_plot_props = []
        #number_of_subplots = int(self.text_ctrl.GetValue())
        txtCtrl_objects = [widget for widget in self.GetChildren() if isinstance(widget, wx.TextCtrl)]
        for txtCtrl_obj in txtCtrl_objects:
            property_values = txtCtrl_obj.GetValue()
            all_plot_props.append(property_values.split(","))
        self.text_boxes_info = all_plot_props
        print(self.text_boxes_info)
            
                
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
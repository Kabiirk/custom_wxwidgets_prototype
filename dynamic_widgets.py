# # REF :
# # https://zetcode.com/wxpython/advanced/ -> some useful info on advanced widgets
# # https://docs.wxwidgets.org/3.0/overview_customwidgets.html
# # http://infinity77.net/pycon/tutorial/pybr/wxpython.html -> a good primer for wxpython and Sizers
# # https://www.blog.pythonlibrary.org/2012/05/05/wxpython-adding-and-removing-widgets-dynamically/ -> Add widgets on the click of a button
# # https://stackoverflow.com/questions/6745463/exit-frame-and-panel-from-panel-method -> Close parent frame from a button in the panel
# # https://stackoverflow.com/questions/15665022/how-do-i-get-the-values-of-textctrl-created-during-a-loop-in-wxpython -> Useful Link to track Textbox IDs
# # https://zetcode.com/wxpython/dialogs/ -> build custom dialogs



import wx
import wx.lib.scrolledpanel as scrolled
########################################################################
class MyPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.number_of_buttons = 0
        self.text_boxes_info = []
        self.sampleList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
        
        self.frame = parent
        
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)


        controlSizer = wx.BoxSizer(wx.HORIZONTAL)
        #self.widgetSizer = wx.BoxSizer(wx.HORIZONTAL)
        bottomSizer = wx.BoxSizer(wx.HORIZONTAL)

        # setup scrollpanel
        self.scrollPnl = scrolled.ScrolledPanel(self, -1, size=(400, 200), style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER)
        self.scrollPnlSizer = wx.BoxSizer(wx.HORIZONTAL) #


        self.addButton = wx.Button(self, label="Add")
        self.addButton.Bind(wx.EVT_BUTTON, self.onAddWidget)
        self.removeButton = wx.Button(self, label="Remove")
        self.removeButton.Bind(wx.EVT_BUTTON, self.onRemoveWidget)
        controlSizer.Add(self.addButton, 0, wx.CENTER|wx.ALL, 5)
        controlSizer.Add(self.removeButton, 0, wx.CENTER|wx.ALL, 5)

        closeBtn = wx.Button(self, label="Cancel")
        closeBtn.Bind(wx.EVT_BUTTON, self.onClose)
        self.plotBtn = wx.Button(self, label="Plot")
        self.plotBtn.Bind(wx.EVT_BUTTON, self.onPlot)
        bottomSizer.Add(closeBtn,  0, wx.CENTER|wx.ALL, 5)
        bottomSizer.Add(self.plotBtn,  0, wx.CENTER|wx.ALL, 5)
        
        
        self.mainSizer.Add(controlSizer, 0, wx.CENTER)
        self.mainSizer.Add(self.scrollPnl)
        #self.mainSizer.Add(self.widgetSizer, 0, wx.CENTER|wx.ALL, 10)
        self.mainSizer.Add(bottomSizer, 0, wx.CENTER|wx.ALL, 10)
        
        self.SetSizerAndFit(self.mainSizer)
        
    #----------------------------------------------------------------------
    def onAddWidget(self, event):
        self.number_of_buttons += 1
        
        text_box_name = "properties"+str(self.number_of_buttons)

        choose_property = wx.ListBox(self.scrollPnl, style=wx.LB_MULTIPLE, choices=self.sampleList)
        self.scrollPnlSizer.Add(choose_property, 0, wx.ALL, 3)
        self.scrollPnl.SetSizer(self.scrollPnlSizer)
        self.scrollPnl.SetAutoLayout(1)
        self.scrollPnl.SetupScrolling()  

        self.Refresh()
        self.Layout()
    
    #----------------------------------------------------------------------
    def onRemoveWidget(self, event):
        if self.scrollPnlSizer.GetChildren():
            sizer_item = self.scrollPnlSizer.GetItem(self.number_of_buttons-1)
            widget = sizer_item.GetWindow()
            self.scrollPnlSizer.Hide(widget)
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
        ListBox_objects = [widget for widget in self.scrollPnlSizer.GetChildren() ]#if isinstance(widget, wx.ListBox)]
        print(ListBox_objects)
        for ListBox_object in ListBox_objects:

            property_index_list = ListBox_object.GetWindow().GetSelections()
            property_values = [self.sampleList[index] for index in property_index_list]
            all_plot_props.append(property_values)
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
        



if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
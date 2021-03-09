# REF :
# https://docs.wxwidgets.org/3.0/overview_customwidgets.html
# http://infinity77.net/pycon/tutorial/pybr/wxpython.html -> a good primer for wxpython and Sizers
# https://www.blog.pythonlibrary.org/2012/05/05/wxpython-adding-and-removing-widgets-dynamically/ -> Add widgets on the click of a button

# import wx

# # Import the widgets inspection tool
# import wx.lib.inspection


# class SizersSample(wx.Frame):

#     def __init__(self, parent):

#         wx.Frame.__init__(self, parent, title='Sizers sample')

#         panel = wx.Panel(self)

#         # Widgets creation
#         static_text = wx.StaticText(panel, -1, "Number of Subplots")
#         self.text_ctrl = wx.TextCtrl(panel, -1, "")

#         # Buttons Creation
#         closeBtn = wx.Button(panel, label="Cancel")
#         plotBtn = wx.Button(panel, label="Plot")


#         # Starts of sizers section

#         main_sizer = wx.BoxSizer(wx.VERTICAL)
#         subplot_sizer = wx.BoxSizer(wx.HORIZONTAL) # MY ADDIITON
#         mid_sizer = wx.BoxSizer(wx.HORIZONTAL) # MY ADDIITON
#         bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        

#         # MY ADDIITON
#         subplot_sizer.Add(static_text, 1, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
#         subplot_sizer.Add(self.text_ctrl, 1, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)

#         bottom_sizer.Add(closeBtn, 0, wx.LEFT|wx.ALIGN_CENTER, 5)
#         bottom_sizer.Add(plotBtn, 0, wx.RIGHT|wx.ALIGN_CENTER, 5)

#         # Add both to main Sizer and set Sizer
#         main_sizer.Add(subplot_sizer, 0, wx.ALL|wx.EXPAND, 5)
#         main_sizer.Add(bottom_sizer, 1, wx.ALL|wx.EXPAND, 5)
#         panel.SetSizer(main_sizer)

#         main_sizer.Layout()

#         # EVENT BINDING
#         closeBtn.Bind(wx.EVT_BUTTON, self.onClose)
#         plotBtn.Bind(wx.EVT_BUTTON, self.onPlot)

#     # METHODS FOR BUTTONS
#     def onClose(self, event):
#         self.Close()

#     def onPlot(self, event):
#         number_of_subplots = int(self.text_ctrl.GetValue())
#         print(number_of_subplots)
        

# if __name__ == '__main__':
#     app = wx.App(0)
#     frame = SizersSample(None)
#     frame.Show()

#     #wx.lib.inspection.InspectionTool().Show()

#     app.MainLoop()

import wx
########################################################################
class MyPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.number_of_buttons = 0
        self.frame = parent
        
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        controlSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.widgetSizer = wx.BoxSizer(wx.VERTICAL)
        
        self.addButton = wx.Button(self, label="Add")
        self.addButton.Bind(wx.EVT_BUTTON, self.onAddWidget)
        controlSizer.Add(self.addButton, 0, wx.CENTER|wx.ALL, 5)
        
        self.removeButton = wx.Button(self, label="Remove")
        self.removeButton.Bind(wx.EVT_BUTTON, self.onRemoveWidget)
        controlSizer.Add(self.removeButton, 0, wx.CENTER|wx.ALL, 5)
        
        self.mainSizer.Add(controlSizer, 0, wx.CENTER)
        self.mainSizer.Add(self.widgetSizer, 0, wx.CENTER|wx.ALL, 10)
        
        self.SetSizer(self.mainSizer)
        
    #----------------------------------------------------------------------
    def onAddWidget(self, event):
        """"""
        self.number_of_buttons += 1
        label = "Button %s" %  self.number_of_buttons
        name = "button%s" % self.number_of_buttons
        new_button = wx.Button(self, label=label, name=name)
        self.widgetSizer.Add(new_button, 0, wx.ALL, 5)
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

    #----------------------------------------------------------------------
    def a_func(self, event):
        print("I was pressed !")
            
                
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

# REF :
# https://docs.wxwidgets.org/3.0/overview_customwidgets.html
# http://infinity77.net/pycon/tutorial/pybr/wxpython.html -> a good primer for wxpython and Sizers
# https://www.blog.pythonlibrary.org/2012/05/05/wxpython-adding-and-removing-widgets-dynamically/ -> Add widgets on the click of a button

import wx

# Import the widgets inspection tool
import wx.lib.inspection


class SizersSample(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, title='Sizers sample')

        panel = wx.Panel(self)

        # Widgets creation
        static_text = wx.StaticText(panel, -1, "Number of Subplots")
        self.text_ctrl = wx.TextCtrl(panel, -1, "")

        # Buttons Creation
        closeBtn = wx.Button(panel, label="Cancel")
        plotBtn = wx.Button(panel, label="Plot")



        # Starts of sizers section

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        subplot_sizer = wx.BoxSizer(wx.HORIZONTAL) # For Buttons
        self.widget_sizer = wx.BoxSizer(wx.HORIZONTAL) # For adding subplots
        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL) # For closing window and plotting
        

        # ADD Widgets to Sizer here
        subplot_sizer.Add(static_text, 1, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        subplot_sizer.Add(self.text_ctrl, 1, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)

        bottom_sizer.Add(closeBtn, 0, wx.LEFT|wx.ALIGN_CENTER, 5)
        bottom_sizer.Add(plotBtn, 0, wx.RIGHT|wx.ALIGN_CENTER, 5)


        # Add both Sizers to main Sizer and set Sizer
        self.main_sizer.Add(subplot_sizer, 0, wx.ALL|wx.EXPAND, 5)
        self.main_sizer.Add(bottom_sizer, 1, wx.ALL|wx.EXPAND, 5)
        self.main_sizer.Add(self.widget_sizer, 0, wx.CENTER|wx.ALL, 10)
        panel.SetSizer(self.main_sizer)

        self.main_sizer.Layout()

        # EVENT BINDING
        closeBtn.Bind(wx.EVT_BUTTON, self.onClose)
        plotBtn.Bind(wx.EVT_BUTTON, self.onPlot)

    # METHODS FOR BUTTONS
    def onClose(self, event):
        self.Close()

    def onPlot(self, event):
        number_of_subplots = int(self.text_ctrl.GetValue())
        print(number_of_subplots)
        

if __name__ == '__main__':
    app = wx.App(0)
    frame = SizersSample(None)
    frame.Show()

    #wx.lib.inspection.InspectionTool().Show()

    app.MainLoop()
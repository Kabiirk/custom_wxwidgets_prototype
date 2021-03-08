# REF : https://docs.wxwidgets.org/3.0/overview_customwidgets.html
#     : http://infinity77.net/pycon/tutorial/pybr/wxpython.html

import wx

# Import the widgets inspection tool
import wx.lib.inspection


class SizersSample(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, title='Sizers sample')

        panel = wx.Panel(self)

        # Widgets creation
        static_text = wx.StaticText(panel, -1, "Number of Subplots")
        text_ctrl = wx.TextCtrl(panel, -1, "")

        # Buttons Creation
        closeBtn = wx.Button(panel, label="Cancel")
        plotBtn = wx.Button(panel, label="Plot")


        # Starts of sizers section

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        center_sizer = wx.BoxSizer(wx.HORIZONTAL) # MY ADDIITON
        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        

        # MY ADDIITON
        center_sizer.Add(static_text, 1, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        center_sizer.Add(text_ctrl, 1, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)

        bottom_sizer.Add(closeBtn, 0, wx.LEFT|wx.ALIGN_CENTER, 5)
        bottom_sizer.Add(plotBtn, 0, wx.RIGHT|wx.ALIGN_CENTER, 5)

        # Add both to main Sizer and set Sizer
        main_sizer.Add(center_sizer, 0, wx.ALL|wx.EXPAND, 5)
        main_sizer.Add(bottom_sizer, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(main_sizer)

        main_sizer.Layout()

        # EVENT BINDING
        closeBtn.Bind(wx.EVT_BUTTON, self.onClose)
        plotBtn.Bind(wx.EVT_BUTTON, self.onPlot)

    # METHODS FOR BUTTONS
    def onClose(self, event):
        self.Close()

    def onPlot(self, event):
        print("Plot !")
        

if __name__ == '__main__':
    app = wx.App(0)
    frame = SizersSample(None)
    frame.Show()

    #wx.lib.inspection.InspectionTool().Show()

    app.MainLoop()

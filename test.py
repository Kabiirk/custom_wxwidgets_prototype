# REF : https://docs.wxwidgets.org/3.0/overview_customwidgets.html
#     : http://infinity77.net/pycon/tutorial/pybr/wxpython.html

import wx

# Import the widgets inspection tool
import wx.lib.inspection


class SizersSample(wx.Frame):
    value = ''

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, title='Sizers sample')

        panel = wx.Panel(self)

        # Widgets creation
        radio_button = wx.RadioButton(panel, -1, "RadioButton")
        check_box = wx.CheckBox(panel, -1, "CheckBox")
        spin_ctrl = wx.SpinCtrl(panel, -1, "", min=0, max=100)
        text_ctrl_1 = wx.TextCtrl(panel, -1, "A first text control", style=wx.TE_MULTILINE)
        text_ctrl_2 = wx.TextCtrl(panel, -1, "A second text control", style=wx.TE_MULTILINE)

        # Buttons Creation
        closeBtn = wx.Button(panel, label="Cancel")
        plotBtn = wx.Button(panel, label="Plot")
        
        
        # MY ADDIITON
        static_text2 = wx.StaticText(panel, -1, "Number of Subplots")
        text_ctrl_3 = wx.TextCtrl(panel, -1, "put no.")

        # Starts of sizers section

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        center_sizer = wx.BoxSizer(wx.HORIZONTAL)
        center_sizer2 = wx.BoxSizer(wx.HORIZONTAL) # MY ADDIITON
        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        bottom_sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        
        #static_text = wx.StaticText(panel, -1, "StaticText")
        #main_sizer.Add(static_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        
        center_sizer.Add(radio_button, 1, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        center_sizer.Add(check_box, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        center_sizer.Add(spin_ctrl, 1, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)

        # MY ADDIITON
        center_sizer2.Add(static_text2, 1, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        center_sizer2.Add(text_ctrl_3, 1, wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)

        bottom_sizer.Add(text_ctrl_1, 1, wx.ALL|wx.EXPAND, 5)
        bottom_sizer.Add(text_ctrl_2, 1, wx.ALL|wx.EXPAND, 5)

        bottom_sizer2.Add(closeBtn, 0, wx.LEFT|wx.ALIGN_CENTER, 5)
        bottom_sizer2.Add(plotBtn, 0, wx.RIGHT|wx.ALIGN_CENTER, 5)

        main_sizer.Add(center_sizer, 0, wx.ALL|wx.EXPAND, 5)
        main_sizer.Add(center_sizer2, 0, wx.ALL|wx.EXPAND, 5)
        main_sizer.Add(bottom_sizer, 1, wx.ALL|wx.EXPAND, 5)
        main_sizer.Add(bottom_sizer2, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(main_sizer)

        main_sizer.Layout()

        # EVENT BINDING
        closeBtn.Bind(wx.EVT_BUTTON, self.onClose)
        plotBtn.Bind(wx.EVT_BUTTON, self.onPlot)

    # METHODS FOR BUTTONS
    def onClose(self, event):
        self.Close()

    def onPlot(self, event):
        print(event.GetValue())
        

if __name__ == '__main__':
    app = wx.App(0)
    frame = SizersSample(None)
    frame.Show()

    #wx.lib.inspection.InspectionTool().Show()

    app.MainLoop()

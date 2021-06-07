# # REF :
# # https://zetcode.com/wxpython/advanced/ -> some useful info on advanced widgets
# # https://docs.wxwidgets.org/3.0/overview_customwidgets.html
# # http://infinity77.net/pycon/tutorial/pybr/wxpython.html -> a good primer for wxpython and Sizers
# # https://www.blog.pythonlibrary.org/2012/05/05/wxpython-adding-and-removing-widgets-dynamically/ -> Add widgets on the click of a button
# # https://stackoverflow.com/questions/6745463/exit-frame-and-panel-from-panel-method -> Close parent frame from a button in the panel
# # https://stackoverflow.com/questions/15665022/how-do-i-get-the-values-of-textctrl-created-during-a-loop-in-wxpython -> Useful Link to track Textbox IDs
# # https://zetcode.com/wxpython/dialogs/ -> build custom dialogs


import os

import wx
import wx.lib.scrolledpanel as scrolled
import wx.lib.inspection

import pandas as pd
import numpy as np

class SelectSwirrColumn(wx.Dialog):
    def __init__(self, parent, data):
        self.available_columns = list(data.columns)
        wx.Dialog.__init__(self, None, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER, size=(300, 300))

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        colSizer = wx.BoxSizer(wx.HORIZONTAL)
        col_text = wx.StaticText(self, wx.ID_ANY, u"Choose SWirr Column", wx.DefaultPosition, wx.DefaultSize, 0)
        self.col_choice = wx.Choice(self, id=wx.ID_ANY, choices=self.available_columns, style=0, validator=wx.DefaultValidator, name=wx.ChoiceNameStr)
        colSizer.Add(col_text , 0, wx.ALL, 0)
        colSizer.Add(self.col_choice , 0, wx.ALL, 0)


        buttonsSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btnOK = wx.Button(self, wx.ID_OK)
        self.btnCancel = wx.Button(self, wx.ID_CANCEL)
        buttonsSizer.Add(self.btnOK, 0, wx.ALL|wx.CENTER, 5)
        buttonsSizer.Add(self.btnCancel, 0, wx.ALL|wx.CENTER, 5)


        mainSizer.Add(colSizer, 0, wx.EXPAND|wx.ALL, 5)
        mainSizer.Add(buttonsSizer, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(mainSizer)
        self.Maximize()
        self.Layout()
        mainSizer.Fit(self)
        self.Centre(wx.BOTH)

    def get_chosen_column(self):
        chosen_col_index = self.col_choice.GetSelection()
        print(str(self.available_columns[chosen_col_index]))
        return str(self.available_columns[chosen_col_index])


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
        self.scrollPnlSizer = wx.BoxSizer(wx.VERTICAL) #


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
        self.csvBtn = wx.Button(self, label="Read .csv")
        self.csvBtn.Bind(wx.EVT_BUTTON, self.oncsv)
        self.excelBtn = wx.Button(self, label="Read .xls")
        self.excelBtn.Bind(wx.EVT_BUTTON, self.onexcel)
        bottomSizer.Add(closeBtn,  0, wx.CENTER|wx.ALL, 5)
        bottomSizer.Add(self.plotBtn,  0, wx.CENTER|wx.ALL, 5)
        bottomSizer.Add(self.csvBtn,  0, wx.CENTER|wx.ALL, 5)
        bottomSizer.Add(self.excelBtn,  0, wx.CENTER|wx.ALL, 5)
        
        
        self.mainSizer.Add(controlSizer, 0, wx.CENTER)
        self.mainSizer.Add(self.scrollPnl)
        #self.mainSizer.Add(self.widgetSizer, 0, wx.CENTER|wx.ALL, 10)
        self.mainSizer.Add(bottomSizer, 0, wx.CENTER|wx.ALL, 10)
        
        self.SetSizerAndFit(self.mainSizer)
        
    #----------------------------------------------------------------------
    def onAddWidget(self, event):
        self.number_of_buttons += 1

        #choose_property = wx.ListBox(self.scrollPnl, style=wx.LB_MULTIPLE, choices=self.sampleList)

        range_and_value_Sizer = wx.BoxSizer(wx.HORIZONTAL)
        range_input = wx.TextCtrl(self.scrollPnl, wx.ID_ANY, 'Range')
        value = wx.TextCtrl(self.scrollPnl, wx.ID_ANY, 'Value')

        range_and_value_Sizer.Add(range_input, 0, wx.ALL, 5)
        range_and_value_Sizer.Add(value, 0, wx.ALL, 5)

        self.scrollPnlSizer.Add(range_and_value_Sizer, 0, wx.ALL, 5)
        self.scrollPnl.SetSizer(self.scrollPnlSizer)
        self.scrollPnl.SetAutoLayout(1)
        self.scrollPnl.SetupScrolling()  

        self.Refresh()
        self.Layout()
    
    #----------------------------------------------------------------------
    def onRemoveWidget(self, event):
        sizer_list = list(self.scrollPnlSizer.GetChildren())
        last_sizer = sizer_list.pop()
        last_box_sizer = last_sizer.GetSizer()
        last_box_sizer.Destroy()
        # last_sizer_item = sizer_list.pop()
        # last_box_sizer = last_sizer_item.GetSizer()
        # print(last_box_sizer.GetItem(1))
        # for item in sizer_list:
        #     print(item.GetSizer())
        # if len(sizer_list)>0:
        #     #sizer_list = list(self.scrollPnlSizer.GetChildren()) #self.scrollPnlSizer.GetItem(self.number_of_buttons-1)
        #     # widget = sizer_item.GetWindow()
        #     # self.scrollPnlSizer.Hide(widget)
        #     # widget.Destroy()
        #     # self.number_of_buttons -= 1
        #     # self.frame.fSizer.Layout()
        #     # self.frame.Fit()
        #     return


        # else:
        #     mssg_box = wx.MessageBox("No Plots to remove !", "Message" ,wx.OK | wx.ICON_INFORMATION)  

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

    def oncsv(self, event):
        wildcard = "SWirr CSV (*.csv)|*.csv"
        home_dir = os.path.expanduser('~')
        prime_dir = os.path.join(home_dir, 'PrimeProjects')
        dlg = wx.FileDialog(
            None,
            message="Select csv for facies",
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN,
            defaultDir=prime_dir if os.path.exists(home_dir) else home_dir
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            csv_dataframe = pd.read_csv(path)
            dlg.Destroy()

            col_dlg = SelectSwirrColumn(None, csv_dataframe)
            if col_dlg.ShowModal() == wx.ID_OK:
                swirr_col = col_dlg.get_chosen_column()
                print(csv_dataframe[swirr_col])
                col_dlg.Destroy()
            else:
                # VERY IMPORTANT, IF DIALOG NOT DESTROYED
                # IT STILL RUNS IN app.MainLoop() LIKE AN
                # INFINITE LOOP & CONTROL IS NOT RETURNED
                # TO USER/TERMINAL
                col_dlg.Destroy()
        else:
            # VERY IMPORTANT, SAME REASON
            dlg.Destroy()
                
    def onexcel(self, event):
        wildcard = "SWirr XLS (*.xls)|*.xls"
        home_dir = os.path.expanduser('~')
        prime_dir = os.path.join(home_dir, 'PrimeProjects')
        dlg = wx.FileDialog(
            None,
            message="Select xls for facies",
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN,
            defaultDir=prime_dir if os.path.exists(home_dir) else home_dir
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            excel_dataframe = pd.read_excel(path)
            dlg.Destroy()

            col_dlg = SelectSwirrColumn(None, excel_dataframe)
            if col_dlg.ShowModal() == wx.ID_OK:
                swirr_col = col_dlg.get_chosen_column()
                print(excel_dataframe[swirr_col])
                col_dlg.Destroy()
            else:
                # VERY IMPORTANT, IF DIALOG NOT DESTROYED
                # IT STILL RUNS IN app.MainLoop() LIKE AN
                # INFINITE LOOP & CONTROL IS NOT RETURNED
                # TO USER/TERMINAL
                col_dlg.Destroy()
        else:
            # VERY IMPORTANT, SAME REASON
            dlg.Destroy()
                
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
    #wx.lib.inspection.InspectionTool().Show()
    app.MainLoop()
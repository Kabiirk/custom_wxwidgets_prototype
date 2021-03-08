import wx
from wx.lib import sized_controls

ID_GMAIL = wx.NewIdRef(count=1)
ID_OUTLOOK = wx.NewIdRef(count=1)


class CustomDialog(sized_controls.SizedDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)
        pane = self.GetContentsPane()

        static_line = wx.StaticLine(pane, style=wx.LI_HORIZONTAL)
        static_line.SetSizerProps(border=(('all', 0)), expand=True)

        pane_btns = sized_controls.SizedPanel(pane)
        pane_btns.SetSizerType('horizontal')
        pane_btns.SetSizerProps(align='center')

        button_ok = wx.Button(pane_btns, ID_GMAIL, label='Gmail')
        button_ok.Bind(wx.EVT_BUTTON, self.on_button)

        button_ok = wx.Button(pane_btns, ID_OUTLOOK, label='Outlook')
        button_ok.Bind(wx.EVT_BUTTON, self.on_button)

        self.Fit()

    def on_button(self, event):
        if self.IsModal():
            self.EndModal(event.EventObject.Id)
        else:
            self.Close()


if __name__ == '__main__':
    app = wx.App(False)
    dlg = CustomDialog(None, title='Custom Dialog')
    result = dlg.ShowModal()
    if result == ID_GMAIL:
        print('Gmail')
    elif result == ID_OUTLOOK:
        print('Outlook')
    dlg.Destroy()
    app.MainLoop()
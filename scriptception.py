import wx
import subprocess
from signal import SIGKILL
import os

class MyFrame(wx.Frame):

    def __init__(self, parent, id=-1, title='External program test',
                 pos=wx.DefaultPosition, size=(600, 600)):
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.text1 = wx.TextCtrl(self, -1, '', wx.DefaultPosition, wx.Size(500,500),
                            wx.NO_BORDER | wx.TE_MULTILINE)
        stop_button = wx.Button(self, wx.ID_ANY, "&Stop", pos=(400,520))
        self.Bind(wx.EVT_BUTTON, self.OnStop)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Show()
        #Call python with -u for unbuffer I/O
        p = subprocess.Popen(["python", "-u", "testp.py"], stdout=subprocess.PIPE, bufsize=-1)
        self.pid = p.pid
        #Poll process for output
        while p.poll() is None:
            x = p.stdout.readline().decode() #decode bytes but don't strip linefeeds
            self.text1.write(x)
            wx.GetApp().Yield() # Yield to MainLoop for interactive Gui
        self.text1.write("\nProcess has ended")

    def OnStop(self, event):
        try:
            os.kill(int(self.pid), SIGKILL)
            self.text1.write("\nProcess killed")
        except:
            self.text1.write("\nProcess has ended")

    def OnClose(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None)
    app.MainLoop()
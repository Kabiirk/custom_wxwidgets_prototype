import wx
import numpy 
import matplotlib

from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

class TestFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(500,500))
        self.sp = wx.SplitterWindow(self)
        self.p1 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.p2 = MatplotPanel(self.sp)
        self.sp.SplitVertically(self.p1,self.p2,100)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Oi')

class MatplotPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,-1,size=(50,50))

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        t = numpy.arange(0.0,10,1.0)
        s = [0,1,0,1,0,2,1,2,1,0]
        self.y_max = 1.0
        self.axes.plot(t,s)
        self.canvas = FigureCanvas(self,-1,self.figure)

app = wx.App(redirect=False)
frame = TestFrame(None, 'Hello World!')
frame.Show()
app.MainLoop()
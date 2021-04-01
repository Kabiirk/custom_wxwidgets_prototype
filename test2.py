import wx
import numpy 
import matplotlib

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

t = numpy.arange(0.0, 10.0, 0.1)
s = 1 + numpy.sin(2 * numpy.pi * t)

made_figure, axis = plt.subplots()
axis.plot(t, s)

axis.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
axis.grid()



class TestFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(500,500))
        self.sp = wx.SplitterWindow(self)
        self.p1 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.p2 = MatplotPanel(self.sp)
        self.p2.set_fig(made_figure)
        self.sp.SplitVertically(self.p1,self.p2,100)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Oi')

class MatplotPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # t = numpy.arange(0.0, 10.0, 0.1)
        # s = 1 + numpy.sin(2 * numpy.pi * t)

        # self.figure, self.axis = plt.subplots()
        # self.axis.plot(t, s)

        # self.axis.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
        # self.axis.grid()

        # self.figure = Figure()
        # self.axes = self.figure.add_subplot(111)
        # t = numpy.arange(0.0,10,1.0)
        # s = [0,1,0,1,0,2,1,2,1,0]
        # self.y_max = 1.0
        # self.axes.plot(t,s)
        self.canvas = FigureCanvas(self,-1,self.figure)

    def set_fig(self, created_figure):
        self.figure = created_figure

# mypanel = MatplotPanel(None, title="some Panel")
# mypanel.set_fig(made_figure)

class MyFrame(wx.Frame):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="Add / Remove Buttons")
        self.fSizer = wx.BoxSizer(wx.VERTICAL)
        panel = MatplotPanel(self)
        # self.fSizer.Add(panel, 1, wx.EXPAND)
        # self.SetSizer(self.fSizer)
        # self.Fit()
        self.Show()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
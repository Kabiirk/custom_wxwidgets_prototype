# sample_one_a.py
# REF: https://wiki.wxpython.org/How%20to%20create%20a%20customized%20splash%20screen%20%28Phoenix%29

import sys
import os
import wx
from   wx.adv import SplashScreen as SplashScreen

# class MyFrame
# class MySplash
# class MyApp

#---------------------------------------------------------------------------

class MyFrame(wx.Frame):
    """
    ...
    """
    def __init__(self):
        super(MyFrame, self).__init__(None,
                                      -1,
                                      title="")

        #------------

        # Return application name.
        self.app_name = wx.GetApp().GetAppName()
        # Return icons folder.
        # self.icons_dir = wx.GetApp().GetIconsDir()

        #------------

        # Simplified init method.
        self.SetProperties()
        self.CreateCtrls()
        self.BindEvents()
        self.DoLayout()

        #------------

        self.CenterOnScreen(wx.BOTH)

        #------------

        self.Show(True)

    #-----------------------------------------------------------------------

    def SetProperties(self):
        """
        ...
        """

        self.SetTitle(self.app_name)
        self.SetSize((340, 250))

        #------------

        # frameIcon = wx.Icon(os.path.join(self.icons_dir,
        #                                  "icon_wxWidgets.ico"),
        #                     type=wx.BITMAP_TYPE_ICO)
        #self.SetIcon(frameIcon)


    def CreateCtrls(self):
        """
        ...
        """

        # Create a panel.
        self.panel = wx.Panel(self, -1)

        #------------

        # Add a button.
        self.btnClose = wx.Button(self.panel,
                                  -1,
                                  "&Close")


    def BindEvents(self):
        """
        Bind some events to an event handler.
        """

        # Bind events to an events handler.
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, self.btnClose)


    def DoLayout(self):
        """
        ...
        """

        # MainSizer is the top-level one that manages everything.
        mainSizer = wx.BoxSizer(wx.VERTICAL)

        # wx.BoxSizer(window, proportion, flag, border).
        # wx.BoxSizer(sizer, proportion, flag, border).
        mainSizer.Add(self.btnClose, 1, wx.EXPAND | wx.ALL, 10)

        # Finally, tell the panel to use the sizer for layout.
        self.panel.SetAutoLayout(True)
        self.panel.SetSizer(mainSizer)

        mainSizer.Fit(self.panel)


    def OnCloseMe(self, event):
        """
        ...
        """

        self.Close(True)


    def OnCloseWindow(self, event):
        """
        ...
        """

        self.Destroy()

#---------------------------------------------------------------------------

class MySplash(SplashScreen):
    """
    ...
    """
    def __init__(self):

        #--------------

        screen = wx.ScreenDC()

        # Screen size.
        ws, hs = screen.GetSize()

        #--------------

        # Return bitmaps folder.
        # self.bitmaps_dir = wx.GetApp().GetBitmapsDir()

        # Load a background bitmap.
        bitmap = wx.Bitmap(r"icons\grand-canyon.jpg",
                           type=wx.BITMAP_TYPE_JPEG)

        # Determine size of bitmap.
        wi, hi = bitmap.GetWidth(), bitmap.GetHeight()
        print("\n... Bitmap size : %sx%s px" % (wi, hi))

        x = int((ws-wi)/2)
        y = int((hs-hi)/2)

        #--------------

        super(MySplash, self).__init__(bitmap=bitmap,
                                       splashStyle=wx.adv.SPLASH_CENTRE_ON_SCREEN |
                                                   wx.adv.SPLASH_TIMEOUT,
                                       milliseconds=8000,
                                       parent=None,
                                       id=-1,
                                       pos=(x, y),
                                       size=(wi, hi),
                                       style=wx.STAY_ON_TOP |
                                             wx.BORDER_NONE)

        #------------

        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)

        self.count = 0

        wx.Sleep(1)

        #------------

        # Simplified init method.
        self.CreateCtrls()
        self.BindEvents()

        #------------

        # Create a timer for my gauge.
        self.timer = wx.Timer(self)

        # Gauge speed. Simulate long startup time.
        self.timer.Start(90)

        self.Bind(wx.EVT_TIMER, self.TimerHandler, self.timer)

        #------------

        print("\n... Display the splashScreen")

        #--------------

        wx.BeginBusyCursor()

    #-----------------------------------------------------------------------

    def CreateCtrls(self):
        """
        Create some controls for my splash screen.
        """

        #------------

        # Put text.
        self.text = wx.StaticText(parent=self,
                                  id=-1,
                                  label="Starting...",
                                  pos=(4, 231),
                                  size=(252, 18),
                                  style=wx.ALIGN_CENTRE_HORIZONTAL)
        self.text.SetBackgroundColour(wx.WHITE)

        #------------

        # Put gauge.
        self.gauge = wx.Gauge(self,
                              id=-1,
                              range=50,
                              size=(-1, 20))

        #------------

        # Cody Precord... thank you !
        rect = self.GetClientRect()
        new_size = (rect.width, 20)
        self.gauge.SetSize(new_size)
        self.SetSize((rect.width, rect.height+20))
        self.gauge.SetPosition((0, rect.height))


    def BindEvents(self):
        """
        Bind all the events related to my splash screen.
        """

        # Bind events to an events handler.
        self.Bind(wx.EVT_CLOSE, self.OnClose)


    def TimerHandler(self, event):
        """
        ...
        """

        self.count = self.count + 1

        if self.count > 20:
            self.text.SetLabel("Loading .LAS Files")

        self.gauge.SetValue(self.count)

        if self.count >= 90:
            self.text.SetLabel("Just a Little Longer...")
            #self.count = 0

        
        # or
        # self.gauge.Pulse()


    def OnClose(self, event):
        """
        Close the splash screen.
        This method will be called under 2 cases :
        1. time-limit is up, called automatically,
        2. you left-click on the splash-bitmap.
        """

        # Make sure the default handler runs
        # too so this window gets destroyed.
        # Tell the event system to continue
        # looking for an event handler, so the
        # default handler will get called.
        event.Skip()
        self.Destroy()

        #------------

        if self.timer.IsRunning():
            # Stop the gauge timer.
            self.timer.Stop()
            # del self.timer
            self.ShowMainFrame()


    def ShowMainFrame(self):
        """
        ...
        """

        print("\n... Close the splash screen")
        print("\n... Create and display the main frame")

        #------------

        wx.CallAfter(wx.EndBusyCursor)

        #------------

        # Create an instance of the MyFrame class.
        frame = MyFrame()

#---------------------------------------------------------------------------

class MyApp(wx.App):
    """
    ...
    """
    def OnInit(self):

        #------------

        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)

        #------------

        self.SetAppName("Main frame")

        #------------

        self.installDir = os.path.split(os.path.abspath(sys.argv[0]))[0]

        #------------

        splash = MySplash()
        splash.Show(True)

        return True

    #-----------------------------------------------------------------------

    def GetInstallDir(self):
        """
        Returns the installation directory for my application.
        """

        return self.installDir


    # def GetIconsDir(self):
    #     """
    #     Returns the icons directory for my application.
    #     """

    #     icons_dir = os.path.join(self.installDir, "icons")
    #     return icons_dir


    # def GetBitmapsDir(self):
    #     """
    #     Returns the bitmaps directory for my application.
    #     """

    #     bitmaps_dir = os.path.join(self.installDir, "bitmaps")
    #     return bitmaps_dir

#---------------------------------------------------------------------------

def main():
    app = MyApp(False)
    app.MainLoop()

#---------------------------------------------------------------------------

if __name__ == "__main__" :
    main()
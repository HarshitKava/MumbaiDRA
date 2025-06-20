def Test1():
  brave = Aliases.brave
  wndChrome_WidgetWin_1 = brave.wndChrome_WidgetWin_1
  wndChrome_WidgetWin_1.Click(1270, 9)
  Browsers.Item[btChrome].Run("")
  chrome_RenderWidgetHostHWND = wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND
  OCR.Recognize(chrome_RenderWidgetHostHWND).BlockByText("Employee Id").Click()
  wndChrome_WidgetWin_12 = brave.wndChrome_WidgetWin_12
  wndChrome_WidgetWin_12.MouseWheel(-2)
  OCR.Recognize(wndChrome_WidgetWin_12).BlockByText("SiteEngALK").Click()
  OCR.Recognize(chrome_RenderWidgetHostHWND).BlockByText("Log").Click()
  chrome_RenderWidgetHostHWND.ClickR(1274, 382)
  OCR.Recognize(wndChrome_WidgetWin_12).BlockByText("Inspect").Click()
  OCR.Recognize(chrome_RenderWidgetHostHWND).BlockByText("Report", spLeftMost).Click()
  chrome_RenderWidgetHostHWND = wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND2
  chrome_RenderWidgetHostHWND.Click(74, 145)
  chrome_RenderWidgetHostHWND.Click(72, 151)
  chrome_RenderWidgetHostHWND2 = wndChrome_WidgetWin_12.Chrome_RenderWidgetHostHWND
  OCR.Recognize(chrome_RenderWidgetHostHWND2).BlockByText("Rahman").Click()
  chrome_RenderWidgetHostHWND.Click(200, 250)
  chrome_RenderWidgetHostHWND.Click(157, 148)
  chrome_RenderWidgetHostHWND2.Click(61, 69)
  chrome_RenderWidgetHostHWND.Click(232, 151)
  wndChrome_WidgetWin_12.Click(110, 45)
  chrome_RenderWidgetHostHWND.Click(269, 158)
  wndChrome_WidgetWin_12.Click(86, 82)
  OCR.Recognize(chrome_RenderWidgetHostHWND).BlockByText("Submit").Click()
  chrome_RenderWidgetHostHWND.Click(62, 196)
  OCR.Recognize(chrome_RenderWidgetHostHWND2).BlockByText("Rahman").Click()
  chrome_RenderWidgetHostHWND.Click(166, 189)
  OCR.Recognize(chrome_RenderWidgetHostHWND2).BlockByText("Mason").Click()
  chrome_RenderWidgetHostHWND.Click(222, 198)
  chrome_RenderWidgetHostHWND.Click(223, 185)
  wndChrome_WidgetWin_12.Click(138, 93)
  chrome_RenderWidgetHostHWND.Click(275, 188)
  wndChrome_WidgetWin_12.Drag(76, 123, 5, -14)
  OCR.Recognize(chrome_RenderWidgetHostHWND).BlockByText("Submit").Click()
  OCR.Recognize(chrome_RenderWidgetHostHWND).BlockByText("Home").Click()
  OCR.Recognize(chrome_RenderWidgetHostHWND).BlockByText("Out").Click()

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.rst import RstDocument

from kivy.uix.actionbar import ActionBar


Builder.load_string('''
<TabbedPanel>:
    size_hint: .5, .5
    pos_hint: {'center_x': .5, 'center_y': .5 }
    do_default_tab: False
    TabbedPanelItem:
        text: 'Tab 1'
        Label:
            text: "First Tab"
    TabbedPanelItem:
        text: 'Tab 2'
        Label: 
            text: "2nd Tab"
    TabbedPanelItem:
        text: 'Tab 3'
        BoxLayout:
            Label:
                text: 'Press Button'
            Button:
                text: 'Click it'
    TabbedPanelItem:
        text: 'Tab 4'
        RstDocument:
            text: "hello from sicko head!!!"
    
''')


# Create Tabbed class 
# class Tab(TabbedPanel):
#     pass

class MyTab(TabbedPanel):
    pass
   
# create App class
class TabbedPanelApp(App):
    def build(self):
        return MyTab()
  
# run the App
if __name__ == '__main__':
    TabbedPanelApp().run()

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.actionbar import ActionBar

from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.stencilview import StencilView
from random import random as r
from functools import partial

Builder.load_string('''
<ActionBar>:
    pos_hint: {'top':1}
    ActionView:
        use_separator: True
        ActionPrevious: 
        ActionButton:
            text: 'Btn1'
        ActionButton:
            text: 'Btn2'
        ActionButton:
            text: 'Btn3'
        ActionButton:
            text: 'Btn4'
        ActionGroup:
            text: 'Group1'
            ActionButton:
                text: 'Btn5'
            ActionButton:
                text: 'Btn6'
            ActionButton:
                text: 'Btn7'
        ActionButton:
            text: 'Btn8'
''')

class CustomeActionBar(ActionBar):
    pass

class ActionBarApp(App):
    def build(self):
        return CustomeActionBar()

app = ActionBarApp()
app.run()
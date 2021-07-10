'''
kivy_gui_001.py

'''
import kivy
from kivy.app import App 
from kivy.lang import Builder

import kivy_garden.contextmenu

kv = """
FloatLayout:
    id: layout

    TabbedPanel:
        size_hint: 1, .95
        # pos_hint: {'center_x': .5, 'center_y': .5 }
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
                text: 
                    '\\n'.join(("Hello world", "-----------",
                    "You are in the third tab."))
    AppMenu:
        id: app_menu
        top: root.height
        cancel_handler_widget: layout

        AppMenuTextItem:
            text: "Menu #1"
            ContextMenu:
                ContextMenuTextItem:
                    text: "Item #11"
                ContextMenuTextItem:
                    text: "Item #12"
        AppMenuTextItem:
            text: "Menu Menu Menu #2"
            ContextMenu:
                ContextMenuTextItem:
                    text: "Item #21"
                ContextMenuTextItem:
                    text: "Item #22"
                ContextMenuTextItem:
                    text: "ItemItemItem #23"
                ContextMenuTextItem:
                    text: "Item #24"
                    ContextMenu:
                        ContextMenuTextItem:
                            text: "Item #241"
                        ContextMenuTextItem:
                            text: "Hello, World!"
                            on_release: app.say_hello(self.text)
                        # ...
                ContextMenuTextItem:
                    text: "Item #5"
        AppMenuTextItem:
            text: "Menu Menu #3"
            ContextMenu:
                ContextMenuTextItem:
                    text: "SubMenu #31"
                ContextMenuDivider:
                ContextMenuTextItem:
                    text: "SubMenu #32"
                # ...
        AppMenuTextItem:
            text: "Menu #4"
    # ...
    # The rest follows as usually

    
"""

class MyApp(App):
    def build(self):
        self.title = 'Simple app menu example'
        return Builder.load_string(kv)

    def say_hello(self, text):
        print(text)
        self.root.ids['app_menu'].close_all()

if __name__ == '__main__':
    MyApp().run()
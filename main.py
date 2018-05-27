from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.config import Config


Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 400)
Config.set("graphics", "height", 500)


class ReminderApp(App):
    def build(self):

        layout = BoxLayout(orientation="vertical",
                           padding=20,
                           spacing=10)

        self.lbl = Label(text="Choose what to remind",
                         font_size=50)
        layout.add_widget(self.lbl)
        layout.add_widget(Button(text="Option 1"))
        layout.add_widget(Button(text="Option 2"))

        return layout


if __name__ == "__main__":
    ReminderApp().run()

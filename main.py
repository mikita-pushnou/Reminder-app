from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.config import Config
from threading import Timer

Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 400)
Config.set("graphics", "height", 500)

time_var = 5


class myLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical",
                           padding=20,
                           spacing=10)

        btn = Button(text="Set up timer")

        self.add_widget(layout)
        layout.add_widget(btn)

        btn.bind(on_press=self.timer)

    def popup(self):

        popup = Popup(title="Remind you to",
                      content=Label(text="go for a walk!"),
                      size_hint=(None, None),
                      size=(350, 200))

        popup.open()

    def timer(self, obj):
        timer = Timer(time_var, self.popup)

        timer.start()


class ReminderApp(App):
    def build(self):
        return myLayout()


if __name__ == "__main__":
    ReminderApp().run()

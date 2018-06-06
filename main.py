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

time_var = 1
time_var_2 = 5
remind_text = "go for a walk"
remind_text_2 = "test"


class Reminder(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical",
                           padding=20,
                           spacing=10)

        button = Button(text="Set up timer")
        button_2 = Button(text="Set up timer_2")

        self.add_widget(layout)
        layout.add_widget(button)
        layout.add_widget(button_2)

        button.bind(on_press=self.timer)
        button_2.bind(on_press=self.timer_2)

    def popup(self):

        popup = Popup(title="Remind you to",
                      content=Label(text=remind_text),
                      size_hint=(None, None),
                      size=(350, 200))

        popup.open()

    def popup_2(self):

        popup_2 = Popup(title="Remind you to",
                        content=Label(text=remind_text_2),
                        size_hint=(None, None),
                        size=(350, 200))

        popup_2.open()

    def timer(self, obj):
        timer = Timer(time_var, self.popup)

        timer.start()

    def timer_2(self, obj):
        timer = Timer(time_var_2, self.popup_2)

        timer.start()


class ReminderApp(App):
    def build(self):
        return Reminder()


if __name__ == "__main__":
    ReminderApp().run()

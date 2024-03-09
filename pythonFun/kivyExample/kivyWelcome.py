from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=(10, 10))
        label = Label(text='Welcome to My App!', font_size=24)
        settings_button = Button(text='Settings', on_press=self.go_to_settings)
        layout.add_widget(label)
        layout.add_widget(settings_button)
        self.add_widget(layout)

    def go_to_settings(self, instance):
        self.manager.current = 'settings'

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=(10, 10))
        label = Label(text='Settings Screen', font_size=24)
        back_button = Button(text='Back to Welcome', on_press=self.go_to_welcome)
        layout.add_widget(label)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_to_welcome(self, instance):
        self.manager.current = 'welcome'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__ == '__main__':
    MyApp().run()

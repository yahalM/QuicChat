import re

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty

Window.size = (360, 640)  # Simulate a standard smartphone screen size

Builder.load_string('''
#:import get_color_from_hex kivy.utils.get_color_from_hex

<CustomButton@ButtonBehavior+Label>:
    background_color: 0, 0, 0, 0
    canvas.before:
        Color:
            rgba: self.background_color if self.background_color else (0.25, 0.25, 0.25, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,]

<LoginScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: 15
        size_hint: None, None
        width: 300
        height: 400
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        canvas.before:
            Color:
                rgba: get_color_from_hex("#075E54")
            Rectangle:
                size: self.size
                pos: self.pos

        Label:
            text: 'QuickChat'
            size_hint_y: None
            height: self.texture_size[1]
            font_size: '24sp'
            color: 1, 1, 1, 1

        TextInput:
            id: username
            hint_text: "Username"
            multiline: False
            size_hint_y: None
            height: 40
            padding_x: 10

        TextInput:
            id: password
            hint_text: "Password"
            password: True
            multiline: False
            size_hint_y: None
            height: 40
            padding_x: 10

        CustomButton:
            text: 'Login'
            size_hint_y: None
            height: 50
            background_color: get_color_from_hex("#2ecc71")
            on_press: app.login_user()

        CustomButton:
            text: 'Sign Up'
            size_hint_y: None
            height: 50
            background_color: get_color_from_hex("#3498db")
            on_press: root.manager.transition.direction = 'left'; root.manager.current = 'signup'

        CustomButton:
            text: 'Forgot Password?'
            size_hint_y: None
            height: 40
            background_color: get_color_from_hex("#e74c3c")
            on_press: app.show_forgot_password()

<SignUpScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: 15
        size_hint: None, None
        width: 300
        height: 500
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        canvas.before:
            Color:
                rgba: get_color_from_hex("#2980b9")
            Rectangle:
                size: self.size
                pos: self.pos

        Label:
            text: 'Sign Up'
            size_hint_y: None
            height: self.texture_size[1]
            font_size: '24sp'
            color: 1, 1, 1, 1

        TextInput:
            id: signup_username
            hint_text: "Username"
            multiline: False
            size_hint_y: None
            height: 40
            padding_x: 10

        TextInput:
            id: signup_email
            hint_text: "Email"
            multiline: False
            size_hint_y: None
            height: 40
            padding_x: 10

        TextInput:
            id: signup_password
            hint_text: "Password"
            password: True
            multiline: False
            size_hint_y: None
            height: 40
            padding_x: 10

        TextInput:
            id: signup_confirm_password
            hint_text: "Confirm Password"
            password: True
            multiline: False
            size_hint_y: None
            height: 40
            padding_x: 10

        CustomButton:
            text: 'Register'
            size_hint_y: None
            height: 50
            background_color: get_color_from_hex("#27ae60")
            on_press: app.register_user()

<UserListScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Chat Room 1'
            on_press: app.open_chat('Chat Room 1')
        Button:
            text: 'Chat Room 2'
            on_press: app.open_chat('Chat Room 2')

<ChatScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: chat_label
            text: 'Welcome to the chat room'
            size_hint_y: None
            height: self.texture_size[1]
        ScrollView:
            BoxLayout:
                id: chat_layout
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
        BoxLayout:
            size_hint_y: None
            height: 50
            TextInput:
                id: chat_input
                size_hint_x: 85
            Button:
                text: 'Send'
                size_hint_x: 15
                on_press: app.send_message(chat_input.text)
''')

class LoginScreen(Screen):
    pass

class SignUpScreen(Screen):
    pass

class UserListScreen(Screen):
    pass

class ChatScreen(Screen):
    chat_name = StringProperty('')

class QuickChatApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignUpScreen(name='signup'))
        sm.add_widget(UserListScreen(name='user_list'))
        sm.add_widget(ChatScreen(name='chat'))
        return sm

    def login_user(self):
        self.root.current = 'user_list'

    def register_user(self):
        # Here, implement actual registration logic
        signup_screen = self.root.get_screen('signup')

        # Assuming you have an email TextInput field with id 'email'
        email = signup_screen.ids.signup_email.text
        password = signup_screen.ids.signup_password.text
        confirm_password = signup_screen.ids.signup_confirm_password.text

        # Email regex pattern
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Check if the email matches the pattern
        if re.match(email_pattern, email):
            print("Email is valid")
            # Continue with your authentication logic here
            if password and confirm_password == password:  # Simple check for non-empty password
                print("signup successful")
                self.root.current = 'login'
                self.show_popup("Success", "Registration successful. Please log in.")
            else:
                print("signup failed: Password cannot be empty")
                self.show_popup("Signup Failed", "Password cannot be empty")
        else:
            print("signup failed: Invalid email format")
            self.show_popup("Signup Failed", "Invalid email format")

    def open_chat(self, chat_name):
        self.root.get_screen('chat').chat_name = chat_name
        self.root.current = 'chat'

    def send_message(self, message):
        # Here, implement the logic to send a message
        chat_screen = self.root.get_screen('chat')
        chat_screen.ids.chat_layout.add_widget(Label(text=message))
        chat_screen.ids.chat_input.text = ''

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(300, 200))
        popup.open()

if __name__ == '__main__':
    QuickChatApp().run()

import secrets
import string
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from mailjet_rest import Client
import os

from User import User
from UsersDB import UserDB

# Temporary storage for forgot passwords (email -> temp password)
temp_passwords = {}

class UserContext:
    def __init__(self, db_path):
        self.user_db = UserDB(db_path)

    def signup_user(self, new_user):

        # 1. Validate the user
        is_valid, message = new_user.is_valid()
        if not is_valid:
            return False, message

        # 2. Check that the user doesn't exist
        if self.user_db.get_user(new_user.email):
            return False, "User already exists."

        # 3. Add the user to our DB
        self.user_db.set_user(new_user)

        # 4. Return True and success message
        return True, "User successfully signed up."

    def send_email_with_mailjet(self, to_email, temp_password):
        api_key = '68a5836683b7a1b35c3c226b09a7b8e9'
        api_secret = 'da00e372e026fe9119ad8336cc30e021'
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "duzan21@gmail.com",
                        "Name": "David"
                    },
                    "To": [
                    {
                        "Email": "duzan21@gmail.com",
                        "Name": "David"
                    }
                    ],
                "Subject": "Temporary Password for QuicChat",
                "TextPart": f"Your temporary password is: {temp_password}",
                "HTMLPart": f"Your temporary password is: {temp_password}",
                "CustomID": "QuicChatTempPasword"
                }
            ]
        }
        result = mailjet.send.create(data=data)
        print(result.status_code)
        print(result.json())

    def send_email_with_sendgrid(self, to_email, temp_password):
        SENDGRID_API_KEY = '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'
        sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
        from_email = Email("no-reply@QuicChat.com")  # This can be a custom email address linked to your SendGrid account
        to_email = To(to_email)
        subject = "Temporary Password for QuicChat"
        content = Content("text/plain", f"Your temporary password is: {temp_password}")
        mail = Mail(from_email, to_email, subject, content)

        try:
            response = sg.client.mail.send.post(request_body=mail.get())
            print(response.status_code)
            print(response.body)
            print(response.headers)
            return True, "Temporary password sent to your email."
        except Exception as e:
            print(e)
            return False, "Failed to send temporary password."

    def forgot_password(self, email):
        # 1. Validate that we can find the user email in our DB
        user_data = self.user_db.get_user(email)
        if not user_data:
            return False, "User email not found."

        # 2. Send email with a temporary password to the user email
        alphabet = string.digits
        temp_password = ''.join(secrets.choice(alphabet) for i in range(6))  # 6-character password
        temp_passwords[email] = temp_password  # Save the temporary password todo: save the password secretly

        # Send the temporary password via email (mockup, replace with actual email sending code)
        print(f"Sending email to {email} with temporary password: {temp_password}")
        self.send_email_with_mailjet(email, temp_password)
        # 3. Return True and success message
        return True, "Temporary password sent to your email."

# Example usage:
db_path = 'users_example.json'
user_context = UserContext(db_path)

# Sign up a user
signup_result, message = user_context.signup_user(User("Jane Doe", "duzan21@gmail.com", "password123"))
print(message)

# Forgot password
forgot_result, message = user_context.forgot_password("duzan21@gmail.com")
print(message)

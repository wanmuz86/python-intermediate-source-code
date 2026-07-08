from email_notification import EmailNotification
from sms_notification import SMSNotification
from notification import Notification

def main():
    email = EmailNotification("test@example.com", log_enabled= False)
    sms = SMSNotification("+60123456789")

    email.send("Hello from Email noti")
    sms.send("Hello from SMS noti")

    print("\n --- Documentation Preview--- \n")
    help(SMSNotification) # Notification on CLI, to exit : q
    help(EmailNotification)
    help(Notification)


if __name__ == "__main__":
    main()
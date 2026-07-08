from logged_notification import LoggedNotification


class EmailNotification(LoggedNotification):
    """
    Email notification implementation.

    Attributes:
        subject_prefix (str): Prefix added to email subject.
    """

    def __init__(self, recipient: str, subject_prefix: str = "[APP]", log_enabled = True):
        super().__init__(recipient, log_enabled)
        self.subject_prefix = subject_prefix

    def send(self, message: str) -> None:
        """
        Send an email notification.

        Args:
            message (str): Email message content.
        """
        self.log("Sending SMS")
        print(
            f"[EMAIL] To: {self.recipient} | "
            f"Subject: {self.subject_prefix} Update | "
            f"Message: {message}"
        )



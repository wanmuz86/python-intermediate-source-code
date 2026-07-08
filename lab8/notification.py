from abc import ABC, abstractmethod


class Notification(ABC):
    """
    Base abstract notification type.

    Attributes:
        recipient (str): Target user identifier (email or phone).

    Methods:
        send(message: str) -> None
            Send a message to the recipient.
    """

    def __init__(self, recipient: str):
        self.recipient = recipient

    @abstractmethod
    def send(self, message: str) -> None:
        """
        Send a message to the recipient.

        Args:
            message (str): Message content.
        """
        pass


Nofication = Notification


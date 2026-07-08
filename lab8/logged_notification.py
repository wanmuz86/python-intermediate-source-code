from notification import Nofication

# Abstract class LoggedNotification inherits Notification
class LoggedNotification(Nofication):
    """
    Intermediate notification class with logging support.

    Attributes:
        log_enabled (bool): Enable or disable logging.
    """
    
    def __init__(self, recipient:str, log_enabled:bool = True):
        super().__init__(recipient)
        self.log_enabled = log_enabled
    
    def log(self, action:str)-> None:
        """
        Log an action if logging is enabled.

        Args:
            action (str): Action description.
        """


        if self.log_enabled:
            print(f" [LOG]{action}-> {self.recipient}")

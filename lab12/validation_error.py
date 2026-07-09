from app_error import AppError
class ValidationError(AppError):
    def __init__ (self, field:str, message:str):
        super().__init__(f"{field}:{message}")
        self.field = field
        self.message = message
class NotHandledException(Exception):
    def __init__(self, message: str = "Message Not Handled"):
        super().__init__(message)

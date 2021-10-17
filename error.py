class AuthorisationError(Exception):
    """
    Exception raised for errors in authorisation

    Attributes:
        message -- explanation of the error
    """

    default_message = "User is not authorized"

    def __init__(self, message=default_message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

class HelpNotFoundError(Exception):
    """
    Exception raised for errors in help

    Attributes:
        message -- explanation of the error
    """

    default_message = "Help not found"

    def __init__(self, message=default_message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

class TimezoneNotFoundError(Exception):
    """
    Exception raised for errors in timezones

    Attributes:
        message -- explanation of the error
    """

    default_message = "Timezone not found"

    def __init__(self, message=default_message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

class ArgumentRequiredError(Exception):
    """
    Exception raised for when arguments are required

    Attributes:
        message -- explanation of the error
    """

    default_message = "Argument(s) required"

    def __init__(self, message=default_message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

class UnknownArgumentError(Exception):
    """
    Exception raised for errors in too many arguments

    Attributes:
        message -- explanation of the error
    """

    default_message = "Unknown argument(s)"

    def __init__(self, message=default_message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
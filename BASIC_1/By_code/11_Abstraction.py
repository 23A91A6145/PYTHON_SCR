

    # Abstraction

# Reduce complexity by hiding unnecessary details from the user.

class EmailService:
    def send_email(self):
        # Call private methods within the class
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()

    def _connect(self):
        print("Connecting to email server...")

    def _authenticate(self):
        print("Authenticating...")

    def _disconnect(self):
        print("Disconnecting from email server...")


email = EmailService()
email.send_email()


# Python provides the ABC class and @abstractmethod decorator to define abstract classes and methods.
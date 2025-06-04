from fastapi import status


class AppException(Exception):
    def __init__(self, message: str = "Internal Server Error", status_code: int = 500):
        self.message = message
        self.status_code = status_code


class InvalidDigiPinException(AppException):
    def __init__(self, message: str = "Invalid DIGIPIN"):
        super().__init__(message, status_code=status.HTTP_400_BAD_REQUEST)


class NominatimException(AppException):
    def __init__(self, message: str = "Error occurred while communicating with Nominatim service"):
        super().__init__(message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

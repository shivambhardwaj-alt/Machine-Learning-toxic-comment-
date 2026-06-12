import sys
from datetime import datetime


def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()

    filename = exc_tb.tb_frame.f_code.co_filename
    timestamp  =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    error_message = (
        f"[{timestamp}] "
        f"Error occurred in file {filename}, "
        f"line number {exc_tb.tb_lineno}, "
        f"error message: {str(error)}"
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        self.error_message = error_message_detail(
            error_message,
            error_detail
        )

        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message
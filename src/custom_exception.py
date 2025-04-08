import sys
import traceback

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        """
        Custom exception class for more detailed error messages.

        :param error_message: Message describing the error
        :param error_detail: Typically the `sys` module, to extract traceback
        """
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, error_detail)

    @staticmethod
    def get_detailed_error_message(error_message, error_detail):
        """
        Returns a detailed error message with traceback info.

        :param error_message: Base error message
        :param error_detail: Typically the `sys` module
        :return: Formatted detailed error string
        """
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown"
        return f"Error in file: {file_name}, line: {line_number} -> {error_message}"

    def __str__(self):
        return self.error_message

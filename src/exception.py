# sys is a module that provides various function and variables that are used to manipulate different parts of the Python runtime environment.
import sys


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info() # talking about execution
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)

    return error_message
    )


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str___(self):
        return self.error_message
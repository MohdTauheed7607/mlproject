import sys

def error_message_detail(error_message,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_num=exc_tb.tb_frame.f_lineno

    custom_message=f'''Error has occured in script {file_name} in line 
                    number {line_num} and 
                    error message is {error_message}'''
    
    return custom_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message=error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    


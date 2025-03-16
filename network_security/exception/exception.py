import sys
from network_security.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, detail:sys):
        self.error_message = error_message
        _,_,exc_tb = detail.exc_info()
        
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return "Error occured in file [{0}] line [{1}] message [{2}]".format(self.file_name, 
                                                                             self.lineno, 
                                                                             str(self.error_message))
        
    

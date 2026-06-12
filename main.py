from src.utils.Exception import CustomException
from src.utils.Logger import logging
import sys

def test_exception():
    try:
        a  =  1/0
    except Exception as e:
        raise CustomException(e,sys)
def test_logger():
    try:
        logging.info("Working!!")
    except Exception as e :
        print(e)
if __name__ == '__main__':
    try:
        # test_exception()
        test_logger()
    except Exception as e :
        print(e)
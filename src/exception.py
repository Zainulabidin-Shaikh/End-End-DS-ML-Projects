# exception.py
from src.logger import logging
import logging

# What is this code about?

# This code is about handling errors (also called exceptions) in a better way using a custom exception class. 
# Instead of just showing boring and unclear errors, it tells you:
# Which file caused the error
# Which line of code
# What exactly went wrong

# Now let’s break it all down:

# Import the 'sys' module which allows access to system-specific parameters and functions
# We'll use it to get error details such as file name and line number
import sys

# What is sys?
# sys is a built-in Python module that gives you access to some variables and functions used by the Python interpreter itself.

# One of those is sys.exc_info() which gives detailed info about any error that occurs.

# So, we use sys here to extract error details.

# The error_message_detail Function
# This function generates a detailed error message
def error_message_detail(error, error_detail: sys):
    """
    This is a function that takes two inputs:

    error: the actual error message (like FileNotFoundError)

    error_detail: this is actually sys module (the whole module is passed so we can use exc_info() from it)
    """

    # Extracts exception information: (type, value, traceback)
    _, _, exc_tb = error_detail.exc_info()

    '''
    sys.exc_info() returns 3 values: (type, value, traceback)

    We only care about the traceback (named exc_tb) because it tells us where the error happened (file, line number).

     The _ are used for values we don’t care about right now.
    '''

    # Gets the file name where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    '''
    We use this to find the name of the file where the error happened.

    exc_tb.tb_frame.f_code.co_filename is a chain of attributes to go deep inside the error 
    object and extract the file name.
    '''

    # Creates a formatted error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name, exc_tb.tb_lineno, str(error)
    )

    '''
    This line creates a clear and formatted message showing:

    File name
    Line number
    Error message

    format() is used to insert the values inside the {} placeholders.

    '''

    # Return the final message string
    return error_message
    '''
    Finally, it returns the whole error message as a string.
    '''

# This class defines a custom exception that gives more meaningful error messages
# The CustomException Class
# Now let’s look at this custom class that extends the built-in Exception class:
class CustomException(Exception):
    """
    You're creating your own type of error (a "custom exception")

    It still behaves like a normal Python error but gives more useful info.

    Custom Exception class that inherits from Python's built-in Exception class.
    It adds more detail to the error message, such as:
    - file name
    - line number
    - full error description
    """

    def __init__(self, error_message, error_detail: sys):
        """
        This is the constructor. It runs when we create an instance of this class.

        It takes:

        error_message: the message about what went wrong
        error_detail: again, the sys module, to extract error traceback info

        Constructor for the custom exception.
        Stores the detailed error message created by error_message_detail().
        """
        # Call the base class (Exception) constructor
        super().__init__(error_message)
        # This line initializes the parent Exception class with the message.

        # super() is used to call methods from the parent class.

        # Use our custom function to build a complete message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

        '''
        Here we’re using the earlier function error_message_detail() to generate a 
        full descriptive message and saving it inside the object.
        '''

    def __str__(self):
        """
        This method controls what gets displayed when you print the error.

        This method is used to define what should be shown when you do print(error) or str(error).

        So it returns the full detailed message.
        """
        return self.error_message
    

# ✅ Example usage of this error handler (Uncomment to test in a script)
"""
try:
    # Example of an error: divide by zero
    result = 1 / 0
except Exception as e:
    # Raise the custom exception with system info
    raise CustomException(e, sys)
"""

# How do you use this?

# Let’s say you have a block of code like this:

# to check everything works properly:
# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e,sys)

"""
This will raise an error.

But instead of showing the boring ZeroDivisionError, it will now show:

Error occurred in python script name [your_script.py] line number [X] error message [division by zero]


"""
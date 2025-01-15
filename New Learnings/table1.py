import learntools
# Set up feedack system
from learntools.core import binder
binder.bind(globals())
try:
    from learntools.sql.ex1 import *
except ImportError:
    print("learntools module is not installed. Please install it using 'pip install learntools'.")
print("Setup Complete")
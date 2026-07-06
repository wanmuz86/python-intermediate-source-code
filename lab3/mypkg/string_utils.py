# #Option 1: Absolute import
#from mypkg.math_utils import add

#Option 2: Relative import
from .math_utils import add

def shout(text):
    return text.upper() # uppercase all text

def repeat_and_add(text,a,b):
    return f"{text} {add(a,b)}"
from functions import *

def load(file_name):

    with open(file_name, 'r') as file:

        return convertToArr(file, ";")
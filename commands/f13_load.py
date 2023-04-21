from functions import *

from my_class import *

def load(file_name, tipe):

    with open(file_name, 'r') as file:

        return convertToArr(file, tipe)
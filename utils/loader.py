# ========================================================================================================================================================================
# Dependencies
# ========================================================================================================================================================================

import os
from pandas import read_csv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ========================================================================================================================================================================
# Full data loader
# ========================================================================================================================================================================

def full_loader(file_name, root=ROOT):
    """ RETURNS THE FULL DATABASE """

    file_path = root + '/data/' + str(file_name)
    data = read_csv(file_path)
    return data


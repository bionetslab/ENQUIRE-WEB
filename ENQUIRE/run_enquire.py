


import os
import sys
import numpy as np 
import pandas as pd
import subprocess
import glob 
import re
import bz2

# ===================================

# import ENQUIRE
from code import ENQUIRE
print(os.getcwd())

# # ------

# # # output_=ENQUIRE.run('SplicingFactors_Neoplasms_Antigens', 'pmid-ferroptosis_ImmuneSystem.txt',      1,     "/Users/surya/Documents/GITHUB-REPOSITORIES/ENQUIRE/",     4,2,3,"all",6)
# # output_=run('SplicingFactors_Neoplasms_Antigens', 'pmid-ferroptosis_ImmuneSystem.txt',      1,     "/Users/surya/Documents/GITHUB-REPOSITORIES/ENQUIRE/",     4,2,3,"all",6)

# tag,to_py,thr=1,comb=4,A=2,K=3,ncores=6, wd="os.getcwd()", etype='all'
output_=ENQUIRE.run('test','/home/surya/Documents/GitHub/ENQUIRE/input/pmid-ferroptosis_ImmuneSystem.txt', 1,4,2,3,6,'/home/surya/Documents/GitHub/ENQUIRE/', etype='all')


# ===================================

print(output_)
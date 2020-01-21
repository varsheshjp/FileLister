import argparse 
from explorer import Explorer
import pandas as pd
import numpy as np
parser = argparse.ArgumentParser(description='File explorer')
parser.add_argument('--dir',default='./',action='store', dest='inpath',help='path to directory')
parser.add_argument('--out',default='./data.csv',action='store', dest='outpath',help='path to output file')
parser.add_argument('--sort',default='none',action='store', dest='sort',help='sort by name,type,created,modified,accessed,fullpath,size')
print('argument parsing...\n\n')
argument=parser.parse_args()

path=argument.inpath
csv=argument.outpath
sort=argument.sort
print('dir :',path)
print('csv :',csv)
print('sort:',sort)
print('\nstarting explorer')
expo=Explorer(path)
d,n=expo.searchInit()
data=pd.DataFrame(data=d)
if sort in ['name','type','created','modified','accessed','fullpath','size']:
    data=data.sort_values([sort],ascending=True)
data.to_csv(csv)
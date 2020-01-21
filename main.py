import argparse 
from explorer import Explorer
import pandas as pd
import numpy as np
parser = argparse.ArgumentParser(description='File explorer')
parser.add_argument('--dir',default='./',action='store', dest='inpath',help='path to directory')
parser.add_argument('--out',default='./data.csv',action='store', dest='outpath',help='path to output file')
parser.add_argument('--sort',default='none',action='store', dest='sort',help='sort by name,type,created,modified,accessed,fullpath,size')
parser.add_argument('-p',default='no',action='store',dest='print')
print('argument parsing...\n\n')
argument=parser.parse_args()

path=argument.inpath
csv=argument.outpath
sort=argument.sort
printF=argument.print
print('dir :',path)
print('csv :',csv)
print('sort:',sort)
print('\n \n starting explorer')
expo=Explorer(path)
print('\n searching started')
if printF not in ['yes','no']:
    printF='no'
d,n=expo.searchInit(printF)
print('\n total file scanned:',n)
data=pd.DataFrame(data=d)
if sort in ['name','type','created','modified','accessed','fullpath','size']:
    data=data.sort_values([sort],ascending=True)
data.to_csv(csv)
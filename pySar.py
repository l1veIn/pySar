import os
import argparse
import pandas as pd
import numpy as np 
def main():
    parser = argparse.ArgumentParser(description="pySar go")
    parser.add_argument('--datadir', type=str, default='None',
                        help='data dir')
    parser.add_argument('--filename', type=str, default='None',
                        help='filename')
    parser.add_argument('--savename', type=str, default='None',
                        help='savename')
    args = parser.parse_args()
    os.system('R CMD BATCH "--args '+args.datadir+' '+args.filename+' '+args.savename+'" utils/test.R ')
    data = pd.read_csv("results/" + args.savename +".csv")
    np.save('results/' + args.savename ,data.values)
    print('success')
if __name__ == "__main__":
    main()
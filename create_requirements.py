# process_input.py

import imageio
import numpy as np
import sys
import matplotlib
import skimage
import tqdm
import torch
import scipy
import yaml
import argparse
import warnings
warnings.filterwarnings("ignore")


if sys.version_info[0] < 3:
    raise Exception(" use version >= 3.7")

def create_requirements():
    """
        creates requirements.txt
    """
    with open('requirements.txt', 'w') as f:
        libs = [    imageio, np, matplotlib, tqdm, torch, skimage,
                    scipy, yaml, argparse
                ]
        for lib in libs:
            try:
                f.write(lib.__name__+"=="+lib.__version__+"\n")
            except Exception as e:
                print( f'EXCEPTION: {e}')
        f.close()   
    print( "requirements.txt created" )
            
            
if __name__=="__main__":
    create_requirements()



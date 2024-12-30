# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 08:46:30 2023

@author: johnp
"""

import os
import ctypes
from ctypes import cdll, c_int
import numpy as np

def getDist(perm):
    n = len(perm)
    return getDistRange(perm, 0, n+5)
def getDistRange(perm, min, max):
    #print("perm ", perm)
    n=len(perm)
    
    aSearch_lib = cdll.LoadLibrary('ASearch/ASearchLibrary.dll')
    
    # Declare the argument and return types for the add function
    aSearch_lib.DistForPerm.argtypes = [c_int, c_int*n, c_int, c_int, c_int*max]
    aSearch_lib.DistForPerm.restype = c_int
    
    # Test the function
    length = n
    p = perm
    IntArrayn = ctypes.c_int * n
    parameter_array = IntArrayn(*p)
    moves = np.zeros(max).astype(int)
    
    IntArrayn = ctypes.c_int * max
    move_array = IntArrayn(*moves)
    #print("BOUTA SEND")
    result = aSearch_lib.DistForPerm(length, parameter_array, min, max, move_array)
    
    #print(f"{length} + {p} = {result}")
    #finalMoves = np.array(move_array)
    #print(f"moves: {finalMoves}")
    return result
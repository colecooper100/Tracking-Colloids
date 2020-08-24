# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 14:27:50 2020

@author: colec
"""

import trackpy as tp
from muvi.readers.vti import VTIMovie

#%%

vm = VTIMovie(r'Z:\Cole\Cine convert/test4.vti')
features = tp.locate(vm[0], diameter=(5, 9, 9))


#%%




























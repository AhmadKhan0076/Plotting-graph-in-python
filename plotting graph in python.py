# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:29:17 2022

@author: DELL
"""

import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,40)
d_r=1*t
d_s=3*(t-30)
fig,ax=plt.subplots()
plt.xlabel('Days')
plt.ylabel('Energy generated')
ax.set_xlim(0,50)
ax.set_ylim(0,50)
ax.plot(t,d_r,c='red')
ax.plot(t,d_s,c='black')
plt.axvline(x=40,color='purple',linestyle="--")
_= plt.axhline(y=40,color='purple',linestyle="--")





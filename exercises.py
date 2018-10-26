#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:36:13 2018

@author: nataliecedeno
"""
#%%
def linear_search(lst,number):
    for i in range(len(lst)):
        if lst[i] == number:
            return i
    return None
#%%

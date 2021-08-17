# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 19:46:17 2021

@author: mgune
"""

"Bir listeyi düzleştiren (flatten) fonksiyon"

a=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def flatten_func(x):
    for i in x:
        if not isinstance(i, list):
            yield i
        else:
            for k in flatten_func(i):
                yield k

output=list(flatten_func(a))

#%%


"Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon"

b=[[1, 2], [3, 4], [5, 6, 7]]
def reverse_list_elements(x):
    for i in x:
        i.reverse()
    return x[::-1]
output2=reverse_list_elements(b)
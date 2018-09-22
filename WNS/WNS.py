#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 02:53:07 2018

@author: shubh
"""
import pandas as pd

df = pd.read_csv('data/WNS/train.csv')
df.describe()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 02:23:41 2018

@author: shubh
"""
from plotnine import *

def scatter(df,x,y):
    p = ggplot(df,aes(x,y))+\
    geom_point()+\
    labs(x=x,y=y)
    
    return p 
    
def hist(df,y,bins):
    df = df.dropna(axis=0)
    p = ggplot(df,aes(y))+\
    geom_histogram(color='white',bins=bins)+\
    labs(y=y)+\
    theme_light()
    
    return p 

def boxplot(df,y):
    p = ggplot(df,aes(1,y))+\
    geom_boxplot()+\
    labs(x=y,y='Value')+\
    theme_light()+\
    theme(axis_text_x = element_blank())   
    
    return p 

def density(df,y):
    p = ggplot(df,aes(y))+\
    geom_density(fill='lightblue')+\
    labs(x=y)+\
    theme_light()
    
    return p 

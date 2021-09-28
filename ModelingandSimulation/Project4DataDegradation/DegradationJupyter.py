#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Shelby Clow and Austin Johns
# CST-305
# Project 4: Degradation of Data Integrity
# Blur of an image to represent image quality degradation. 

# import necessary packages for image work and ODE use
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint
from PIL import Image
from PIL import ImageFilter


# In[2]:


# Open the original image
im = Image.open(r"C:\Users\shelb\Documents\GCU\Summer 2020\CST-305\corgi.jpg") 
px = im.load()
# Printing pixel quality of the original image
print("Original image pixels: ")
print(px[4, 4]) 
px[4, 4] = (0, 0, 0) 
# find quality of the image at specific coordinate (1500,1300)
coordinate = x, y = 1500, 1300
impixel = im.getpixel(coordinate)
print("Original image pixels at coordinate (1500, 1300): ")
print(impixel)


# In[3]:


# Apply blur to original image
blurIm = im.filter(ImageFilter.GaussianBlur(radius = 20))
px2 = blurIm.load() 
# Printing new image quality
print("Blurred image pixels: ")
print(px2[4, 4]) 
px2[4, 4] = (0, 0, 0) 
# Finding the quality at specific coordinate (1500,1300)
coordinate2 = x2, y2 = 1500, 1300
blurImpixel = blurIm.getpixel(coordinate2)
print("Blurred image pixels at coordinate (1500, 1300): ")
print(blurImpixel)


# In[4]:


# ODE to represent exponential decay
def model(xt, t):
    return -1*a*xt


# In[5]:


# Change of image quality found from image quality comparison
a = 0.0559
xt = (161, 173)
t = np.linspace(0, 120)
y = odeint(model, xt, t)

# Plot the graph to show image quality degradation
plt.plot(t, y)
plt.title("Image Quality Degradation")
plt.xlabel("Time")
plt.ylabel("Data Degradation")
plt.show()


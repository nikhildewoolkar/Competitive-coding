#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    c=[]
    for i in range(len(word)):
        c.append(h[a.index(word[i])])
    print(max(c)*len(c))
h = list(map(int, input().rstrip().split()))
word = input()
result = designerPdfViewer(h, word)

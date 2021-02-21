#!/bin/python3

import math
import os
import random
import re
import sys
def bomberMan(n, grid):
    if(n==1):
        for i in grid:
            print(''.join(i))
        return
    if(n%2==0):
        s='O'*c
        for i in range(r):
            print(s)
        return
    else:
        for z in range(3,n+1,2):  
            for i in range(r):
                for j in range(c):
                    if(grid[i][j]=="."):
                        grid[i][j]="1"       
            for i in range(r):
                for j in range(c):
                    if(grid[i][j]=="O"):
                        grid[i][j]='.'
                        if(i-1>=0 and grid[i-1][j]!="O"):
                            grid[i-1][j]='.'
                        if(i+1<r and grid[i+1][j]!="O"):
                            grid[i+1][j]='.'
                        if(j-1>=0 and grid[i][j-1]!="O"):
                            grid[i][j-1]='.'
                        if(j+1<c and grid[i][j+1]!="O"):
                            grid[i][j+1]='.'
            for i in range (r):
                for j in range(c):
                    if(grid[i][j]=="1"):
                        grid[i][j]="O"
        for i in grid:
            print(''.join(i))

rcn = input().split()
r = int(rcn[0])
c = int(rcn[1])
n = int(rcn[2])
grid = []
for _ in range(r):
    grid_item = list(input())
    grid.append(grid_item)
bomberMan(n, grid)



































"""#!/bin/python3

import math
import os
import random
import re
import sys
def bomberMan(n, grid):
    if(n==1):
        for i in grid:
            print(''.join(i))
        return
    if(n%2==0):
        s='O'*c
        # print(s)
        for i in range(r):
            print(s)
        return
    else:
        gri=[]
        for z in range(3,n+1,2):
            gri=[]
            for j in range(r):
                g1=[u.replace(".","1") for u in grid[j]]
                # print("g1",g1)
                gri.append(g1)
            grid=[]
            grid=gri.copy()
            # for i in grid:
            #     print(''.join(i))            
            for i in range(r):
                for j in range(c):
                    if(grid[i][j]=="O"):
                        grid[i][j]='.'
                        if(i-1>=0 and grid[i-1][j]!="O"):
                            grid[i-1][j]='.'
                        if(i+1<r and grid[i+1][j]!="O"):
                            grid[i+1][j]='.'
                        if(j-1>=0 and grid[i][j-1]!="O"):
                            grid[i][j-1]='.'
                        if(j+1<c and grid[i][j+1]!="O"):
                            grid[i][j+1]='.'
            # for i in grid:
            #     print(''.join(i))
            gri=[]
            for j in range(r):
                g=[i.replace("1","O") for i in grid[j]]
                # g1=[u.replace(".","1") for u in g]
                gri.append(g)
            gri1=[]
            gri1=gri.copy()
            # print("yayay")


            grid=[]
            grid=gri.copy()
            # for i in grid:
            #     print(''.join(i))

        for i in gri:
            print(''.join(i))







# Complete the bomberMan function below.
# def bomberMan(n, grid):
#     gri1=grid.copy()
#     for z in range(1,n+1):

#             # for i in gri:
#             #     print(*i)

#         if(z%3==1):
#             # for j in range(r):
#             #     g=[i.replace("1",".") for i in grid[j]]
#             #     # g=[i.replace("1","O") for i in grid[j]]
#             #     # g1=[u.replace(".","1") for u in g]
#             #     gri1.append(g)
#             print("pppp")
#             for i in gri1:
#                 print(*i)
#         elif(z%3==2):
#             for i in range(r):
#                 for j in range(c):
#                     print("O",end=' ')
#                 print("\n")
#             # print("intermediate grid",z)
#             # for i in grid:
#             #     print(*i)
#         elif(z%3==0):
#             gri=[]
#             for j in range(r):
#                 # g=[i.replace("1","O") for i in grid[j]]
#                 g1=[u.replace(".","1") for u in grid[j]]
#                 gri.append(g1)
#             grid=gri.copy()
#             for i in range(r):
#                 for j in range(c):
#                     if(grid[i][j]=="O"):
#                         grid[i][j]='.'
#                         if(i-1>=0 and grid[i-1][j]!="O"):
#                             grid[i-1][j]='.'
#                         if(i+1<r and grid[i+1][j]!="O"):
#                             grid[i+1][j]='.'
#                         if(j-1>=0 and grid[i][j-1]!="O"):
#                             grid[i][j-1]='.'
#                         if(j+1<c and grid[i][j+1]!="O"):
#                             grid[i][j+1]='.'

#             gri=[]
#             for j in range(r):
#                 g=[i.replace("1","O") for i in grid[j]]
#                 # g1=[u.replace(".","1") for u in g]
#                 gri.append(g)
#             gri1=gri.copy()
#             print("yayay")
#             for i in gri:
#                 print(*i)                   


rcn = input().split()
r = int(rcn[0])
c = int(rcn[1])
n = int(rcn[2])
grid = []
for _ in range(r):
    grid_item = list(input())
    # g=[i.replace(".","1") for i in grid_item]
    grid.append(grid_item)
result=bomberMan(n, grid)
# bomberMan(n, result)'''import math
import os
import random
import re
import sys
def bomberMan(n, grid,gri):
    gri1=grid.copy()
    for z in range(1,n+1):
        if(z%3==1):
            # for j in range(r):
            #     g=[i.replace("1",".") for i in grid[j]]
            #     gri1.append(g)
            for i in gri1:
                print(*i)
            print("gri1 complete z",z)
            
                
        elif(z%3==2):
            for i in range(r):
                for j in range(c):
                    print("O",end=' ')
                print("\n")
            print("z complete",z)

        elif(z%3==0):
            grid=gri.copy()
            for i in range(r):
                for j in range(c):
                    if(grid[i][j]=="O"):
                        grid[i][j]='.'
                        if(i-1>=0 and grid[i-1][j]!="O"):
                            grid[i-1][j]='.'
                        if(i+1<r and grid[i+1][j]!="O"):
                            grid[i+1][j]='.'
                        if(j-1>=0 and grid[i][j-1]!="O"):
                            grid[i][j-1]='.'
                        if(j+1<c and grid[i][j+1]!="O"):
                            grid[i][j+1]='.'
            gri=[]
            for i in grid:
                print(*i)                   
            print("grid complete")
            for j in range(r):
                g=[i.replace("1","O") for i in grid[j]]
                g1=[u.replace("1",".") for u in g]
                gri.append(g1)
            gri1=gri.copy()
            for i in gri:
                print(*i)
            print("gri complete")
            for i in gri1:
                print(*i)
            print("gri1 complete")            


rcn = input().split()
r = int(rcn[0])
c = int(rcn[1])
n = int(rcn[2])
grid = []
gri=[]
for _ in range(r):
    grid_item = list(input())
    g=[i.replace(".","1") for i in grid_item]
    gri.append(g)
    grid.append(grid_item)
result=bomberMan(n, grid,gri)"""

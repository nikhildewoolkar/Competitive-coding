#!/bin/python3

import math
import os
import random
import re
import sys

def gridSearch(G, P):
    t=0
    for i in range(len(G)):
        for j in range(len(G[i])):
            if(P[0] in G[i][j:]):
                t=G[i].index(P[0],j)
                u=i+1
                v=j
                c=0
                for k in range(1,len(P)):
                    #if(u>=len(G) or P[k] not in G[u][v:v+len(P[k])]):
                    if(u>=len(G) or P[k] not in G[u][v:] or G[u][v:].index(P[k])!=0):
                        break
                    c+=1
                    u+=1
                if(c==len(P)-1):
                    print("YES")
                    return
    print("NO")
t = int(input())
for t_itr in range(t):
    RC = input().split()
    R = int(RC[0])
    C = int(RC[1])
    G = []
    for _ in range(R):
        G_item = input()
        G.append(G_item)
    rc = input().split()
    r = int(rc[0])
    c = int(rc[1])
    P = []
    for _ in range(r):
        P_item = input()
        P.append(P_item)
    result = gridSearch(G, P)
"""
#!/bin/python3

import math
import os
import random
import re
import sys

def gridSearch(G, P):
    t=0
    for i in range(len(G)):
        
        
        for j in range(len(G[i])):
            if(P[0] in G[i][j:]):
                t=G[i].index(P[0],j)
                u=i
                v=t
                # print(u,v)
                arr=[]
                if(u+r<=R and v+c<=C):
                    for m in range(u,u+r):
                        z=""
                        for n in range(v,v+c):
                            z=z+G[m][n]
                        arr.append(z)
                    # print(arr)
                    # print(P)
                    if(arr == P):
                        print("YES")
                        return
    print("NO")

t = int(input())
for t_itr in range(t):
    RC = input().split()
    R = int(RC[0])
    C = int(RC[1])
    G = []
    for _ in range(R):
        G_item = input()
        G.append(G_item)
    rc = input().split()
    r = int(rc[0])
    c = int(rc[1])
    P = []
    for _ in range(r):
        P_item = input()
        P.append(P_item)
    result = gridSearch(G, P)
"""
"""
#!/bin/python3

import math
import os
import random
import re
import sys

def gridSearch(G, P):
    t=0
    for i in range(len(G)):
        
        
        for j in range(len(G[i])):
            if(P[0] in G[i][j:]):
                t=G[i].index(P[0],j)
                u=i
                v=t
                # print(u,v)
                arr=[]
                if(u+r<=R and v+c<=C):
                    w=0
                    x=0
                    for m in range(u,u+r):
                        z=""
                        flag=0
                        x=0
                        for n in range(v,v+c):
                            # z=z+G[m][n]
                            # print("w,x",w,x,P[w][x],G[m][n])
                            if(G[m][n]!=P[w][x]):
                                flag=1
                                break
                            x+=1
                        if(flag==1):
                            break
                            
                            # print(v,n,x,v+c)
                        # print(m,m-r)
                        # print(r)
                        # if(z!=P[w]):
                        #     flag=1
                        #     break
                        w+=1
                        # arr.append(z)
                    # print(arr)
                    # print(P)
                    if(flag==0):
                        print("YES")
                        return
    print("NO")

t = int(input())
for t_itr in range(t):
    RC = input().split()
    R = int(RC[0])
    C = int(RC[1])
    G = []
    for _ in range(R):
        G_item = input()
        G.append(G_item)
    rc = input().split()
    r = int(rc[0])
    c = int(rc[1])
    P = []
    for _ in range(r):
        P_item = input()
        P.append(P_item)
    result = gridSearch(G, P)
    """

from collections import Counter,defaultdict,deque
import itertools #product
import math
import sys

sys.setrecursionlimit(10**6)

import time

#3つ受け取り
h,w,n=map(int,input().split())
l=[]
l.append(['.']*(w+2))
for i in range(h):
    tmp=input().split()
    tmp.append('.')
    tmp.insert(0,'.')
    l.append(tmp)
l.append(['.']*(w+2))
#移動のための配列
dy=[0,1,0,-1]
dx=[1,0,-1,0]
#一応退避
dydy=dy
dxdx=dx
#この回数だけ回す
for i in range(n):
    a,b,c,d=map(int,input().split())
    flg=False
    moji=l[a][b]
    y,x=a,b
    for j in range(20):
        y+=dy[0]
        x+=dx[0]        
        if y<0 or y>h+1 or x<0 or x>w+1:
            break
        if l[y][x]=='.':
            yy=y
            xx=x
            for k in range(20):
                yy+=dy[3]
                xx+=dx[3]
                if yy<0 or yy>h+1 or xx<0 or xx>w+1:
                    break
                if l[yy][xx]=='.':
                    yyy=yy
                    xxx=xx
                    for v in range(20):
                        yyy+=dy[0]
                        xxx+=dx[0]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                    yyy=yy
                    xxx=xx
                    for vv in range(20):
                        yyy+=dy[2]
                        xxx+=dx[2]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                if l[yy][xx]=='.':
                    continue
                elif l[yy][xx]==moji:
                    if yy==c and xx==d:
                        flg=True
                    else:
                        break
                else:
                    break
            yy=y
            xx=x
            for k in range(20):
                yy+=dy[1]
                xx+=dx[1]
                if yy<0 or yy>h+1 or xx<0 or xx>w+1:
                    break
                if l[yy][xx]=='.':
                    yyy=yy
                    xxx=xx
                    for v in range(20):
                        yyy+=dy[0]
                        xxx+=dx[0]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                    yyy=yy
                    xxx=xx
                    for vv in range(20):
                        yyy+=dy[2]
                        xxx+=dx[2]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                if l[yy][xx]=='.':
                    continue
                elif l[yy][xx]==moji:
                    if yy==c and xx==d:
                        flg=True
                    else:
                        break
                else:
                    break            
        if l[y][x]=='.':
            continue
        elif l[y][x]==moji:
            if y==c and x==d:
                flg=True
            else:
                break
        else:
            break
    y,x=a,b
    for j in range(20):
        y+=dy[2]
        x+=dx[2]
        if y<0 or y>h+1 or x<0 or x>w+1:
            break
        if l[y][x]=='.':
            yy=y
            xx=x
            for k in range(20):
                yy+=dy[3]
                xx+=dx[3]
                if yy<0 or yy>h+1 or xx<0 or xx>w+1:
                    break
                if l[yy][xx]=='.':
                    yyy=yy
                    xxx=xx
                    for v in range(20):
                        yyy+=dy[0]
                        xxx+=dx[0]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                    yyy=yy
                    xxx=xx
                    for vv in range(20):
                        yyy+=dy[2]
                        xxx+=dx[2]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                if l[yy][xx]=='.':
                    continue
                elif l[yy][xx]==moji:
                    if yy==c and xx==d:
                        flg=True
                    else:
                        break
                else:
                    break
            yy=y
            xx=x
            for k in range(20):
                yy+=dy[1]
                xx+=dx[1]
                if yy<0 or yy>h+1 or xx<0 or xx>w+1:
                    break
                if l[yy][xx]=='.':
                    yyy=yy
                    xxx=xx
                    for v in range(20):
                        yyy+=dy[0]
                        xxx+=dx[0]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                    yyy=yy
                    xxx=xx
                    for vv in range(20):
                        yyy+=dy[2]
                        xxx+=dx[2]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                if l[yy][xx]=='.':
                    continue
                elif l[yy][xx]==moji:
                    if yy==c and xx==d:
                        flg=True
                    else:
                        break
                else:
                    break            
        if l[y][x]=='.':
            continue
        elif l[y][x]==moji:
            if y==c and x==d:
                flg=True
            else:
                break
        else:
            break
    y,x=a,b
    for j in range(20):
        y+=dy[3]
        x+=dx[3]
        if y<0 or y>h+1 or x<0 or x>w+1:
            break
        if l[y][x]=='.':
            yy=y
            xx=x
            for k in range(20):
                yy+=dy[0]
                xx+=dx[0]
                if yy<0 or yy>h+1 or xx<0 or xx>w+1:
                    break
                if l[yy][xx]=='.':
                    yyy=yy
                    xxx=xx
                    for v in range(20):
                        yyy+=dy[3]
                        xxx+=dx[3]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                    yyy=yy
                    xxx=xx
                    for vv in range(20):
                        yyy+=dy[1]
                        xxx+=dx[1]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                if l[yy][xx]=='.':
                    continue
                elif l[yy][xx]==moji:
                    if yy==c and xx==d:
                        flg=True
                    else:
                        break
                else:
                    break
            yy=y
            xx=x
            for k in range(20):
                yy+=dy[2]
                xx+=dx[2]
                if yy<0 or yy>h+1 or xx<0 or xx>w+1:
                    break
                if l[yy][xx]=='.':
                    yyy=yy
                    xxx=xx
                    for v in range(20):
                        yyy+=dy[3]
                        xxx+=dx[3]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                    yyy=yy
                    xxx=xx
                    for vv in range(20):
                        yyy+=dy[1]
                        xxx+=dx[1]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                if l[yy][xx]=='.':
                    continue
                elif l[yy][xx]==moji:
                    if yy==c and xx==d:
                        flg=True
                    else:
                        break
                else:
                    break            
        if l[y][x]=='.':
            continue
        elif l[y][x]==moji:
            if y==c and x==d:
                flg=True
            else:
                break
        else:
            break
    y,x=a,b
    for j in range(20):
        y+=dy[1]
        x+=dx[1]
        if y<0 or y>h+1 or x<0 or x>w+1:
            break
        if l[y][x]=='.':
            yy=y
            xx=x
            for k in range(20):
                yy+=dy[0]
                xx+=dx[0]
                if yy<0 or yy>h+1 or xx<0 or xx>w+1:
                    break
                if l[yy][xx]=='.':
                    yyy=yy
                    xxx=xx
                    for v in range(20):
                        yyy+=dy[3]
                        xxx+=dx[3]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                    yyy=yy
                    xxx=xx
                    for vv in range(20):
                        yyy+=dy[1]
                        xxx+=dx[1]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                if l[yy][xx]=='.':
                    continue
                elif l[yy][xx]==moji:
                    if yy==c and xx==d:
                        flg=True
                    else:
                        break
                else:
                    break

            yy=y
            xx=x
            for k in range(20):
                yy+=dy[2]
                xx+=dx[2]
                if yy<0 or yy>h+1 or xx<0 or xx>w+1:
                    break
                if l[yy][xx]=='.':
                    yyy=yy
                    xxx=xx
                    for v in range(20):
                        yyy+=dy[3]
                        xxx+=dx[3]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                    yyy=yy
                    xxx=xx
                    for vv in range(20):
                        yyy+=dy[1]
                        xxx+=dx[1]
                        if yyy<0 or yyy>h+1 or xxx<0 or xxx>w+1:
                            break
                        if l[yyy][xxx]=='.':
                            continue
                        elif l[yyy][xxx]==moji:
                            if yyy==c and xxx==d:
                                flg=True
                            else:
                                break
                        else:
                            break
                if l[yy][xx]=='.':
                    continue
                elif l[yy][xx]==moji:
                    if yy==c and xx==d:
                        flg=True
                    else:
                        break
                else:
                    break            
        if l[y][x]=='.':
            continue
        elif l[y][x]==moji:
            if y==c and x==d:
                flg=True
            else:
                break
        else:
            break
    if flg:
        print('yes')
    else:print('no')

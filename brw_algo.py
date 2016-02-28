# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:27:35 2016

@author: Vasu
"""
"""
This is the programatic solution for a whatsapp brain stroming question!!!!
i was just thought to implement it out in programm to give the solution.
here is the problem and below is the solution :)

problem:

last digt of 3 same number should is the sum of these 3 numbers
i call this brw-circle algorithem as the problem was showen to me as first digit in blue circle
second as red circle and 3rd as white. and result should be white 3 digit color

i tried this for 5 digit numbers
solution is NULL :( 

+#*
+#*
+#*
---
***

sum of the 3 number ("+#*" is one number)  should be match with the last digit of number

"""
def permuThree():
    threeList=[[i,j,k] for i in range(0,10) for j in range(0,10) for k in range(0,10) if not i==j==k]
    #resuList=[] 
    resulDict={}
    for b in threeList:
        s=""
        for a in b:
            s=s+str(a)
        resulDict[s]=str(int(s)*3)
    return resulDict

def permuFive():
    fiveList=[[i,j,k] for i in range(0,10) for j in range(0,10) for k in range(0,10) for l in range(0,10) for m in range(0,10)if not i==j==k==l==m]
    #resuList=[] 
    resulDict={}
    for b in fiveList:
        s=""
        for a in b:
            s=s+str(a)
        resulDict[s]=str(int(s)*5)
    return resulDict

def checkLen(n):
    r1=permuThree()
    for i in r1:
        if len(r1[i])==n:
            temp=i[-1]
            count=0
            for j in range(0,n):
                #if i[-1] == r1[i][0] and i[-1] == r1[i][1] and i[-1] == r1[i][2]:
                #count=0
                if temp==r1[i][j]:
                    count=count+1
            if count==n:        
                print (i,r1[i])

checkLen(5)


    
def t(s):
    n=0
    for i in s:
        n += ord(i)-ord('0')
    return str(n)
if __name__ =='__main__':
    s=input()
    cnt=0
    while(len(s)>1):
        s=t(s)
        cnt+=1
    print(cnt)

#                --------            --------             ---------
#                -        -        -          -          -
#                -         -      -            -        -
#               ----       -      -            -        -
#                -         -      -         -  -        -
#                -        -        -          -          -
#                --------            --------   -          ---------
## Functions

## Square

def sqr (patternchar, length):
    for x in range (length):
        for y in range (length):
            print(patternchar, end="")
        print()

## Right angle triangle

def right (patternchar, length):
    for x in range (1, (length+1)):
        for y in range (1, (length+1)):
            if(y <= x):
                print(patternchar, end="")
        print()

## Right angle triangle (Flipped)

def rightflp (patternchar, length):
    for x in range (1, (length+1)):
        for y in range (1, (length+1)):
            if(x <= y):
                print(patternchar, end="")
        print()

## Right angle triangle (Inverted)

def rightinv (patternchar, length):
    for x in range (1, (length+1)):
        for y in range (1, (length+1)):
            if(y < x):
                print(" ", end="")
            if(y >= x):
                print(patternchar, end="")
        print()

## Pyramid

def pyramid (patternchar, length):
    for x in range(1,(length+1)):
        for y in range((length+1),x,-1):
            print(" ",end="")
        for z in range(1,x*2):
            print(patternchar, end="")
        print()
    return

## Pyramid (Inverted)

def pyramidinv (patternchar, length):
    for x in range(1,(length+1)):
        for y in range(1,x+1):
            print(" ",end="")
        for z in range(x,(length*2+1)-x):
            print(patternchar, end="")
        print()
    return

## Diamond

def diamond (patternchar, length):
    for x in range(1,(length+1)):
        for y in range((length+1),x,-1):
            print(" ",end="")
        for z in range(1,x*2):
            print(patternchar, end="")
        print()
    for a in range(2,(length+1)):
        for b in range(1,a+1):
            print(" ",end="")
        for c in range(a,(length*2+1)-a):
            print(patternchar, end="")
        print()
    return

## Hourglass

def hrglass (patternchar, length):
    for a in range(1,(length+1)):
        for b in range(1,a+1):
            print(" ",end="")
        for c in range(a,(length*2+1)-a):
            print(patternchar, end="")
        print()
    for x in range(2,(length+1)):
        for y in range((length+1),x,-1):
            print(" ",end="")
        for z in range(1,x*2):
            print(patternchar, end="")
        print()
    return

## Wings

def wings (patternchar, length):
    for a in range(1,(length+1)):
        for b in range(1,a+1):
            print(patternchar, end="")
        for c in range(a,(length*2+1)-a):
            print(" ",end="")
        for d in range(1,a+1):
            print(patternchar, end="")
        print()
    for x in range(2,(length+1)):
        for y in range((length+1),x,-1):
            print(patternchar, end="")
        for z in range(1,x*2):
            print(" ",end="")
        for q in range((length+1),x,-1):
            print(patternchar, end="")
        print()
    return

## Xmas Tree

def xmastree (patternchar, length):
    for x in range(1,(length+1)):
        for y in range((length),x,-1):
            print(" ",end="")
        for z in range(1,x*2):
            print(patternchar, end="")
        print()
    for a in range(1,(length)):
        for b in range(1,((length*2)-(length+1))):
            print(" ",end="")
        for c in range(1,4):
            print(patternchar," ", end="")
        print()
    return

## Heart

def heart (patternchar, length):
    n=length//2
    for a in range(1,n):
        for b in range(n,a,-1):
            print(" ",end="")
        for c in range(0,a*2):
            print(patternchar, end="")
        for d in range(a,(n*2+1)-a):
            print(" ",end="")
        for e in range(0,a*2):
            print(patternchar, end="")   
        print()
    if(length%2==0):
        for x in range(1,length+1):
            for y in range(1,x+1):
                print(" ",end="")
            for z in range(x,(length*2+1)-x):
                print(patternchar, end="")
            print()
    else:
        for x in range(2,length+1):
            for y in range(2,x+1):
                print(" ",end="")
            for z in range(x,(length*2+1)-x):
                print(patternchar, end="")
            print()
    return

rightinvflp ("*", 7)
rightinv ("*", 7)
## The above patterns are developed and updated by Animesh and Shiwani

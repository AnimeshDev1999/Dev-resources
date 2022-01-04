## Initalization

pat = input("Input the pattern character")
length = int(input("Input the length of the pattern"))

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

## Right angle triangle (Inverted, Flipped)

def rightinvflp (patternchar, length):
    for x in range (1, (length+1)):
        for y in range (1, (length+1)):
            if(x < y):
                print(patternchar, end="")
            if(x >= y):
                print(" ", end="")
        print()

## Condition

righinvtpat(pat, length)

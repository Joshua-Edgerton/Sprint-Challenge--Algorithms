#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(1)
Reasoning: Seems simple. "a" will always be less than "n"

b)
O(n^2)
Reasoning: While loop nested in for loop. when "n" increases, it also increases the amount of times its looped through

c)
O(2^n)
Reasoning: This function is recursive and seems to double itself after each step

## Exercise II

I would have a function that take in paramaters of the "height"(the height of the building) and "floor"(the floor that an egg will break)
"if" the floor was less than or equal to the height -
    and "if" the floor equalled "0" then return that floor - 
    otherwise I would return that function again, taking the same height and floor minus 1

def egg_break(height, floor):
    if floor <= height:
        if floor == 0:
            return floor
        
        return egg_break(height, floor - 1)
    
I believe this would be O(2^n) due to recursion



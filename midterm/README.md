# AP4063 Midterm TA Solution

```py
def four_piles(n, y):
    piles = []
    
    for x in range(1, n):
        if (
            x + y > 0 and 
            x - y > 0 and 
            x * y > 0 and 
            x % y == 0 and 
            x // y > 0
        ):
            if n == (x + y) + (x - y) + (x * y) + (x // y):
                piles = [
                    (x + y),
                    (x - y),
                    (x * y),
                    (x // y)
                ]
                return piles
    
    return piles
```
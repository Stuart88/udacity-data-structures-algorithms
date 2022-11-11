

"""

The solution to this problem uses binary search logic. 
First it handles the trivial cases for num = 0, 1, 2, 4, 5 by giving a manual numeric result.

For num > 5, we can use the following:

    root(num) > num/2

This allows us to start the binary search in the range 0 < n < num/2,
which gives a small boost in efficiency.

The results are handled via a SqrtResult class, which has been designed
for testing the effiency of the search.

Time complexity: O(logn), same as binary search

Space complexity: 1, since there is no array traversal.

"""

class SqrtResult:
    def __init__(self, root, cycles, number) -> None:
        self.number = number # The number being square-rooted
        self.root = root # The answer
        self.cycles = cycles # The amount of loop cycles it took to find the solution
    def __str__(self) -> str:
        return f'Root {self.number} is {self.root} and took {self.cycles} cycles'
    

def sqrt_calc(number: int) -> SqrtResult:
    
    if number < 5:
        raise Exception('The given number should be higher than 5!')

    # For number > 5, square root is always less than half of the number,
    # so we can use that as our start point
    max_i = number // 2  
    min_i = 0
    
    # Start by checking mid-point of range
    n = max_i // 2

    val = n * n
    next_val = (n+1)*(n+1) # This will be needed to check if we've hit the floor

    # This is to track performance of the loop below
    cycles = 1
    
    while val != number: # if val == number, we have found our square root
        
        if val < number and next_val > number: 
            # Here we see that the next_val is higher so we know that current val is our answer
            # as the square root floor
            break
        
        if val > number:
            # value too high, so can set max_i to n
            max_i = n
        else:
            # value too low, so can set min_i to n 
            min_i = n
        
        cycles += 1

        # re-calculate n as mid-point of the new min and max values
        n = min_i + (max_i - min_i) // 2

        val = n * n
        next_val = (n+1)*(n+1)
    
    return SqrtResult(n, cycles, number)

def sqrt(number: int) -> SqrtResult:

    if number > 5:
        return sqrt_calc(number)

    # Handle trivial cases manually
    if number == 5 or number == 4:
        return SqrtResult(2, 1, number)
    if number == 3 or number == 2:
        return SqrtResult(1, 1, number)
    if number == 0 or number == 1:
        return SqrtResult(number, 1, number)

    

slowest_result = SqrtResult(0, 0, 0)

for i in range(0, 1000):
    result = sqrt(i)
    print(result)
    if result.cycles > slowest_result.cycles:
        slowest_result = result

print(f'Slowest was {slowest_result.cycles} cycles for sqrt({slowest_result.number})')

print ("Pass" if  (3 == sqrt(9).root) else "Fail")
print ("Pass" if  (0 == sqrt(0).root) else "Fail")
print ("Pass" if  (4 == sqrt(16).root) else "Fail")
print ("Pass" if  (1 == sqrt(1).root) else "Fail")
print ("Pass" if  (5 == sqrt(27).root) else "Fail")

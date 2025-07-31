
#Return: The total number of rabbit pairs that will be present after n
# months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
# rabbit pairs (instead of only 1 pair).

#F(1) = 1
#F(2) = 1


#months
n = 5 

# (each mature pair has 3 new pairs per month)
k = 3 

# F(n) = number of rabbit pairs alive in month n


#F(n) = F(n-1) + k * F(n-2)

#F(n-1) = rabbits from last month (they're still alive)

#F(n-2) = rabbits from two months ago = how many mature pairs we have now

#k * F(n-2) = new rabbits born this month

def rabbit_pairs(n, k):
    if n == 1 or n == 2:
        return 1
    return rabbit_pairs(n - 1, k) + k * rabbit_pairs(n - 2, k)

# Example usage:
print(rabbit_pairs(36, 4))  

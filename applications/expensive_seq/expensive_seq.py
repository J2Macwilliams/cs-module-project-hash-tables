# instantiate cache
my_cache = {}

def expensive_seq(x, y, z):
    # set up the key as a tuple of the variables
    key = (x, y, z)
    # base case
    if x <= 0: 
        return y + z
    if key in my_cache:
        return my_cache[key]
    if x >  0: 
        my_cache[key] = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
    return my_cache[key]



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))

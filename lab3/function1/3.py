
def solve(numheads, numlegs):
    chicken = (4 * numheads - numlegs)/2
    rabbit = numheads - chicken
    print(f'Chickens - {int(chicken)} and Rabbits - {int(rabbit)}')
solve(int(input()),int(input()))    

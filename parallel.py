import multiprocessing
import numpy as np

data_pairs = [ [3,5], [4,3], [7,3], [1,6] ]

# define what to do with each data pair ( p=[3,5] ), example: calculate product 
def myfunc(p):
    product_of_list = np.prod(p)
    return product_of_list

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    result_list = pool.map(myfunc, data_pairs)
    print(result_list)

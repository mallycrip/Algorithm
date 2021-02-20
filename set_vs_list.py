import time

big_list = [i for i in range(100000000)]

_set = set(big_list)
_list = list(big_list)

if __name__ == '__main__':
    start_time = time.time()
    if 90000000 in _set: print("Hit") # 0.0s
    if 90000000 in _list: print("Hit") # 1.11s
    print(time.time() - start_time)

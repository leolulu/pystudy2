import random


def retrying_2times(func):
    def wrapper(*args, **kw):
        retry_times = 10
        while retry_times > 0:
            try:
                func(*args, **kw)
            except:
                print('error')
                retry_times -= 1
    return wrapper

@retrying_2times
def maybe_divide_by_zero(try_times):
    for _ in range(try_times):
        divide_num = random.randint(-1, 1)
        print('divide_num:', divide_num, end='\t')
        print(10 / divide_num)


if __name__ == "__main__":
    maybe_divide_by_zero(10)

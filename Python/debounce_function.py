'''

Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, 

f itself will not be called for N milliseconds.

'''

from time import sleep


def solution(N):
    T = N/ 1000
    def my_decorator(function):
        def wrapper(*args, **kwargs):
            sleep(T)
            return function(*args, **kwargs)
        return wrapper
    return my_decorator     

@solution(4000)
def f(x):
    return x  


from datetime import datetime

print(datetime.now())

print(f(200))

print(datetime.now())







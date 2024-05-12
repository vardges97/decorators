import time
def timing(func):
    def inner(*args,**kwargs):
        start = time.time()
        x = func(*args,**kwargs)
        end = time.time()
        print(f'function{func.__name__!r} started at {(start):.4f} ended at {(end):.4f}')
        return x
    return inner


import time
def timing(func):
    def inner(*args,**kwargs):
        start = time.time()
        x = func(*args,**kwargs)
        end = time.time()
        final = end - start
        print(f'function{func.__name__!r} executed in {(final):.4f}s')
        return x
    return inner


def errorhandling(func):
    def inner(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except TypeError:
            print('function encountered an error')
    return inner

def authorisation(func):
    def inner(*args,**kwargs):
        code = 1234
        id = input("enter authorised id: ")
        if id == code:
            return func(*args,**kwargs)
        else:
            print("input id does not match")
    return inner

def authorisation(func):
    def inner(*args,**kwargs):
        if isinstance((args,kwargs),int):
            return  func(*args,**kwargs)
        else:
            return ValueError
    return inner

def caching(func):
    cache = []
    def inner(*args):
        func()
        if args in cache:
            return cache[args]
        else:
            func[args] = cache[args]
        return func(*args)
    return inner



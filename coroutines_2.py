def coroutine(gen_func):
    def inner(*args, **kwargs):
        gen = gen_func(*args, **kwargs)
        gen.send(None)
        return gen
    return inner


class CustomExeption(Exception):
    pass

@coroutine
def subgen():
    while True:
        try:
            massage = yield
        except StopIteration:
            pass
        else:
            print('.'*10, massage)

@coroutine
def delegator(g):
    while True:
        try:
            data = yield
            g.send(data)
        except StopIteration:
            pass
        
        



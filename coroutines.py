def coroutine(gen_func):
    def inner(*args, **kwargs):
        gen = gen_func(*args, **kwargs)
        gen.send(None)
        return gen
    return inner


def subgen():
    # a = 'ready to accept massage'
    while True:
        massage = yield 
        print('Subgen received', massage)
        
@coroutine
def average():
    count = 0
    summ = 0
    average = None
    
    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
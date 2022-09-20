def gen(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


a = gen('beka')
a1 = gen2(5)

tasks = [a, a1]

while tasks:
    task = tasks.pop(0)
    
    try:
        i = next(task)
        print(i)
        tasks.append(task)
        
    except StopIteration:
        pass
    
import functools
import time


#@functools.lru_cache(maxsize=128, typed=False) #type是指传入实参的类型，如果传入x=9，相当于type(9)的类型
@functools.lru_cache() #此处的括号不能少，否则会出错，lru_cache有两个缺省值
def add(x, y):
    time.sleep(2)
    return x + y


@functools.lru_cache(maxsize=60)
def fib(n):
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(35))
print(fib(101)) #仍然很快，虽然超过了maxsize，但是前面的计算好了，就会清除，保留最近使用的60项


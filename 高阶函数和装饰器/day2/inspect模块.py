import inspect


# 参数注解只是友好的提醒，不是强制性的
def add(x: int, y: int = 4, *args, **kwargs) -> int:  # 参数注解是python3.5 的语法,对于x而言，如果没有写参数注解，就是说x可以是任意类型
    return x + y


# r:list = add([4], [5]) #python3.6才有的语法，变量注解。
# print(r)
# print(add('mage', 'du'))

print(add.__annotations__)  # annotations不会显示缺省值;annotations是字典
# {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}

print(add(4, 5))  # 由于字典是无序的，所以在annotations中具体x是4还是5不确定的

sig = inspect.signature(add)

print(sig, type(sig))
# (x:int, y:int=4, *args, **kwargs) -> int <class 'inspect.Signature'>

print(sig.parameters)  # OrderedDict
# OrderedDict([('x', <Parameter "x:int">), ('y', <Parameter "y:int=4">), ('args', <Parameter "*args">),
# ('kwargs', <Parameter "**kwargs">)])

print(sig.return_annotation)

print(sig.parameters['y'], type(sig.parameters['y']))
# y:int=4 <class 'inspect.Parameter'>

print(sig.parameters['x'].annotation)
# <class 'int'>

print(sig.parameters['args'])  # *args
print(sig.parameters['args'].annotation)  # <class 'inspect._empty'>
print(sig.parameters['kwargs'])
print(sig.parameters['kwargs'].annotation)

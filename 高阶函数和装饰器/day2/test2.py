import inspect


def add(x, y: int=7, *args, z, t=10, **kwargs) -> int:
    return x + y


sig = inspect.signature(add)
print(sig)
print(sig.parameters)
print(sig.return_annotation)
print('~~~~~~~~~~~~~~~~~~~~~~~')
for i, item in enumerate(sig.parameters.items()):
    name, param = item
    print(i + 1, param.annotation, param.kind, param.default)
    print(param.default is param.empty, end='\n\n')

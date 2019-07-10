
class Person:
    def __del__(self):
        print('del')


t = Person()
t.__del__()
t.__del__()
t.__del__()
t.__del__()
t.__del__()
print('11111111111111111')
t1 = t
t2 = t1

del t
print('22222222222222222')
del t2
print('33333333333333333')
# del t1
print('44444444444444444')

print('~~~~~~~~~~~~~~~~~~')

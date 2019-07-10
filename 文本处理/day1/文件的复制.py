"""指定一个源文件，实现copy到目标文件

"""
import shutil

fn1 = 'c:/test1.txt'
fn2 = 'c:/test2.txt'

with open(fn1, 'w') as f:
    f.writelines('\n'.join(['abc', '123', 'xyz']))

with open(fn1, 'rb') as f1:
    with open(fn2, 'wb') as f2:
        length = 16 * 1024
        while True:
            buf = f1.read(length)
            if not buf:
                break
            f2.write(buf)

with open(fn1, 'rb') as f1:
    with open(fn2, 'wb') as f2:
        shutil.copyfileobj(f1, f2)

shutil.copyfile(fn1, fn2)
shutil.copy(fn1, fn2)
shutil.copy2(fn1, fn2)

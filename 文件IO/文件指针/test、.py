import io
import sys
from io import StringIO
from io import BytesIO


sio = StringIO()
print(sio.readable(), sio.writable(), sio.seekable())
sio.write('abc')
print(sio.read())  # 结果为空，因为写入后，文件指针在EOF
sio.seek(0)  # 将文件指针调整到文件开头
print(sio.read())
print(sio.getvalue())  # 获取所有内容，跟文件指针没有关系
sio.close()

bio = BytesIO()
print(bio.readable(), bio.writable(), bio.seekable())
bio.write(b'abc')
print(bio.read())  # 结果为空，因为写入后，文件指针在EOF
bio.seek(0)  # 将文件指针调整到文件开头
print(bio.read())
bio.close()

with io.StringIO() as f:
    print(f.readable(), f.writable(), f.seekable())
    print(f.fileno())  # 输出文件描述符——>会出错，因为你文件根本就没落地

# file-like类文件对象
f = sys.stdout
f.write('xyz')
sys.stderr.write('xyz')

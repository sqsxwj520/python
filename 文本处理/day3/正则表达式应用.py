
import re

s = """ftp://ftp.astron.com/pub/file/file-5.14.tar.gz
ftp://ftp.gmplib.org/pub/gmp-5.1.2/gmp-5.1.2.tar.xz
ftp://ftp.vim.org/pub/vim/unix/vim-7.3.tar.bz2
http://anduin.linuxfromscratch.org/sources/LFS/lfs-packages/conglomeration//iana-etc/iana-etc-
2.30.tar.bz2
http://anduin.linuxfromscratch.org/sources/other/udev-lfs-205-1.tar.bz2
http://download.savannah.gnu.org/releases/libpipeline/libpipeline-1.2.4.tar.gz
http://download.savannah.gnu.org/releases/man-db/man-db-2.6.5.tar.xz
http://download.savannah.gnu.org/releases/sysvinit/sysvinit-2.88dsf.tar.bz2
http://ftp.altlinux.org/pub/people/legion/kbd/kbd-1.15.5.tar.gz
http://mirror.hust.edu.cn/gnu/autoconf/autoconf-2.69.tar.xz
http://mirror.hust.edu.cn/gnu/automake/automake-1.14.tar.xz
"""

# result = s.split()
# for x in result:
#     if 'ftp' in x and (x.endswith('gz') or x.endswith('xz')):
#         print(x.rsplit('/', 1)[1])

regex = re.compile('.*ftp.*[gz|xz]$', re.M)
r = regex.findall(s)
print(r)
for x in r:
    print(re.split('[/]', x)[-1])

t = """<a href='http://www.magedu.com/index.html' target='_blank'>马哥教育</a>"""
r = re.findall('>(\w+)<', t)
print(r[0])

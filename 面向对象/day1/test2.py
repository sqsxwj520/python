"""实现Base64解码"""
import re
base_tbl = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
alphabet = dict(zip(base_tbl, range(64)))  # 改为字典，会提高效率

pattern = b'[A-Za-z\d+/]{2,4}={0,2}'

regex = re.compile(pattern)


def base64decode(src: bytes):
    ret = bytearray()
    length = len(src)

    if length % 4 != 0:
        return
    step = 4
    for offset in range(0, length, step):
        end = offset + step
        block = src[offset: end]
        if end == length:  # 最后四个字符
            m = regex.fullmatch(block)  # 只有末尾出现等号，切最多为两个等号，才能匹配到
            if m is None:  # 匹配不到
                return
        tmp = 0
        for i, c in enumerate(reversed(block)):  # reversed没有效率的问题
            index = alphabet.get(c)  # find的效率偏低，改为字典会提高效率

            if index:  # 0没有影响，因为0左移多少位还是0
                tmp += index << i * 6
            elif index == 0:  # 0不需要移位
                pass
            else:
                if end != length:  # 判断是否到了末尾的四个字符；没到末尾四个字符，出现非法字符；
                    return
        # print(tmp, hex(tmp))
        ret.extend(tmp.to_bytes(3, 'big'))  # 3表示字节数

    return bytes(ret)


print(base64decode(b'YWJj'))
print(base64decode(b'YW=*=Jj='))  # 不是在末尾，出现了非法字符

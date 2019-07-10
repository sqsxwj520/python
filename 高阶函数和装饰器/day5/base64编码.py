
"""实现base64编码"""

alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def b64encode(src: str):
    ret = bytearray()

    if isinstance(src, str):
        _src = src.encode()  # bytes
    else:
        return

    length = len(_src)
    for offset in range(0, length, 3):
        triple = _src[offset: offset + 3]
        # print(triple)

        r = 3 - len(triple)
        if r:
            triple += b'\x00' * r
        # print(triple)

        # 一定会有三个字节
        x = int.from_bytes(triple, 'big')  # 大端模式

        for i in range(18, -1, -6):
            index = x >> i & 0x3F  # 与63位与运算
            ret.append(alphabet[index])
        # print(ret)
        # for i in range(r):
        #     ret[-i - 1] = 61  # 61为十进制的，对应的ASCII码为‘=’
        if r:
            ret[-r:] = b'=' * r
    return bytes(ret)


print(b64encode("教育a"))

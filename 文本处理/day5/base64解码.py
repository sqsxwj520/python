alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def b64decode(src: str):  # base64解码函数
    ret = bytearray()
    if isinstance(src, str):
        _src = src.encode()
    else:
        return

    length = len(_src)
    for offset in range(0, length, 4):
        tmp = 0
        f = _src[offset: offset + 4]

        for i, c in enumerate(reversed(f)):
            index = alphabet.find(c)
            if index == -1:
                continue
            tmp += index << i * 6
        ret.extend(tmp.to_bytes(3, 'big'))
    return bytes(ret.rstrip(b'\x00'))


print(b64decode('5pWZ6IKyYQ==').decode())

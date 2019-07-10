#
# alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
#
# def base64decode(src):
#
#     length = len(src)
#
alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def base64decode(src):
    ret = bytearray()
    length = len(src)
    step = 4  # 对齐的，每次取4个
    for offset in range(0, length, step):
        tmp = 0x00
        block = src[offset:offset + step]
        # 反查表，从字符到index a YQ==
        for i, c in enumerate(reversed(block)):
            index = alphabet.find(c)
            if index == -1:
                continue  # 找不到说明是=，就是0，不用移位相加了
            tmp += index << i * 6
        ret.extend(tmp.to_bytes(3, 'big'))

    return bytes(ret)


# base64的decode
# txt = "TWFu"
# txt = "TWE="
# txt = "TQ=="
txt = "TWFuTWE="
# txt = "TWFuTQ=="
txt = txt.encode()
print(txt)
print(base64decode(txt).decode())

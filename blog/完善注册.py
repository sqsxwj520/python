import jwt
import base64
import simplejson
from jwt import algorithms


SECRET_KEY = 'k*)_*v2%04niq0#5xc6fkl@p0pqjn2=hrm^yw3vdxloom2v7+2'
payload = {
    'user': 'sun',
    'school': 'mag'
}


def add_eq(b: bytes):
    """为base64编码补齐等号"""
    r = 4 - len(b) % 4
    return b + b'=' * r


enc = jwt.encode(payload, SECRET_KEY, algorithm="HS256")  # bytes
print(enc)

header, pd, sig = enc.split(b'.')
print(header, pd, sig, sep='\n')

print('header = ', base64.urlsafe_b64encode(header))
new_pd = base64.urlsafe_b64decode(add_eq(pd))
print('payload =', new_pd)
print(simplejson.loads(new_pd))

print('sig =', base64.urlsafe_b64encode(sig))


# 根据jwt算法重新生成签名
# 1 获取算法对象
alg = algorithms.get_default_algorithms()['HS256']
# <jwt.algorithms.HMACAlgorithm object at 0x0000000002AD1EB8> ~~~~~~~
print(alg, '~~~~~~~')
new_key = alg.prepare_key(SECRET_KEY)
print(new_key)

# 2 获取前两部分 header.payload
signing_input, _, _ = enc.rpartition(b'.')
print(signing_input)

# 3 使用key得到签名
signature = alg.sign(signing_input, new_key)
print('+++++++++++++++++++++++++++++++++++++++++++')
print(signature)
print(base64.urlsafe_b64encode(signature).decode().strip("="))
# wMJbLvqCEV2rMXwtf7ibrRVUYN4os8D00t9f-LfUFHo

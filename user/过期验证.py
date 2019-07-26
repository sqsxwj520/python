import jwt
import datetime
import threading


event = threading.Event()
SECRET_KEY = 'k*)_*v2%04niq0#5xc6fkl@p0pqjn2=hrm^yw3vdxloom2v7+2'

payload = {
    'user': 'sun',
    'school': 'mag',
    'exp': datetime.datetime.now().timestamp() + 3  # 3秒过期
}

enc = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
print(enc)

try:
    while not event.wait(1):
        x = jwt.decode(enc, SECRET_KEY, algorithms=['HS256'])
        print(x)
except Exception as e:
    print(type(e), e, '~~~~~~~~~~')
    # <class 'jwt.exceptions.ExpiredSignatureError'> Signature has expired ~~~~~~~~~~

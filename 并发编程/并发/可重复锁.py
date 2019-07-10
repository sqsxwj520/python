import threading


lock = threading.RLock()  # 可重复锁
print(lock)

print(lock.acquire())
print(lock.acquire(False))
print(lock.acquire())
print(lock.acquire(timeout=4))

lock.release()
lock.release()
lock.release()  # 还有一把锁没有释放
# lock.release()


def sub(l: threading.RLock):
    print("enter~~~~")
    print(l)
    print(threading.main_thread().ident)
    print(l.acquire())  # 锁在当前工作线程中
    print("exit~~~~~")


t = threading.Thread(target=sub, args=(lock, ))
t.start()
t.join()
# lock.release()  # 释放的是主线程的锁，但是主线程的所有锁都已经释放了，所以会报错
print("~~~~~end~~~~~")
# 注意主线程是无法释放其他线程的锁

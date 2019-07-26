from celery import Celery
import time


app = Celery('my_task')

# app的配置
app.conf.broker_url = 'redis://192.168.171.128/0'  # 0号库执行任务队列

app.conf.broker_transport_options = {'visibility_timeout': 43200}  # 过期时间为12小时 12 * 3600
app.conf.result_backend = 'redis://192.168.171.128:6379/1'  # 1号库执行结果

app.conf.update(enable_utc=True, tiemzone='Asia/Shanghai')


# @app.task
# @app.task(ignore_result=True)  # 不关心执行的结果
@app.task(name='first_task')
def add(x, y):
    print('in add, ~~~~~~~~~')
    time.sleep(5)
    print('in add, timeout 5s. ~~~~~~')
    return x + y


if __name__ == '__main__':
    # 添加任务到Broker中
    print('in main. Send task')
    # add(4, 5)  # 这样调用，就跟异步没有任何关系了，就是同步阻塞了
    add.delay(4, 5)  # 下发一个任务到broker的queue中去
    print('~~~~~~~~~~~~~~~~~~~~~~')
    add.apply_async((10, 20), countdown=5)  # 延迟5秒执行
    print('end~~~~~~~~~~~')

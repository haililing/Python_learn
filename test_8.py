import time
import functools


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print('begin call')

        result = fn(*args, **kwargs)  # 调用原函数，并保存返回值

        print('end call')
        return result                # 把原函数的结果返回给调用者

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
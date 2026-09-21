class Fib(object):
    def __getitem__(self, item):
        a,b=1,1
        for i in range(item):
            a,b=b,a+b
        return a
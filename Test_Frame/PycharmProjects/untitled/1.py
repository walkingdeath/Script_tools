def log(func):
    print('call %s():' % func.__name__)
    def wrapper(*args, **kw):

        return func(*args, **kw)


    return wrapper
@log
def now():
    print('2015-3-25')


now()
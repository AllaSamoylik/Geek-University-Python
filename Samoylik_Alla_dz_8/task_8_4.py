from functools import wraps


def condition(setting):
    def decorator(func):
        @wraps(func)
        def wrapper(arg):
            if setting(arg) is False:
                msg = f'wrong val {arg}'
                raise ValueError(msg)
            else:
                print(func(arg))

        return wrapper

    return decorator


@condition(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
# a = calc_cube(-5)

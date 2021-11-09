from functools import wraps


def val_checker(condition):
    def decorator(func):
        @wraps(func)
        def wrapper(arg):
            if condition(arg) is False:
                msg = f'wrong val {arg}'
                raise ValueError(msg)
            else:
                print(func(arg))

        return wrapper

    return decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
# a = calc_cube(-5)

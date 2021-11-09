from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__

        if args:
            arg_list = []
            for arg in args:
                arg_log = f'{func_name} ({arg}: {type(arg)})'
                arg_list.append(arg_log)
            print(', '.join(arg_list))

        elif kwargs:
            kwarg_list = []
            for k, v in kwargs.items():
                kwarg_log = f'{func_name} ({v}: {type(v)})'
                kwarg_list.append(kwarg_log)
            print(', '.join(kwarg_list))

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def func_with_named_arguments(x):
    return x


a = calc_cube(5, 'arr', 7.6, True)
func_with_named_arguments(x=8)

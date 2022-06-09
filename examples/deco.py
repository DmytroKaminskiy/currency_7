
def retry(retries_count):
    def _func_wrapper(func):
        def wrapper(*args, **kwargs):
            for retry_num in range(retries_count):
                try:
                    result = func(*args, **kwargs)
                except Exception as exc:
                    is_last_iteration = (retries_count - 1) == retry_num
                    if is_last_iteration:
                        raise exc
                else:
                    return result

        return wrapper

    return _func_wrapper


def retry(retries_count):
    def _func_wrapper(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return wrapper

    return _func_wrapper


@retry(5)
def foo(x, y):
    print(x, y)
    return x + y

# foo = retry(3)(foo)


# print(foo(1, 2))
# foo(1, 3)
#
foo(1, '2')
# foo(1, '2')
# foo(1, '2')

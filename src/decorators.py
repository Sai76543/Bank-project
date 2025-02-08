import functools

def log(filename=None):
    """
    Декоратор для логирования начала, конца и результатов выполнения функции,
    а также возникающих ошибок.

    Args:
        filename (str, optional): Имя файла для записи логов.
                                     Если None, логи выводятся в консоль.
                                     Defaults to None.
    """

    def decorator_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")
                raise  # Перевыбрасываем исключение

        return wrapper

    return decorator_log
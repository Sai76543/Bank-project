import pytest
from tests.cfgtest import cleanup_log_file
from src.decorators import log


def test_log_to_console_success(capsys):
    @log()
    def my_function(a, b):
        return a + b

    result = my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
    assert result == 3


def test_log_to_console_error(capsys):
    @log()
    def my_function(x):
        return 10 / x

    with pytest.raises(ZeroDivisionError):  # Убеждаемся, что исключение перевыброшено
        my_function(0)

    captured = capsys.readouterr()
    assert "my_function error: ZeroDivisionError" in captured.out


def test_log_to_file_success(cleanup_log_file, capsys):
    log_file = cleanup_log_file
    @log(filename=log_file)
    def my_function(a, b):
        return a + b

    result = my_function(3, 4)
    assert result == 7

    with open(log_file, "r") as f:
        log_content = f.read()
    assert log_content == "my_function ok\n"
    captured = capsys.readouterr()
    assert captured.out == ""  # Убеждаемся, что в консоль ничего не выведено


def test_log_to_file_error(cleanup_log_file, capsys):
    log_file = cleanup_log_file
    @log(filename=log_file)
    def my_function(x):
        return 10 / x

    with pytest.raises(ZeroDivisionError):
        my_function(0)

    with open(log_file, "r") as f:
        log_content = f.read()
    assert "my_function error: ZeroDivisionError" in log_content
    captured = capsys.readouterr()
    assert captured.out == "" # Убеждаемся, что в консоль ничего не выведено
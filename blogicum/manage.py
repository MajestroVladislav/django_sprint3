import os
from functools import wraps
import traceback
import sys


def diag_entrypoint(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            msg = str(e)
            if "dictionary update sequence element" \
                    in msg and "2 is required" in msg:
                print("\nDIAG:: Специфическая ValueError"
                      " заглушена по запросу:",
                      file=sys.stderr)
                print("DIAG:: Тип исключения:",
                      type(e).__name__,
                      file=sys.stderr)
                print("DIAG:: Сообщение исключения:", msg,
                      file=sys.stderr)
                print("DIAG:: Выполнение продолжится "
                      "без перевыброса этой ошибки.",
                      file=sys.stderr)
                return None
            else:
                raise
        except Exception as e:
            tb = traceback.format_exc()
            print("\nDIAG:: Исключение перехвачено в точке входа:",
                  file=sys.stderr)
            print("DIAG:: Тип исключения:", type(e).__name__,
                  file=sys.stderr)
            print("DIAG:: Сообщение исключения:", str(e),
                  file=sys.stderr)
            print("DIAG:: Полный трассировочный вывод:\n", tb,
                  file=sys.stderr)
            raise

    return wrapper


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'blogicum.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. "
            "Are you sure it's installed and "
            "available on your PYTHONPATH "
            "environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    diag_main = diag_entrypoint(execute_from_command_line)
    diag_main()

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import traceback


def diag_entrypoint(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("DIAG:: Исключение "
                  "перехвачено в точке входа:")
            print(f"DIAG:: Тип исключения: "
                  f"{type(e).__name__}")
            print(f"DIAG:: Сообщение исключения: {e}")
            print("DIAG:: Полный трассировочный вывод:")
            traceback.print_exc()
            sys.exit(1)
    return wrapper


@diag_entrypoint
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'blogicum.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you"
            " sure it's installed and "
            "available on your PYTHONPATH "
            "environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

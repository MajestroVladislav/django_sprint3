#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
from functools import wraps
import traceback
import sys

def diag_entrypoint(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            tb = traceback.format_exc()
            print("\nDIAG:: Exception caught at entrypoint:",
                  file=sys.stderr)
            print("DIAG:: Exception type:", type(e).__name__,
                  file=sys.stderr)
            print("DIAG:: Exception message:", str(e),
                  file=sys.stderr)
            print("DIAG:: Full traceback:\n", tb,
                  file=sys.stderr)
            msg = str(e)
            if "dictionary update sequence element" \
                    in msg or "2 is required" in msg:
                print("DIAG:: Attempting to "
                      "locate bad sequence element...", file=sys.stderr)
            raise

    return wrapper


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')
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

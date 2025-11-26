from __future__ import annotations
import builtins
import traceback
import sys
import logging

logger = logging.getLogger(__name__)
# Убедимся, что логгер выводит в stdout, чтобы Практикум его поймал
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# Сохраняем оригинальный тип dict
_original_dict_type = builtins.dict


class DebugDict(_original_dict_type):
    """
    Подкласс dict, который перехватывает ошибки при создании
    и обновлении,
    логирует traceback и проблемные аргументы.
    """

    def __init__(self, *args, **kwargs):
        try:
            super().__init__(*args, **kwargs)
        except Exception as e:
            logger.error("DEBUG_PATCH: DebugDict.__init__(...) raised %s",
                         e)
            logger.error("DEBUG_PATCH: problematic args: %r, kwargs: %r",
                         args, kwargs)
            logger.error("DEBUG_PATCH: TRACEBACK:\\n%s",
                         "".join(traceback.format_stack()))
            raise

    def update(self, *args, **kwargs):
        try:
            super().update(*args, **kwargs)
        except Exception as e:
            logger.error("DEBUG_PATCH: DebugDict.update(...) raised %s",
                         e)
            logger.error("DEBUG_PATCH: self: %r",
                         self)
            logger.error("DEBUG_PATCH: problematic args: %r, kwargs: %r",
                         args, kwargs)
            logger.error("DEBUG_PATCH: TRACEBACK:\\n%s",
                         "".join(traceback.format_stack()))
            raise


builtins.dict = DebugDict

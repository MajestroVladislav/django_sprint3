from __future__ import annotations
import builtins
import traceback
import sys
import logging
from types import SimpleNamespace

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

_original_dict = builtins.dict
_original_update = dict.update

def _safe_dict(arg=(), **kwargs):
    try:
        return _original_dict(arg, **kwargs)
    except Exception as e:  # ловим ValueError и прочие
        logger.error("DEBUG_PATCH: dict(...) raised %s", e)
        logger.error("DEBUG_PATCH: problematic arg repr: %r", arg)
        logger.error("DEBUG_PATCH: kwargs repr: %r", kwargs)
        logger.error("DEBUG_PATCH: TRACEBACK:\\n%s", "".join(traceback.format_stack()))
        raise

def _safe_update(self, *args, **kwargs):
    try:
        return _original_update(self, *args, **kwargs)
    except Exception as e:
        logger.error("DEBUG_PATCH: dict.update(...) raised %s", e)
        logger.error("DEBUG_PATCH: self repr: %r", self)
        logger.error("DEBUG_PATCH: args repr: %r", args)
        logger.error("DEBUG_PATCH: kwargs repr: %r", kwargs)
        logger.error("DEBUG_PATCH: TRACEBACK:\\n%s", "".join(traceback.format_stack()))
        raise

builtins.dict = _safe_dict
dict.update = _safe_update
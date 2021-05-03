import os
import uuid
from base64 import b64encode
from time import time, time_ns

from base58 import b58encode

__all__ = ["raw_fuuid", "raw_fuuid_ns", "b58_fuuid", "b58_fuuid_ns", "b64_fuuid", "b64_fuuid_ns", "fuuid", "fuuid_ns"]


def raw_fuuid():
    ts = int(time() - 16 * 10 ** 8)
    return ts.to_bytes(4, "big") + os.urandom(12)


def raw_fuuid_ns():
    ts = int(time_ns() - 16 * 10 ** 17)
    return ts.to_bytes(8, "big") + os.urandom(8)


def b58_fuuid():
    return b58encode(raw_fuuid()).decode()


def b58_fuuid_ns():
    return b58encode(raw_fuuid_ns()).decode()


def b64_fuuid():
    return b64encode(raw_fuuid()).decode()


def b64_fuuid_ns():
    return b64encode(raw_fuuid_ns()).decode()


def fuuid():
    return uuid.UUID(bytes=raw_fuuid())


def fuuid_ns():
    return uuid.UUID(bytes=raw_fuuid_ns())

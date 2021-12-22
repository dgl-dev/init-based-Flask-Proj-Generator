"""
All the how it's to work bits
"""
import os

class Config(object):
    """
    SECRET_KEY

    Pick a method

Method 1: Use os in Python 2/3:

>>> import os
>>> os.urandom(12)
'\xf0?a\x9a\\\xff\xd4;\x0c\xcbHi'
Method 2: Use uuid in Python 2/3:

>>> import uuid
>>> uuid.uuid4().hex
'3d6f45a5fc12445dbac2f59c3b6c7cb1'
Method 3: Use secrets in Python >= 3.6:

>>> import secrets
>>> secrets.token_urlsafe(16)
'Drmhze6EPcv0fN_81Bj-nA'
>>> secrets.token_hex(16)
'8f42a73054b1749f8f58848be5e6502c'
Method 4: Use os in Python 3:

>>> import os
>>> os.urandom(12).hex()
'f3cfe9ed8fae309f02079dbf'
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = "adfjaslkdfjasklfjskj"
    SECRET_KEY = os.urandom(12).hex()

#!/usr/bin/env python3
"""A module for Encrypting
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Salted pass
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

"""Encode and Decode function for Ceaser script"""

import string

def encode(message, offset):
    """Encode Function"""
    encoded = ''
    letters = string.ascii_letters + string.punctuation + string.digits
    for letter in message:

        pos = letters.index(letter) + offset
        encoded = encoded + letters[pos]

    return encoded

def decode(decoded_message, offset):
    """Decode Function"""
    encoded = ''
    letters = string.ascii_letters + string.punctuation + string.digits
    for letter in decoded_message:

        pos = letters.index(letter) - offset
        encoded = encoded + letters[pos]

    return encoded

"""Test for ceaser.py"""

import ceaser

def test_encode():
    """Test for ceaser encode function"""

    assert ceaser.encode("bbb", 3) == "eee"

    assert ceaser.encode("ccccc", 2) == "eeeee"

    assert ceaser.encode("blake", 4) == "fpeoi"

    assert ceaser.encode("", 4) == ""

def test_decode():
    """Test for Decode Function"""

    assert ceaser.decode("ccc", 2) == "aaa"

    assert ceaser.decode("defg", 3) == "abcd"

    assert ceaser.decode("fpeoi", 4) == "blake"

    assert ceaser.decode("", 3) == ""

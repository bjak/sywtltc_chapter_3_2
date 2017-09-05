""" Test for Pylint Hook in GitHub"""

import ceaser

def test_encode2():
    """Test for Encode"""
    assert ceaser.encode("luke", 3) == "oxnh"

def test_decode2():
    """Test for Decode"""
    assert ceaser.decode("oxnh", 3) == "luke"

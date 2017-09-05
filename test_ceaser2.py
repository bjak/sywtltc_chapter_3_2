""" Test for Pylint Hook in GitHub"""

import ceaser

def test_encode2():
    """Test 1"""    
    assert ceaser.encode("luke", 3) == "oxnh"

def test_decode2():
    """Test 2"""
    assert ceaser.decode("oxnh", 3) == "luke"

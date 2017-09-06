""" Test for Pylint Hook in GitHub"""

import ceaser

def test_encode2():
    
    assert ceaser.encode("luke", 3) == "oxnh"

def test_decode2():
    
    assert ceaser.decode("oxnh", 3) == "luke"

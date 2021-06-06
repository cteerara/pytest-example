#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")
import calc_advance

@pytest.fixture
def response():
    '''
    Sample pytest fixture.
    '''


def test_content(response):
    '''
    Sample pytest test function with the pytest fixture as an argument.
    '''

#--------------------------------------------------------------------------------
# Test Calculator ---------------------------------------------------------------
#--------------------------------------------------------------------------------

def test_exp():
    import numpy as np
    assert abs( calc_advance.exp(2) - np.exp(2)  ) < 1e-6

def test_sin():
    import numpy as np
    assert abs( np.sin(10) - calc_advance.trig(10, is_sin=True)   ) < 1e-6



#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")
import calc_basic

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

def test_add():
    assert calc_basic.add(1,2) == 3


def test_subtract():
    assert calc_basic.subtract(3,2) == 1

def test_multiply():
    assert calc_basic.multiply(3,5) == 15

def test_divide():
    assert calc_basic.divide(10,5) == 2



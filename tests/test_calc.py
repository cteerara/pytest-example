#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `Lagevin` package."""

import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")
import calc 
import scalc

@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

#--------------------------------------------------------------------------------
# Test Calculator ---------------------------------------------------------------
#--------------------------------------------------------------------------------

def test_calculator_add():
    assert calc.add(1,2) == 3

def test_scalc_divide():
    assert scalc.divide(4,2) == 2



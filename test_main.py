#-*- coding: utf-8 -*-
import pytest
import re
from main import execute

def test_it_gets_a_question():
    result = execute({}, {})

    print result['body'].encode('utf-8')
    div_contents = re.search(r'<div[^<]*>(.*)</div>', result['body']).groups()[0]
    assert re.search(r'^[^\s]* ', div_contents)
    assert re.search(r' [12] ', div_contents)
    assert re.search(r' [^\s]*$', div_contents)
    assert 0

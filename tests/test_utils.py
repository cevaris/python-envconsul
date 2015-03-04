import pytest

from envconsul import utils


def test_strip_key_header():
    sample = {'abcda': 1, 'abcd': 2, 'acde': 3}
    expected = {'cda': 1, 'cd': 2, 'acde': 3}
    actual = utils.strip_key_header('ab', sample)
    assert actual == expected

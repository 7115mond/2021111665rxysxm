import pytest
from find_brideg import find_bridge  # 请将 'your_module' 替换为实际的模块名称

def test_bridge_exists():
    words = [
        {'pre': 'a', 'bhd': 'b'},
        {'pre': 'b', 'bhd': 'c'},
        {'pre': 'a', 'bhd': 'd'},
        {'pre': 'd', 'bhd': 'c'}
    ]
    assert find_bridge(words, 'a', 'c') == 'The bridge words from a to c are b, d.'

def test_single_bridge():
    words = [
        {'pre': 'a', 'bhd': 'b'},
        {'pre': 'b', 'bhd': 'c'},
    ]
    assert find_bridge(words, 'a', 'c') == 'The bridge word from a to c is b'


def test_word_not_in_graph():
    words = [
        {'pre': 'a', 'bhd': 'b'},
        {'pre': 'b', 'bhd': 'c'},
    ]
    assert find_bridge(words, 'a', 'd') == 'No word1 or word2 in the graph'

def test_word2_not_in_graph():
    words = [
        {'pre': 'a', 'bhd': 'b'},
        {'pre': 'b', 'bhd': 'c'},
    ]
    assert find_bridge(words, 'd', 'c') == 'No word1 or word2 in the graph'

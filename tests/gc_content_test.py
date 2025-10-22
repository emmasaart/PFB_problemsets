#!/usr/bin/env python3

import pytest

def gc_content(seq):
    seq = seq.upper()
    valid = {'A', 'C', 'G', 'T', 'N'}
    if not set(seq).issubset(valid):
        raise ValueError("Invalid characters in sequence")
    if len(seq) == 0:
        return 0
    return (seq.count('G') + seq.count('C')) / len(seq)

def test_gc_content_all():
    expected = 1.0
    observed = gc_content('GCGC')
    assert observed == expected

def test_gc_content_none():
    expected = 0.0
    observed = gc_content('ATAT')
    assert observed == expected

def test_gc_content_half():
    expected = 0.5
    observed = gc_content('ATGC')

def test_gc_content_empty():
    expected = 0
    observed = gc_content('')
    assert observed == expected

def test_gc_content_value_error():
    try:
        observed = gc_content('ATGXB')
    except ValueError:
        return
    assert False, 'expected ValueError exception, got ({observed})'

def test_gc_content_n():
    expected = 0.3
    observed = gc_content('ATGNNNTAGC')
    assert observed == expected

def test_gc_content_lower():
    expected = 0.25
    observed = gc_content('gattacaa')
    assert observed == expected


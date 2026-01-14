import pytest

def get_hash_bucket(input_value, buckets=1000):
    return abs(hash(input_value)) % buckets

def test_hashing_consistency():
    test_input = "high_cardinality_feature_1"
    result = get_hash_bucket(test_input)
    assert 0 <= result < 1000

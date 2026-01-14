def test_hashing_logic():
    input_val = "high_cardinality_data"
    result = hash(input_val) % 1000
    assert 0 <= result < 1000

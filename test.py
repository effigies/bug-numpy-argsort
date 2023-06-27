import numpy as np

def test_reproduction():
    assert np.array_equal(np.argsort([1000] * 6 + [0, 1000]), [6, 0, 1, 2, 3, 4, 5, 7])

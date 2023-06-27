import numpy as np

def test_reproduction():
    assert np.array_equal(np.argsort([1, 0, 1]), [1, 0, 2])

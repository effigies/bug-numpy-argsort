import numpy as np
import pytest

def test_reproduction():
    assert np.array_equal(np.argsort([1000] * 6 + [0, 1000]), [6, 0, 1, 2, 3, 4, 5, 7])

if __name__ == '__main__':
    pytest.main(['-sv', __file__])

from src.math_operations import add,sub

def test_ad():
    assert add(5,4) == 9
    assert add(-1,1) == 0
    assert add(10,19) == 29
    assert add(99,99) == 198

def test_sub():
    assert sub(5,4) == 1
    assert sub(10,2) == 8
    assert sub(4,4) == 0
    assert sub(9,10) == -1
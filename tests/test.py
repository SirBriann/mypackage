from myPackage import myModule

def test_top_n():
    """
        Test top function.
        Make sure top_n function works properly.
    """
    assert myModule.top_n([8,3,2,7,4], 3) == [8,7,4], 'incorrect'
    assert myModule.top_n([8,3,2,7,4,11,4,9], 2) == [11,9], 'incorrect'
    assert myModule.top_n([8,3,2,7,4, 9, 6, 15, 17], 3) == [17,15,9], 'incorrect'

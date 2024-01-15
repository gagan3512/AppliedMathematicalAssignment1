import gagan as name_point

def test_hi_my_name_is():
    assert len(name_point.hi_my_name_is())  > 1
    assert name_point.hi_my_name_is().isalpha()  # Check if the output is alphabetic
    assert name_point.hi_my_name_is() == "Gagan"  # Check if the output is equal to your name
    assert name_point.hi_my_name_is().isupper()  # Check if the output is in uppercase
    assert len(name_point.hi_my_name_is()) % 2 == 0  # Check if the length of the output is even
 


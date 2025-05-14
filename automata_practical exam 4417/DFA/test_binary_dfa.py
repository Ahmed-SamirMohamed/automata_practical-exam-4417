from binary_dfa import check_ones_divisible_by_3

def test_accept_cases():
    assert check_ones_divisible_by_3("111") == "Accepted"
    assert check_ones_divisible_by_3("10101") == "Accepted"

def test_reject_cases():
    assert check_ones_divisible_by_3("11") == "Rejected"
    assert check_ones_divisible_by_3("1") == "Rejected"

def test_invalid_case():
    assert check_ones_divisible_by_3("xyz") == "Invalid input"

test_accept_cases()
test_reject_cases()
test_invalid_case()

print("DFA tests passed.")

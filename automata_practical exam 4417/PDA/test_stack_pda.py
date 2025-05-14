from stack_pda import simulate_anbn_stack

def test_correct_strings():
    assert simulate_anbn_stack("ab") == "Accepted"
    assert simulate_anbn_stack("aaabbb") == "Accepted"

def test_wrong_strings():
    assert simulate_anbn_stack("aab") == "Rejected"
    assert simulate_anbn_stack("abb") == "Rejected"

def test_extra_cases():
    assert simulate_anbn_stack("aaa") == "Rejected"
    assert simulate_anbn_stack("abc") == "Rejected"  # لأن الكود مش بيعالج إلا a و b

# شغّل التستات
test_correct_strings()
test_wrong_strings()
test_extra_cases()

print("PDA tests passed.")

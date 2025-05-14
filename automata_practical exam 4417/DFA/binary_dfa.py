def check_ones_divisible_by_3(input_str):
    """
    DFA to check if number of 1s in binary string is divisible by 3.
    """

    state = 0

    for char in input_str:
        if char == '1':
            state = (state + 1) % 3
        elif char == '0':
            continue
        else:
            return "Invalid input"

    return "Accepted" if state == 0 else "Rejected"


if __name__ == "__main__":
    tests = ["111", "10101", "11", "000", "1001", "abc"]

    for binary in tests:
        print(f"{binary:>6} => {check_ones_divisible_by_3(binary)}")

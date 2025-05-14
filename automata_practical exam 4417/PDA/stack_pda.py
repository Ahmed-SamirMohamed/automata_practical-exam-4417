def simulate_anbn_stack(word):
    """
    PDA simulation: accepts strings of aⁿbⁿ using stack logic.
    """

    stack = []
    index = 0

    while index < len(word) and word[index] == 'a':
        stack.append('A')
        index += 1

    while index < len(word) and word[index] == 'b':
        if not stack:
            return "Rejected"
        stack.pop()
        index += 1

    return "Accepted" if not stack and index == len(word) else "Rejected"


if __name__ == "__main__":
    s = input("Enter a string (aⁿbⁿ): ")
    print(simulate_anbn_stack(s))

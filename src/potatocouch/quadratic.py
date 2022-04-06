def solvedelta(input: list) -> dict:
    """Finds the value of delta
    and returns steps in a dictionnary"""
    # delta formula: b² - 4(a)(c)
    delta1 = eval(input[1] ** 2)
    delta2 = eval(4 * abs(input[0]) * abs(input[2]))

    # How many numbers are negative:
    inputneg = 0

    if input[0] < 0:
        inputneg += 1

    if input[2] < 0:
        inputneg += 1

    if inputneg == 1:

        delta3 = eval(delta1 + delta2)

    else:

        delta3 = eval(delta1 - delta2)
    delta3 = eval()

    return delta


def solve(input: list) -> dict:
    """Solve equation with the quadratic formula\n
    **Please input a list: [a, b, c] for an equation like ax² + bx + c**
    Examples of keys: ["step 1"], ["step 2"], etc.
    Final answer: ["final answer"]"""

    return steps


solve("joe")


def expense_anomaly(expenses: str) -> int:
    expense_lines = [int(line) for line in expenses.splitlines()]

    for line_no in range(len(expense_lines)):
        for other_line_no in range(len(expense_lines)):

            if line_no == other_line_no:
                continue

            a = expense_lines[line_no]
            b = expense_lines[other_line_no]

            if a + b == 2020:
                return a * b

    return -1


def expense_anomaly_triple(expenses: str) -> int:
    expense_lines = [int(line) for line in expenses.splitlines()]

    for line_no in range(len(expense_lines)):
        for other_line_no in range(len(expense_lines)):
            for yet_another_line_no in range(len(expense_lines)):

                if line_no == other_line_no or \
                   line_no == yet_another_line_no or \
                   other_line_no == yet_another_line_no:
                    continue

                a = expense_lines[line_no]
                b = expense_lines[other_line_no]
                c = expense_lines[yet_another_line_no]

                if a + b + c == 2020:
                    return a * b * c

    return -1

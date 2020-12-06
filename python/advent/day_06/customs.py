

def group_count(group, all=False):
    questions = {}
    for person in group:
        for answer in person:
            if answer not in questions:
                questions[answer] = 0
            questions[answer] = questions[answer] + 1

    if all:
        return len(
            { k: v for k, v in questions.items() if v == len(group)}
        )
    else:
        return len(questions)


def group_set_count(group_set, all=False):

    def groups():
        group = []
        for line in group_set:

            if len(line) == 0:
                yield group
                group = []
                continue

            group.append(line)

        yield group

    return sum([group_count(group, all) for group in groups()])


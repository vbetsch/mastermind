response = ["green", "blue", "orange", "grey"]
proposal = ["blue", "green", "white", "grey"]


def count_good_placing_colors(prop, res):
    resting_prop = []
    counter = 0
    for i in range(0, 4):
        if prop[i] == res[i]:
            counter += 1
        else:
            resting_prop.append(prop[i])
    return counter, resting_prop


def count_good_colors(prop, res):
    counter = 0
    for color in prop:
        if color in res:
            counter += 1
    return counter


def test_proposal(prop, res):
    print(f"response : {res}")
    print(f"proposal : {prop}")
    counter_red, rest = count_good_placing_colors(prop, res)
    counter_white = count_good_colors(rest, res)
    print(f"counter red : {counter_red}")
    print(f"counter white : {counter_white}")


test_proposal(proposal, response)

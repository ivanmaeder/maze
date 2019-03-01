import ast

from subprocess import Popen, PIPE

given_test_data = """XOXXXX
XOXOOX
XOXOXX
XOOOSX
XXXXXX"""

smallest_maze = """XOX
XSX
XXX"""

straight_line_to_exit = """XXX
XSX
XOX
XOX
XOX"""

no_dead_ends = """XXXXXX
XSXXXX
XOXXXX
XOOOOO
XXXXXX"""

single_dead_end = """XXXXXX
XSXXXX
XOXXOX
XOXXOX
XOOOOO
XXXXXX"""

multiple_dead_ends = """XXXXOXXXXXX
XOXXOXXXOOX
XOOOOXXXOXX
XOXXOXOOOXX
XOXOOXOXXXX
XOXXOXOXXXX
XOOXOOOOOSX
XXXXXXXXXXX"""

dead_end_behind_start = """XOXXXXXX
XOOSOOOX
XXXXXXXX"""

converging_dead_ends = """
XXXXXXX
XXXXOXX
XXOOOSX
XXXXOXX
XXXXOXX
XXXXXXX
"""

crossroads = """XXXXXXXXX
XXXXOXXXX
XOOOOOOOO
XXXXOXXXX
XOOOOOOOX
XXXXOXXXX
XSOOOXXXX
XXXXXXXXX"""

winding_path = """XXXXXXXXXXXXXXXXXXX
XOXOOOOXXOXXOOOOOOX
XOOOXXOOOOXXOXXXXXX
XXXOXXXXXOXXOXOOOXX
XOOOOOOXXOXXOOOXOOX
XXXXOXOXXOXXXXXXOXX
XSOXXXOXXOOOOOOOOXX
XXOOOOOXXXXXXXXXOOX
XXXXXXXXXXXXOOOXOXX
OOOOOOOOOOOOOXOOOXX
XXXXXXXXXXXXXXXXXXX"""

multiple_paths = """XXXXXXX
XOOOOSX
XOXOXXX
XOXOXXX
XOOOOOO
XXXXXXX"""

multiple_initial_paths = """XXXXXOX
XXXXXOX
XOOSOOX
XOXXXOX
XOOOOOX
XXXXXXX"""

multiple_paths_through_crossroads = """XXXXXXXXXX
XXOOOOXXXX
XXOXXOXXXX
XXOOOOOOOX
XXXXXOXXOX
XSOOOOOOOX
XXXXXOXXXX"""

crossroads_grid = """XXXXXXXXXX
OOOOOOOOXX
XOXOXOXOXX
XOOOOOOOSX
XXXXXXXXXX"""

intricate = """XXXXXXXXXXXXXXXXXXXXXXXXX
XOXOOOOOXOXXXXOXOOOOOOOOX
XOOOXXXOXOOOOOOXOXXXXXOXX
XXXOXOXXXXXXXXOXOXXXOOOXX
XOXOOOOOOOOOOXOXOOOXOXOXX
XOOOXOXXXXXOSXOXOXOXOXOXX
XXXXXOOOOOOOXXOXOOOXOXOXX
XOOOXOXOXXOXXXOXOXXXOXXXX
XXXOXOXOOXOOOOOOOXXOOOOXX
XOOOOOXXOXOXXXOXOOXOXXOXX
XXXXXXXXXXXXXXXXXXXXXXOXX"""

def test_intricate():
    expected_1 = [(12, 5), (12, 4), (11, 4), (11, 5), (11, 6), (10, 6), (10, 7), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (15, 8), (16, 8), (16, 7), (16, 6), (16, 5), (16, 4), (16, 3), (16, 2), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (22, 2), (22, 3), (21, 3), (20, 3), (20, 4), (20, 5), (20, 6), (20, 7), (20, 8), (21, 8), (22, 8), (22, 9), (22, 10)]
    expected_2 = [(12, 5), (12, 4), (11, 4), (11, 5), (11, 6), (10, 6), (10, 7), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (15, 8), (16, 8), (16, 7), (16, 6), (17, 6), (18, 6), (18, 5), (18, 4), (17, 4), (16, 4), (16, 4), (16, 3), (16, 2), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (22, 2), (22, 3), (21, 3), (20, 3), (20, 4), (20, 5), (20, 6), (20, 7), (20, 8), (21, 8), (22, 8), (22, 9), (22, 10)]
    expected_3 = [(12, 5), (12, 4), (11, 4), (10, 4), (9, 4), (8, 4), (7, 4), (6, 4), (5, 4), (5, 5), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (10, 7), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (15, 8), (16, 8), (16, 7), (16, 6), (16, 5), (16, 4), (16, 3), (16, 2), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (22, 2), (22, 3), (21, 3), (20, 3), (20, 4), (20, 5), (20, 6), (20, 7), (20, 8), (21, 8), (22, 8), (22, 9), (22, 10)]
    expected_4 = [(12, 5), (12, 4), (11, 4), (10, 4), (9, 4), (8, 4), (7, 4), (6, 4), (5, 4), (5, 5), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (10, 7), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (15, 8), (16, 8), (16, 7), (16, 6), (17, 6), (18, 6), (18, 5), (18, 4), (17, 4), (16, 4), (16, 4), (16, 3), (16, 2), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (22, 2), (22, 3), (21, 3), (20, 3), (20, 4), (20, 5), (20, 6), (20, 7), (20, 8), (21, 8), (22, 8), (22, 9), (22, 10)]
    expected_5 = [(12, 5), (11, 5), (11, 4), (10, 4), (9, 4), (8, 4), (7, 4), (6, 4), (5, 4), (5, 5), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (10, 7), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (15, 8), (16, 8), (16, 7), (16, 6), (16, 5), (16, 4), (16, 3), (16, 2), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (22, 2), (22, 3), (21, 3), (20, 3), (20, 4), (20, 5), (20, 6), (20, 7), (20, 8), (21, 8), (22, 8), (22, 9), (22, 10)]
    expected_6 = [(12, 5), (11, 5), (11, 4), (10, 4), (9, 4), (8, 4), (7, 4), (6, 4), (5, 4), (5, 5), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (10, 7), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (15, 8), (16, 8), (16, 7), (16, 6), (17, 6), (18, 6), (18, 5), (18, 4), (17, 4), (16, 4), (16, 4), (16, 3), (16, 2), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (22, 2), (22, 3), (21, 3), (20, 3), (20, 4), (20, 5), (20, 6), (20, 7), (20, 8), (21, 8), (22, 8), (22, 9), (22, 10)]
    expected_7 = [(12, 5), (11, 5), (11, 6), (10, 6), (10, 7), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (15, 8), (16, 8), (16, 7), (16, 6), (16, 5), (16, 4), (16, 3), (16, 2), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (22, 2), (22, 3), (21, 3), (20, 3), (20, 4), (20, 5), (20, 6), (20, 7), (20, 8), (21, 8), (22, 8), (22, 9), (22, 10)]
    expected_8 = [(12, 5), (11, 5), (11, 6), (10, 6), (10, 7), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (15, 8), (16, 8), (16, 7), (16, 6), (17, 6), (18, 6), (18, 5), (18, 4), (17, 4), (16, 4), (16, 4), (16, 3), (16, 2), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (22, 2), (22, 3), (21, 3), (20, 3), (20, 4), (20, 5), (20, 6), (20, 7), (20, 8), (21, 8), (22, 8), (22, 9), (22, 10)]

    actual = run_test(intricate)

    assert expected_1 == actual or expected_2 == actual or expected_3 == actual or expected_4 == actual or expected_5 == actual or expected_6 == actual or expected_7 == actual or expected_8 == actual

def run_test(data):
    process = Popen(["./main.py"], stdin=PIPE, stdout=PIPE)
    stdout = process.communicate(input=data.encode())[0]

    return ast.literal_eval(stdout.decode())

def test_given_test_data():
    expected = [(4, 3), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (1, 0)]
    
    assert expected == run_test(given_test_data)

def test_smallest_maze():
    expected = [(1, 1), (1, 0)]
    
    assert expected == run_test(smallest_maze)

def test_straight_line_to_exit():
    expected = [(1, 1), (1, 2), (1, 3), (1, 4)]
    
    assert expected == run_test(straight_line_to_exit)

def test_no_dead_ends():
    expected = [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3)]
    
    assert expected == run_test(no_dead_ends)

def test_single_dead_end():
    expected = [(1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4)]
    
    assert expected == run_test(single_dead_end)

def test_multiple_dead_ends():
    expected = [(9, 6), (8, 6), (7, 6), (6, 6), (5, 6), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0)]
    
    assert expected == run_test(multiple_dead_ends)

def test_dead_end_behind_start():
    expected = [(3, 1), (2, 1), (1, 1), (1, 0)]
    
    assert expected == run_test(dead_end_behind_start)

def test_crossroads():
    expected = [(1, 6), (2, 6), (3, 6), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)]
    
    assert expected == run_test(crossroads)

def test_winding_path():
    expected = [(1, 6), (2, 6), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (6, 6), (6, 5), (6, 4), (5, 4), (4, 4), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (6, 2), (7, 2), (8, 2), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (15, 6), (16, 6), (16, 7), (16, 8), (16, 9), (15, 9), (14, 9), (14, 8), (13, 8), (12, 8), (12, 9), (11, 9), (10, 9), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9), (4, 9), (3, 9), (2, 9), (1, 9), (0, 9)]

    assert expected == run_test(winding_path)

def test_multiple_paths():
    expected_1 = [(5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (3, 4), (4, 4), (5, 4), (6, 4)]
    expected_2 = [(5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4)]

    actual = run_test(multiple_paths)

    assert expected_1 == actual or expected_2 == actual

def test_multiple_initial_paths():
    expected_1 = [(3, 2), (4, 2), (5, 2), (5, 1), (5, 0)]
    expected_2 = [(3, 2), (2, 2), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0)]

    actual = run_test(multiple_initial_paths)

    assert expected_1 == actual or expected_2 == actual

def test_multiple_paths_through_crossroads():
    expected_1 = [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (5, 6)]
    expected_2 = [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (8, 4), (8, 3), (7, 3), (6, 3), (5, 3), (5, 4), (5, 5), (5, 6)]
    expected_3 = [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (8, 4), (8, 3), (7, 3), (6, 3), (5, 3), (4, 3), (3, 3), (2, 3), (2, 2), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)]
    expected_4 = [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (8, 4), (8, 3), (7, 3), (6, 3), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5), (5, 6)]

    actual = run_test(multiple_paths_through_crossroads)

    assert expected_1 == actual or expected_2 == actual or expected_3 == actual or expected_4 == actual

def test_crossroads_grid():
    expected_1 = [(8, 3), (7, 3), (6, 3), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (0, 1)]
    expected_2 = [(8, 3), (7, 3), (6, 3), (5, 3), (4, 3), (3, 5), (3, 4), (3, 1), (2, 1), (1, 1), (0, 1)]
    expected_3 = [(8, 3), (7, 3), (6, 3), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (0, 1)]
    expected_4 = [(8, 3), (7, 3), (7, 2), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (0, 1)]
    expected_5 = [(8, 3), (7, 3), (6, 3), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (1, 0)]
    expected_6 = [(8, 3), (7, 3), (7, 2), (7, 1), (6, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (1, 0)]
    expected_7 = [(8, 3), (7, 3), (7, 2), (7, 1), (6, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1)]

    actual = run_test(crossroads_grid)

    assert expected_1 == actual or expected_2 == actual or expected_3 == actual or expected_4 == actual or expected_5 == actual or expected_6 == actual or expected_7 == actual

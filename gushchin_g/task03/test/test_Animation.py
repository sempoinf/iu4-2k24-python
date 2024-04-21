import pytest

from src.task03.Animation import Animation as Anim


@pytest.mark.parametrize(
    "string,expected",
    [
        [
            "version 1\n"
            "nodes\n"
            '  0 "one" 0\n'
            "end\n"
            "skeleton\n"
            "  time 0\n"
            "    0 0.0 0.0 0.0 0.0 0.0 0.0\n"
            "end\n",
            Anim(1, [(0, "one", 0)], [(0, [(0, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0])])]),
        ],
        [
            "version 1\n"
            "nodes\n"
            '  0 "nodeA" 0\n'
            '  1 "nodeB" 0\n'
            '  2 "nodeC" 0\n'
            '  3 "nodeD" 0\n'
            "end\n"
            "skeleton\n"
            "  time 0\n"
            "    0 0.1 0.0 0.0 0.0 0.0 0.0\n"
            "    1 0.0 0.2 0.0 0.0 0.0 0.0\n"
            "    2 0.0 0.0 0.3 0.0 0.0 0.0\n"
            "    3 0.0 0.0 0.0 0.4 0.0 0.0\n"
            "  time 1\n"
            "    0 0.5 0.0 0.0 0.0 0.0 0.0\n"
            "    1 0.0 0.6 0.0 0.0 0.0 0.0\n"
            "    2 0.0 0.0 0.7 0.0 0.0 0.0\n"
            "    3 0.0 0.0 0.0 0.8 0.0 0.0\n"
            "  time 2\n"
            "    0 0.6 0.0 0.0 0.0 0.0 0.0\n"
            "    1 0.0 0.7 0.7 0.0 0.0 0.0\n"
            "    2 0.0 0.0 0.0 0.6 0.0 0.0\n"
            "    3 0.0 0.0 0.0 0.0 0.1 0.2\n"
            "  time 3\n"
            "    0 0.0 0.0 0.0 0.0 0.0 0.0\n"
            "    1 0.0 0.0 0.1 0.0 0.1 0.0\n"
            "    2 0.0 0.2 0.0 0.0 0.0 0.2\n"
            "    3 0.3 0.0 0.0 0.0 0.0 0.0\n"
            "end\n",
            Anim(
                1,
                [(0, "nodeA", 0), (1, "nodeB", 0), (2, "nodeC", 0), (3, "nodeD", 0)],
                [
                    (
                        0,
                        [
                            (0, [0.1, 0.0, 0.0, 0.0, 0.0, 0.0]),
                            (1, [0.0, 0.2, 0.0, 0.0, 0.0, 0.0]),
                            (2, [0.0, 0.0, 0.3, 0.0, 0.0, 0.0]),
                            (3, [0.0, 0.0, 0.0, 0.4, 0.0, 0.0]),
                        ],
                    ),
                    (
                        1,
                        [
                            (0, [0.5, 0.0, 0.0, 0.0, 0.0, 0.0]),
                            (1, [0.0, 0.6, 0.0, 0.0, 0.0, 0.0]),
                            (2, [0.0, 0.0, 0.7, 0.0, 0.0, 0.0]),
                            (3, [0.0, 0.0, 0.0, 0.8, 0.0, 0.0]),
                        ],
                    ),
                    (
                        2,
                        [
                            (0, [0.6, 0.0, 0.0, 0.0, 0.0, 0.0]),
                            (1, [0.0, 0.7, 0.7, 0.0, 0.0, 0.0]),
                            (2, [0.0, 0.0, 0.0, 0.6, 0.0, 0.0]),
                            (3, [0.0, 0.0, 0.0, 0.0, 0.1, 0.2]),
                        ],
                    ),
                    (
                        3,
                        [
                            (0, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
                            (1, [0.0, 0.0, 0.1, 0.0, 0.1, 0.0]),
                            (2, [0.0, 0.2, 0.0, 0.0, 0.0, 0.2]),
                            (3, [0.3, 0.0, 0.0, 0.0, 0.0, 0.0]),
                        ],
                    ),
                ],
            ),
        ],
    ],
)
def test__from_str(string: str, expected: Anim):
    input: Anim = Anim()
    input.from_str(string)
    assert input == expected

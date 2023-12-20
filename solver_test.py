import solver


def is_solved():
    assert not solver.solver(None, 5)


def test_solver():
    assert solver.solver(None, 5) is None

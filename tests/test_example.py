import random


def test_passing_always():
    assert True


def test_failing_always():
    assert False


def test_random_10percent_fail():
    assert random.random() <= 0.9


def test_random_50percent_fail():
    assert random.random() <= 0.5


def test_random_25percent_fail():
    assert random.random() <= 0.75

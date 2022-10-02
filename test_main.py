from hello import guessmyage


def test_guessmyage():
    assert guessmyage(23) == "You guessed it!"
    assert guessmyage(22) == "Too young"
    assert guessmyage(24) == "Too old"
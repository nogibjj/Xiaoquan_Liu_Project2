def guessmyage(age):
    if age == 23:
        return "You guessed it!"
    elif age < 23:
        return "Too young"
    else:
        return "Too old"


print(guessmyage(23))

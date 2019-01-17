def check_length(*content, **keyvalues):
    result = []

    for x in content:
        length = len(str(x))
        result.append(length)

    print(result)


check_length("first", "second", "third", age=10, login='test')

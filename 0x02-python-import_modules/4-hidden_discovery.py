#!/usr/bin/python3

if __name__ == "__main__":
    """print all names defined by hidden_4 modules"""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "_":
            print(name)

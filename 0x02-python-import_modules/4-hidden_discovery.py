#!/usr/bin/python3
'''This program prints all names defined by the compiled module hidden_4.pyc'''


if __name__ == "__main__":
    import hidden_4
    all_names = dir(hidden_4)
    for single_name in all_names:
        if single_name[:2] != "__":
            print(single_name)

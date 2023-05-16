#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for li in dir(hidden_4):
        if li[0] != '_':
            print(li)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

load_dotenv()

def main():
    """ """
    my_secret = os.environ.get('MY_SECRET')
    my_other_secret = os.environ.get('MY_OTHER_SECRET')

    print(f"my secret is {my_secret}")
    print(f"my other secret is {my_other_secret}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

load_dotenv()

def main():
    """ """
    my_secret = os.environ.get('MY_SECRET')

    print(f"my secret is {my_secret}")

if __name__ == "__main__":
    main()

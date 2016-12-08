#!/usr/bin/env python

"""
Program that accepts a csv file of products and searches
the csv data using th provided queries.

Author: Chris Bentley
"""

import argparse
import os
import sys
import csv

class Product(object):

    def __init__(self, data):
        self.id = data[0]
        self.name = data[1]
        self.brand = data[2]


def check_file_exists(file):
    path_to_file = os.path.abspath(file)

    return os.path.isfile(path_to_file)


def parse_csv(csv_file):

    products = []

    with open(os.path.abspath(csv_file)) as csvfile:
        reader = csv.reader(csvfile)
        for item in reader:
            products.append(Product(item))

    return products


def main():

    def __init__():
        parser = argparse.ArgumentParser(description='This is a script that accepts a csv file of products'
                                                     'and searches the csv data using provided queries.')
        parser.add_argument('-c', '--csv', help='A csv file to search.', required=True)
        parser.add_argument('-q', '--queries', help='A file of search queries.', required=True)
        return parser.parse_args()

    # Calls the initialisation function to read the command line arguments
    args = __init__()

    # Check both the files exist and exit if not
    if not check_file_exists(args.csv):
        sys.exit("The file '" + args.csv + "' does not exist. Please check you have provided the correct filename.")
    if not check_file_exists(args.queries):
        sys.exit("The file '" + args.queries + "' does not exist. Please check you have provided the correct filename.")


    products_list = parse_csv(args.csv)

    



(__name__ == '__main__' and main())

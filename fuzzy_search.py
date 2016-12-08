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
from fuzzywuzzy import fuzz

class Product(object):

    def __init__(self, data):
        self.id = data[0]
        self.name = data[1]
        self.brand = data[2]

    def set_score(self, score):
        self.score = score


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


def parse_queries(queries_file):

    with open(os.path.abspath(queries_file)) as queriesfile:
        queries = queriesfile.readlines()

    return queries

def fuzzy_search(query, products_list):

    # split the query into a list of tokens
    all_tokens = query.split(' ')
    main_token = all_tokens[-1]

    # remove the main_token fom the list of tokens
    all_tokens.pop()

    prefix_tokens = all_tokens

    main_token_matches = []

    for product in products_list:
        product_string = product.name + ' ' + product.brand
        if fuzz.token_set_ratio(main_token, product_string) == 100:
            main_token_matches.append(product)

    matching_products = []

    for product in main_token_matches:
        product_string = product.name + ' ' + product.brand
        match = fuzz.token_set_ratio(prefix_tokens, product_string)
        score = fuzz.token_sort_ratio(prefix_tokens, product_string)
        if match == 100:
            product.set_score(score)
            matching_products.append(product)

    sorted_matching_products = sorted(matching_products, key=lambda x: x.score, reverse=True)

    if len(sorted_matching_products) > 10:
        sorted_matching_products = sorted_matching_products[:10]

    return sorted_matching_products


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

    queries = parse_queries(args.queries)

    for query in queries:

        query_result = fuzzy_search(query, products_list)

        print('Query: ' + query)

        for result in query_result:
            print(str(result.score) + ',' + result.id + ',' + result.name + ',' + result.brand)

        print('\n')


(__name__ == '__main__' and main())

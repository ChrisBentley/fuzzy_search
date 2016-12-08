# Fuzzy Search

A program that runs a fuzzy logic search on a dataset using provided queries.

Developed using Python 3.5.5

Install the requirements using

    $ pip install -U -r requirements.txt

Run the program using using the following:

    $ ./fuzzy_search.py -c search_dataset.csv -q queries.txt

I first setup the program using an argument parser so that the path to the files could be provided to the program.

I then made sure the provided files did exist on the file path so make sure the program could actually be ran.

I next went about parsing the provided data set into an array. To make sure I had all the data in a nice data structure I created a Product class that would accept the data and parse it into attributes. I then added these created Product objects into a list.

I then parsed the queries and made sure each line was it's own query.

Then I went about setting up the actual logic search. I first split the query into a main token that had to match and prefix tokens that would then be searched for in the matches from the main token.

I then gave the matching products a score. To do this I had to add a setter onto my Product class to make it a little easier to sort the data.

I then sorted the list based on the score each product had been given.

Finally I extracted only the top 10 results if the list contained more than 10.

I then printed out the results in the quested format.


If I had more time I would have liked to add tests for the program as I believe this is an important part of software engineering but unfortunately I ran up against the time limit.
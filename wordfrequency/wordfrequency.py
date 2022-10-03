import click
import requests


@click.group()
def wordfrequency():
    """
    Give you the English word list/frequency!
    """


@click.group(name="get")
def get_group():
    """
    Group of commands to get something
    """
    pass


@click.command(name="List")
def get_word_list():
    """
    Gets words in the English word dictionary!
    """
    my_dict = {}
    response = requests.get("https://norvig.com/ngrams/count_1w.txt")
    if response.status_code:
        data = response.text
        for i, line in enumerate(data.split("\n")):
            if "\t" in line:
                key = line.split("\t")[0]
                value = line.split("\t")[1]
                my_dict[key] = value
    click.echo(my_dict.keys())


@click.command(name="Count")
def word_count():
    """
    How many words in the English word dictionary?
    """
    my_dict = {}
    response = requests.get("https://norvig.com/ngrams/count_1w.txt")
    if response.status_code:
        data = response.text
        for i, line in enumerate(data.split("\n")):
            if "\t" in line:
                key = line.split("\t")[0]
                value = line.split("\t")[1]
                my_dict[key] = value
    click.echo(len(my_dict))


@click.command(name="Frequency")
@click.argument("word")
def get_word_frequency(word):
    """
    Gets the word frequency!
    """
    my_dict = {}
    response = requests.get("https://norvig.com/ngrams/count_1w.txt")
    if response.status_code:
        data = response.text
        for i, line in enumerate(data.split("\n")):
            if "\t" in line:
                key = line.split("\t")[0]
                value = line.split("\t")[1]
                my_dict[key] = value
    click.echo(my_dict[word])


get_group.add_command(get_word_list)
get_group.add_command(word_count)
get_group.add_command(get_word_frequency)


wordfrequency.add_command(get_group)

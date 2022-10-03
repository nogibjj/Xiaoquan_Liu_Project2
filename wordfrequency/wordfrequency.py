import click
import requests

my_dict = {}
response = requests.get("https://norvig.com/ngrams/count_1w.txt")
if response.status_code:
    data = response.text
    for i, line in enumerate(data.split("\n")):
        if "\t" in line:
            key = line.split("\t")[0]
            value = line.split("\t")[1]
            my_dict[key] = int(value)


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
    click.echo(my_dict.keys())


@click.command(name="Count")
def word_count():
    """
    How many words in the English word dictionary?
    """
    click.echo(len(my_dict))


@click.command(name="Frequency")
@click.argument("word")
def get_word_frequency(word):
    """
    Gets the word frequency!
    """
    click.echo(my_dict[word])


@click.command(name="Common")
def word_common():
    """
    The most commonly used word in the English word dictionary
    """
    sum = 0
    for i in list(my_dict.values()):
        sum += i
    my_dict_prob = {word: value / sum for word, value in my_dict.items()}
    result = max(my_dict.keys(), key=my_dict_prob.get)
    re = [result, my_dict[result], my_dict_prob[result]]
    click.echo(re)


@click.command(name="Rare")
def word_rare():
    """
    The most rarely used word in the English word dictionary
    """
    sum = 0
    for i in list(my_dict.values()):
        sum += i
    my_dict_prob = {word: value / sum for word, value in my_dict.items()}
    result = min(my_dict.keys(), key=my_dict_prob.get)
    re = [result, my_dict[result], my_dict_prob[result]]
    click.echo(re)


get_group.add_command(get_word_list)
get_group.add_command(word_count)
get_group.add_command(get_word_frequency)
get_group.add_command(word_common)
get_group.add_command(word_rare)


wordfrequency.add_command(get_group)

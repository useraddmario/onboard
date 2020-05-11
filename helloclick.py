#!/usr/bin/env python
import click


@click.command()
def hello():
    click.echo('Hello World I am livestreaming!')

if __name__ == '__main__':
    hello()

# Text2Test
Testing Framework that implements BDD through Gherkin syntax and makes use of predefined keywords to generate web automated test cases using PyTest and Selenium

## Installation

Download locally the git repository.

Run commands:
1. Function runtext2test {python "path\to\controller.py" $args}
2. Set-Alias -Name text2test -Value runtext2test

## Usage

Create feature files inside the "features" folder.

Run text2test with parameters:
 - Syntax: text2test [-t|all|run|h] [--help]
 - options:
 - h:     Print this Help.
 - help:  Print this Help.
 - t:     Generate a test from a specific feature file.
 - all:   Generate tests from all feature files inside features folder.
 - run:   Execute generated test cases and generate a report.

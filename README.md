# Portfolio Performance
Class that calculates portfolio performance in USD given asset weights in portfolio, asset prices in different currencies and currencies rate to dollar.
Class have the following methods:
- calculate asset performance(start date, end date);
- calculate currency performance(start date, end date);
- calculate total performance(start date, end date).

Each method return pandas.Series with portfolio performances from start date to end date.

## Prerequisits
- [Python 3.7](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)

## Installation
```
pip install pandas
pip install numpy

```

## Tests
test_portfolioPerf.py

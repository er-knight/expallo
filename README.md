## `📄 expallo`
command-line tool to allocate experiments to student on the basis of roll-numbers

## `⚙️ requirements`
`language`
- [`python`](https://www.python.org/) 

`modules` 
- [`json`](https://docs.python.org/3/library/json.html)
- [`csv`](https://docs.python.org/3/library/csv.html) 
- [`argparse`](https://docs.python.org/3/library/argparse.html)

## `🎯 usage`
⦿ format for execution (use `-h` or `--help`).
```
~$ python3 expallo.py <roll-number-start> <roll-number-end> <number-of-experiments> <format>
```
⦿ storing result as `csv`.
```sh
~$ python3 expallo.py 10 40 8 csv
stored in data.csv
```
⦿ storing result as `json`.
```sh
~$ python3 expallo.py 10 40 8 json
stored in data.json
```
⦿ invalid format (other than `csv` and `json`).
```sh
~$ python3 expallo.py 10 40 8 txt
usage: expallo.py [-h] S E N {csv,json}
expallo.py: error: argument F: invalid choice: 'txt' (choose from 'csv', 'json')
```
⦿ creating shortcut with `alias`.
```sh
~$ alias expallo="python3 expallo.py"
```
```sh
~$ expallo 10 40 8 csv
stored in data.csv
```
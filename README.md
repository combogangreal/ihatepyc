# ihatepyc
Automatic __pycache__ folder deleter

## Usage
```bash
$ ihatepyc watch --interval 3 --recursive --verbose
```
The above command will watch the current directory (you change change this by providing a --path /path/to/directory if you want a specific place) every 3 seconds and delete all `__pycache__` folders found within the directory, and sub directories. It will also print out the deleted folders because of the verbose option, you can delete it if needed.

## Installation

```bash

$ pip install ihatepyc

```
or
```bash

$ pip3 install ihatepyc

```

## Help
```bash
$ ihatepyc --help
```
```bash
$ ihatepyc watch --help
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
[combogangreal](https://combogang.com)(contact@combogang.com)(combogang on discord)
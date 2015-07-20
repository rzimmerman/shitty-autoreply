# shitty-autoreply
Irritate people by getting their names wrong. This module provides a `wrong_name` function that returns a name that is close, but not quite the same as the input parameter.


## Installation

```bash
git clone https://github.com/rzimmerman/shitty-autoreply.git
cd shitty-autoreply
python setup.py install
```

## Usage

```python
>> from shitty_autoreply import wrong_name

>> print wrong_name('Robert')
Roberto
>> print wrong_name('Elizabeth')
Elizbeth
>> print wrong_name('Daniel')
Daniele
>> print wrong_name('Jennifer')
Jennings
>> print wrong_name('Steve')
Stevie
>> print wrong_name('Rachel')
Raquel
>> print wrong_name('Joe')
Joell
```

```bash
$ wrong-name Eggs
Egbert
```

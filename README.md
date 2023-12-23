# vt100logging

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![example log feed](https://raw.githubusercontent.com/g2labs-grzegorz-grzeda/vt100logging/main/res/screenshot.png)

The original `logging` package lacks basic coloring of the log output. This does not help when one tries to quickly check on the real time console feed.

`vt100logging` is a simple wrapper around `logging`. Using [VT100 escape](https://www.wikiwand.com/en/ANSI_escape_code#Colors) codes it colors the log feed.

## Supported OS
Tested on MS Win11 and Ubuntu.

## Installation
`pip install vt100logging`

## How to use it
```python
from vt100logging import vt100logging_init, D, I, W, E

vt100logging_init('LOGGED-MODULE', is_verbose=True)

D('example DEBUG message')
I('example INFO message')
W('example WARNING message')
E('example ERROR message')
```

## Contribution
If something is wrong, you can raise issues [here](https://github.com/g2labs-grzegorz-grzeda/vt100logging/issues).

## Copyright
Created by Grzegorz Grzęda. Distributed under MIT license
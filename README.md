# logging-vt100
Python VT100 flavored logging package. Writes to STDOUT with VT100 color escape codes.

## How to use it
Just import the package into your project, `vt100logging_initialize("YOUR LOGGER NAME HERE", is_verbose=<True or False>)` and enjoy the `D(), I(), W(), E()` message levels. The `D()` is for debug purposes and will print only if `is_verbose` was set true.

# Copyright
Created by Grzegorz Grzęda. Distributed under MIT license
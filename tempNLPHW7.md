-2.2
> 0 (0|1)* 111 1?

> Basic string FSTs are defined by text enclosed by double quotes ("). (Note that raw strings, such as those used in filenames, are enclosed by single quotes (') instead.) They can be parsed in one of three ways, which are denoted using a dot (.) followed by either byte, utf8, or an identifier holding a symbol table. Note that within strings, the backslash character (\) is used to escape the next character. Of particular note, \n translates into a newline, \r into a line feed, and \t into the tab character. Literal left and right square brackets will also need escaping, as they are used natively to generate symbols (see below). All other characters following the backslash are uninterpreted, so that we can use \" and \' to insert an actual quote (double) quote symbol instead of terminating the string.


-2.3

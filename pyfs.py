#GNU 3 pyFs

import numpy as np
fs = [];


contents = 0;
i = 0;

def addFile(filename, filecontents):
    global contents;

    fs.insert(contents, filename);
    contents = contents + 1;
    fs.insert(contents, filecontents);
    contents = contents + 1;

def readFile(filename):
    global i;
    while (fs[i] != filename):
        i = i + 1;

    i = i + 1;
    return fs[i];
    i = 0;

def delFile(filename):
    global i;
    while (fs[i] != filename):
        i = i + 1;
    fs[i] = NULL;
    fs[i + 1] = NULL;
    i = 0;
    



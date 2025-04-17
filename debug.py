import pyfs as pfs

pfs.addFile("file0", "file working");
pfs.addFile("file1", "other file working");
f0 = pfs.readFile("file0");
f1 = pfs.readFile("file1");

print(f0);
print(f1);

#*
# okay, i got a working output, i made this file cause the fs kinda broke when i tried it on another device
# then i came to realize, the name was the FIRST argument in the function
# not the second :D
# *
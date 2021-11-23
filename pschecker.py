import sys
from subprocess import Popen, PIPE, STDOUT

if len(sys.argv) != 4:
    print("usage: {} <your> <sol> <num of input files>".format(sys.argv[0]))
else:
    for i in range(int(sys.argv[3])):
        filename = "input{:03d}.txt".format(i)
        f = open(filename, "r")
        contents = f.read()
        f.close()

        p1 = Popen(sys.argv[1].split(" "), stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        p1out = p1.communicate(input=contents.encode())[0].strip().decode()

        p2 = Popen(sys.argv[2].split(" "), stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        p2out = p2.communicate(input=contents.encode())[0].strip().decode()

        if p1out != p2out:
            print("DIFF AT {}".format(filename))
            #print("p1out: {}, p2out: {}".format(p1out, p2out))
import sys

replace = {'\\':'/','file://':'file///'}
for line in sys.stdin:
    for source, target in replace.iteritems():
        line = line.replace(source, target)
    print line

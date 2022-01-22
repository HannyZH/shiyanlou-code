import sys
def Hours(mins):
    '''mins convert to hours mins'''
    if mins < 0:
        raise ValueError
    else:
    #   print("{} H, {} M".format(int(minute / 60), minute % 60))
        print('%s H, %s M' % divmod(mins, 60))
try:
    Hours(int(sys.argv[1]))
except:
    print('Parameter Error')

import sys
def Hours(mins):
'''输入分钟数转化为小时数和分钟数'''
    if mins < 0:
        raise ValueError
    else:
        print('%s H, %s M' % divmod(mins, 60))
try:
    Hours(int(sys.argv[1]))
except:
    print('Parameter Error')

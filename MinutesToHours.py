import sys
def Hours(mins):
'''输入分钟数转化为小时数和分钟数'''
#    hours, minuts = divmod(mins, 60)
    print('%s H, %s M' % divmod(mins, 60))
#    print(str(hours)+' H, '+str(minuts)+' M')
try:
    mins = int(sys.argv[1])
    if mins < 0:
        raise ValueError
except:
    print('Parameter Error')
else:
    Hours(mins)

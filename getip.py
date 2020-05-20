#!/usr/bin/python
# getip after layer domin
# Useage:
# python getip.py layer_domain.txt
import re
import sys,os

def clearIpList(iplist):
    tmpList = list(set(iplist))
    tmpList = sorted(tmpList,key = lambda x: ( int(x.split('.')[0]), int(x.split('.')[1]), int(x.split('.')[2]) ))

    return tmpList

def clearchar(strs):
    restr = ['\n','\r']
    data = strs
    for s in restr:
        data = data.replace(s,'')

    return data

if __name__ == '__main__':
    try:
        import IPy
        from IPy import IP
    except:
        print('Can`t import IPy, Please install it.\n\t python -m pip install IPy')
        exit()
    try:
        ofile = sys.argv[1]
    except:
        print('Usage:\n\tpython getip.py layer_domain.txt')
        exit()

    iplist = []
    ofile = sys.argv[1]

    f = open(ofile, 'r')
    w = open('res_'+ofile,'w+')
    lanfile = open('res_'+ofile[0:-4]+'_lan.txt','w+')
    lines = f.readlines()

    for line in lines:
        line = clearchar(line)
        ips = line.split('\t')[1]
        if ',' not in ips:
            iplist.append(ips)
        else:
            for ipaddress in ips.split(','):
                iplist.append(ipaddress)

    del iplist[0]

    print('\nLan Address:')
    
    iplist = clearIpList(iplist)
    for ipaddress in iplist:
        if IP(ipaddress).iptype() != 'PUBLIC':
            print(ipaddress)
            lanfile.write(ipaddress+'\n')
        else:
            w.write(ipaddress+'\n')

    f.close()
    w.close()
    lanfile.close()

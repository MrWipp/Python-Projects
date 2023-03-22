from time import sleep
import random

sign = '*'
name = 'V0id'

def banner(name, symbol, max):
    symbol = symbol[random.randint(0,len(symbol))]
    index = 0
    sign = str(symbol)
    sign2 = sign*50
    for i in range(0,max):

        if i >= max/2:
            lastword = sign[index].replace(symbol, name)
            word = sign[0:currentindex]+lastword
            sign2+=symbol
            print(word)
            sleep(0.06)
            currentindex-=1
            
        else:
            sign = sign + symbol
            lastword = sign[index].replace(symbol, name)
            word = sign+lastword+sign2
            sign2 = sign2[:-1].strip(symbol)
            print(word)
            index+=1
            sleep(0.06)
            currentindex = i

        
banner('Mr.Wipp', '*', 125)

import Sym_Table as ST
import Data_Structs as DS

Code = []

with open("FILE.asm","r") as ifile:
    lno = 1
    for line in ifile.readlines():
        ST.parse(line,lno)
        lno += 1


for i in ST.Inter_Code:
    global textsize
    if i.oper1[1] in DS.regop and i.oper2[1] in DS.regop:
        val  = str('11'+DS.regop[i.oper1[1]]+DS.regop[i.oper2[1]])
        code = str(i.instop+('%02X' % int(val,2)))
        
    elif(i.oper1[1] in DS.regop and i.oper2[0] == 'SYM' and i.oper2[1] in DS.regop):
        val  = str('00'+DS.regop[i.oper1[1]]+DS.regop[i.oper2[1]])
        code = str(i.instop+('%02X' % int(val,2)))
        
    elif(i.oper1[1] in DS.regop and i.oper2[1] == 'SYM' and i.oper2[1] not in DS.regop):
        val  = str('00'+DS.regop[i.oper1[1]]+DS.regop['ebp'])
        addr = str('['+i.oper2[1]+']')
        code = str(i.instop+('%02X' % int(val,2))+addr)

    elif(i.oper1[1] in DS.regop and i.oper2[0] == 'LIT'):
        val  = str('['+i.oper2[1]+']')
        code = str(i.instop+val)

    elif(i.oper1[0] == 'SYM' and i.oper1[1] not in DS.regop and i.oper2[1] in DS.regop):
        val  = str('00'+DS.regop[i.oper2[1]]+DS.regop['ebp'])
        addr = str('['+i.oper1[1]+']')
        code = str(i.instop+('%02X' % int(val,2))+addr)

    elif(i.oper1[0] == 'SYM' and i.oper1[1] not in DS.regop and i.oper2[0] == 'LIT'):
        addr = str('['+i.oper1[1]+']')
        code = str(i.instop+'05'+addr+i.oper2[1])

    elif(i.oper1[0] == 'SYM' and i.oper1[1] in DS.regop and i.oper2[0] == 'LIT'):
        code = str(i.instop+('%02X' % int(DS.regop[i.oper1[1]],2))+i.oper2[1])

    Code.append(code)


for i in Code:
    print (i)

import json
import Dico_msg_Paco

DMP=Dico_msg_Paco.msg
DMP1=Dico_msg_Paco.msg1
DMP2=Dico_msg_Paco.msg2

print('Le Dico de Paco contient 3 dictionnaires: msg, msg1 et msg2')
print('msg: ',len(DMP),' messages')
print('msg1: ',len(DMP1),' messages')
print('msg2: ',len(DMP2),' messages')

D=''
x=len(DMP)+1
y=len(DMP)+1
while D!='FINI':
    print('Si vous avez fini tapez FINI')
    D=input('Dico 0, 1, ou 2?')
    if D=='0':
        print('pour',x,',')
        I=input('message=  ')
        DMP[x]=I
        x=int(x+1)
    elif D=='1':
        print('pour',y,',')
        I=input('message=  ')
        DMP1[y]=I
        y=int(y+1)
    elif D=='2':
        z=int(input('numero de message ?')) #car len(DMC2) != len(DMC) ou len(DMC1)
        print('pour',z,',')
        I=input('message=  ')
        DMP2[z]=I
    elif D=='FINI':
        break
    else:
        print('Tapez 0, 1, 2 ou FINI')
    print('msg: ',len(DMP),' messages')
    print('msg1: ',len(DMP1),' messages')
    print('msg2: ',len(DMP2),' messages')
    
    


fichier_msg=open('Dico_msg_Paco.py','w')

fichier_msg.write('msg=')
json.dump(DMP,fichier_msg)

fichier_msg.write('\nmsg1=')
json.dump(DMP1,fichier_msg)

fichier_msg.write('\nmsg2=')
json.dump(DMP2,fichier_msg)

fichier_msg.write('\nx=0\nL=list(msg)\nL1=list(msg1)\nL2=list(msg2)') #on convertit les clés de string() en int() pour les utiliser dans P2
fichier_msg.close()
print('Dictionnaires sauvegardés dans Dico_msg_Paco')


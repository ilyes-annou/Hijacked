import json
import Dico_msg_Carla

DMC=Dico_msg_Carla.msg
DMC1=Dico_msg_Carla.msg1
DMC2=Dico_msg_Carla.msg2

print('Le Dico de Carla contient 3 dictionnaires: msg, msg1 et msg2')
print('msg: ',len(DMC),' messages')
print('msg1: ',len(DMC1),' messages')
print('msg2: ',len(DMC2),' messages')

D=''
x=len(DMC)+1
y=len(DMC1)+1
while D!='FINI':
    print('Si vous avez fini tapez FINI')
    D=input('Dico 0, 1, ou 2?')
    if D=='0':
        print('pour',x,',')
        I=input('message=  ')
        DMC[x]=I
        x=int(x+1)
    elif D=='1':
        print('pour',y,',')
        I=input('message=  ')
        DMC1[y]=I
        y=int(y+1)
    elif D=='2':
        z=int(input('numero de message ?')) #car len(DMC2) != len(DMC) ou len(DMC1)
        print('pour',z,',')
        I=input('message=  ')
        DMC2[z]=I
    elif D=='FINI':
        break
    else:
        print('Tapez 0, 1, 2 ou FINI')
    print('msg: ',len(DMC),' messages')
    print('msg1: ',len(DMC1),' messages')
    print('msg2: ',len(DMC2),' messages')
    
    


fichier_msg=open('Dico_msg_Carla.py','w')

fichier_msg.write('msg=')
json.dump(DMC,fichier_msg)

fichier_msg.write('\nmsg1=')
json.dump(DMC1,fichier_msg)

fichier_msg.write('\nmsg2=')
json.dump(DMC2,fichier_msg)

fichier_msg.write('\ny=0\nL=list(msg)\nL1=list(msg1)\nL2=list(msg2)') #on convertit les clés de string() en int() pour les utiliser dans P2
fichier_msg.close()
print('Dictionnaires sauvegardés dans Dico_msg_Carla')



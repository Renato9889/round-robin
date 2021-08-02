#Renato Luiz de Almeida - Trabalho Pratico 2 de Sistemas Operacionais
processos = [5,2,4,6,7,8]
num1 = 5
quantum = 2

def filaround_robin_com_prioridade():
    contadorfila = num1
    frentefila = 1
    while (contadorfila != 0):
        while (processos[frentefila]<=0):
            frentefila = frentefila + 1
            if(frentefila>=num1):
                frentefila = 0
        print('Processo %d vai ser executado com %d segundos'%(frentefila,processos[frentefila]))
        print("Executa até %d segundos (Prioridade)"%(quantum))
        processos[frentefila] = processos[frentefila] - quantum
        if(processos[frentefila]<=0):
            print("Finalizado o processo %d"%(frentefila))
            contadorfila = contadorfila - 1
        else:
            print("Vai para o final da fila com %d de segundos resantes"%(processos[frentefila]))
        frentefila = frentefila + 1
        if(frentefila>num1):
            frentefila = 0


print(":::::::Escalonamento Round-robin com Prioridade :::::::");
filaround_robin_com_prioridade();
print("::::::::: Fim ::::::::::");



import csv
from avaliado import Avaliado 

arquivoin = open('./Feedback360Parser/entrada.csv')
alunoslist = csv.DictReader(arquivoin)
avaliados = []
rotulos = ["RA","PROJETO","IDEIA",
           "NOME1","COMUNICACAO1","COMPROMETIMENTO1","RESULTADO1","MAIS1",
           "NOME2","COMUNICACAO2","COMPROMETIMENTO2","RESULTADO2","MAIS2",
           "NOME3","COMUNICACAO3","COMPROMETIMENTO3","RESULTADO3","MAIS3",
           "NOME4","COMUNICACAO4","COMPROMETIMENTO4","RESULTADO4","MAIS4",
           "NOME5","COMUNICACAO5","COMPROMETIMENTO5","RESULTADO5"]

def avaliadoGetByRa(buscaRa):
    i=0
    pos=-1
    for avaliado in avaliados:
        if (avaliado.raGet()==buscaRa):
            pos=i
        i=i+1
    if(pos!=-1):
        return avaliados[pos]
    else:
        return None


vsite = '1';
venabled = 'enabled'
vtype = 'team'


print("[parsing...]\n")
for alunocsv in alunoslist:
    
    print("\nAVALIADOR =", alunocsv["RA"]) 
    print("PROJETO =", alunocsv["PROJETO"])

    for i in (1, 2, 3, 4, 5) :
        
        existe = avaliadoGetByRa(alunocsv["NOME"+str(i)])

        if(existe == None) :
            novo = Avaliado(alunocsv["NOME"+str(i)])
            novo.avalia(alunocsv["COMUNICACAO"+str(i)], alunocsv["COMPROMETIMENTO"+str(i)], alunocsv["RESULTADO"+str(i)])
            avaliados.append(novo)
        else :
            existe.avalia(alunocsv["COMUNICACAO"+str(i)], alunocsv["COMPROMETIMENTO"+str(i)], alunocsv["RESULTADO"+str(i)])

        if (i==5) : 
            break
        else :
            if(alunocsv["MAIS"+str(i)] == "No"):
                break

#relatorio console
print("\nRelatorio all ---------------") 
for avaliado in avaliados:
    #print(avaliado, "-", avaliado.mediaGet(), "com", avaliado.totalGet(), "de", avaliado.contGet())
    print(avaliado, f"- {avaliado.mediaGet():.1f}" , f"(com {avaliado.mediaComuGet():.1f}, {avaliado.mediaCompGet():.1f} e {avaliado.mediaResuGet():.1f}) de", avaliado.contGet(), "envio.")

#file
arquivoout = open('./Feedback360Parser/saida.txt', 'w')
arquivoout.write("Relatorio all ---------------\n")
for avaliado in avaliados:
    imprime = avaliado.raGet()+ "-"+ str(avaliado.mediaGet())+ "de" + str(avaliado.contGet())
    arquivoout.write(imprime)

print("\n**** FIM")

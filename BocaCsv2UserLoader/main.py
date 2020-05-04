
import csv

arquivoin = open('./BocaCsv2UserLoader/entrada.csv')
alunoslist = csv.DictReader(arquivoin)

vsite = '1';
venabled = 'enabled'
vtype = 'team'

print("[user]\n")
for aluno in alunoslist:
    print("usernumber =", aluno["RA"]) 
    print("usersitenumber =", vsite) 
    print("username =", aluno["RA"]) 
    print("userfullname =", aluno["NOME"]) 
    print("userdesc =", aluno["TURMA"])
    print("usertype =", vtype) 
    print("userpassword =", aluno["RA"]) 
    print("userenabled =", venabled) 
    print("usericpcid =", aluno["RA"]) 
    print("")

arquivoout = open('./BocaCsv2UserLoader/saida.txt', 'w')

arquivoout.write("[user]\n\n")
for aluno in alunoslist:
    arquivoout.write('usernumber = ' + aluno["RA"] + '\n') 
    arquivoout.write("usersitenumber = " + vsite + '\n') 
    arquivoout.write("username = " + aluno["RA"] + '\n') 
    arquivoout.write("userfullname = " + aluno["NOME"] + '\n') 
    arquivoout.write("userdesc = " + aluno["TURMA"] + '\n')
    arquivoout.write("usertype = team\n") 
    arquivoout.write("userpassword = " + aluno["RA"] + '\n') 
    arquivoout.write("userenabled = enabled\n") 
    arquivoout.write("usericpcid = " + aluno["RA"] + '\n') 
    arquivoout.write("\n")

arquivoout.close()



#usernumber	=	37578
#usersitenumber	=	1
#username	=	37578
#userfullname	=	Ricardo Silveira Kasburg
#userdesc	=	CAP2
#usertype	=	team
#userpassword	=	37578
#userenabled	=	enabled
#usericpcid	=	37578

#
#linhas = csv.reader(arquivo)
#for linha in linhas:
#    print(linha)


#fonte/referencia
#https://dicasdepython.com.br/como-ler-arquivos-csv-em-python/

##template

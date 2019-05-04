# Beta 3.0
try:
    def calcula_media(n):
        return (n[0]+((n[1]+n[2]+n[3]+n[4]+n[5]+n[6]+n[7]+n[8]+n[9])/4*9))/10+n[10]
  
    repetir = True
    notas = [0,0,0,0,0,0,0,0,0,0,0]
    tipos_notas = ["\nNota do Simulado: ","Nota A: ","Nota B: ","Nota D: ","Nota E: ","Nota F: ","Nota G: ","Nota H: ","Nota I: ","Nota J: ","Nota de Participação: "]
    novas_notas = "SABDEFGHIJP"
    
    print("\n**Sessão iniciada**")
    
    while repetir == True:
    
        for i in range(len(notas)):
            notas[i] = float(input(tipos_notas[i]))
            while notas[i] < 0 or notas[i] > 10:
                notas[i] = float(input(tipos_notas[i]))
         
        media = calcula_media(notas)
        print("\nMédia = %.2f" %media)
        print("-----------------------------------------")
        
        alterar = True
        while alterar == True:
        
            nota = input("Alterar nota (S/A/B/D/E/F/G/H/I/J/P): ").upper()
            while not(nota in novas_notas):
                print("Nota referente inválida\n")
                nota = input("Alterar nota (S/A/B/D/E/F/G/H/I/J/P): ").upper()   
            
            for i in range(len(novas_notas)):
                if nota == novas_notas[i]:
                    notas[i] = float(input("Insira a nova nota: "))
                    
            for i in range(len(notas)):
                print("%s %.1f" %(tipos_notas[i], notas[i]))
            
            media = calcula_media(notas)
            print("\nMédia = %.2f" %media)
            print("-----------------------------------------")
            
            recalcular = input("Recalcular média novamente?(S/N): ").upper()
            while recalcular != "S" and recalcular != "N":
                print("*Responda S/s ou N/n*")
                recalcular = input("\nRecalcular média novamente?(S/N): ").upper()
            if recalcular != "S":
                alterar = False
                
        encerrar = input("\nCalcular média de outro aluno?(S/N): ").upper()
        while encerrar != "S" and encerrar != "N":
            print("*Responda S/s ou N/n*")
            encerrar = input("\nCalcular média de outro aluno?(S/N): ").upper()
        if encerrar == "N":
            repetir = False
            
        print("-----------------------------------------")
    print("\n**Sessão encerrada**\n**Aperte enter para sair**")

except:
    print("Caractere inválido, reinicie o programa")

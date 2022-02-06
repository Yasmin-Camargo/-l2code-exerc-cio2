import os.path

#abrindo e verificando se o arquivo verb.in existe
if(os.path.isfile('verb.in')):
  entrada = open('verb.in', 'r')
else:
  print('\n -- O arquivo não existe -- \n')
  op = int (input('Deseja criar um arquivo e adicionar palavras? pressione 1\n'))
  if (op == 1):
      #criando um arquivo verb.in 
      entrada = open('verb.in', 'w')
      print ('\nArquivo criado com sucesso')
      op2 = int (input('\nQuantas palavras você deseja adicionar: '))
      cont=0
      #adicionando palavras no arquivo
      while (cont != op2):
          novapalavra = str (input (' Palavra {}: '.format(cont+1)))
          entrada.write(novapalavra)
          entrada.write('\n')
          cont+=1
      entrada.close()
      entrada = open('verb.in', 'r')
  else:
      print('\nDesculpe, o programa não pode ser incializado sem um arquivo de entrada')
      exit() 

#abrindo arquivo de saida no modo escrita
arquivo = open('verb.out', 'w')

#lendo linhas do arquivo
for palavra in entrada:
    palavra = palavra.lower().strip() #removendo espaços excedentes no início e no fim da frase e deixando em minúsculo
    
    #obtendo comprimento das palavras e extraindo o sufixo
    comprimento = int (len(palavra))
    sufixo = palavra[comprimento-4:comprimento]

    #análise da palavra para saber o seu verbo, pessoa e tempo verbal
    print ('{} -'.format(palavra),end=' ',file=arquivo)
    if ('aist' in sufixo):
        print ('verb {}en,'.format(palavra[:comprimento-4]),end=' ',file=arquivo)
        print ('future tense, 5th person',file=arquivo)

    elif ('ons' in sufixo[1:]):
        print ('verb {}en,'.format(palavra[:comprimento-3]),end=' ',file=arquivo)
        print ('present tense, 5th person',file=arquivo)
        
    elif ('est' in sufixo[1:]):
        print ('verb {}en,'.format(palavra[:comprimento-3]),end=' ',file=arquivo)
        print ('past tense, 5th person',file=arquivo)
        
    elif ('ais' in sufixo[1:]):
        print ('verb {}en,'.format(palavra[:comprimento-3]),end=' ',file=arquivo)
        print ('future tense, 2nd person',file=arquivo)

    elif ('aem' in sufixo[1:]):
        print ('verb {}en,'.format(palavra[:comprimento-3]),end=' ',file=arquivo)
        print ('future tense, 4th person',file=arquivo)

    elif ('aim' in sufixo[1:]):
        print ('verb {}en,'.format(palavra[:comprimento-3]),end=' ',file=arquivo)
        print ('future tense, 6th person',file=arquivo)
        
    elif ('os' in sufixo[2:]):
        print ('verb {}en,'.format(palavra[:comprimento-2]),end=' ',file=arquivo)
        print ('present tense, 2nd person',file=arquivo)
        
    elif ('om' in sufixo[2:]):
        print ('verb {}en,'.format(palavra[:comprimento-2]),end=' ',file=arquivo)
        print ('present tense, 4th person',file=arquivo)
        
    elif ('am' in sufixo[2:]):
        print ('verb {}en,'.format(palavra[:comprimento-2]),end=' ',file=arquivo)
        print ('present tense, 6th person',file=arquivo)

    elif ('ei' in sufixo[2:]):
        print ('verb {}en,'.format(palavra[:comprimento-2]),end=' ',file=arquivo)
        print ('past tense, 1st person',file=arquivo)
        
    elif ('es' in sufixo[2:]):
        print ('verb {}en,'.format(palavra[:comprimento-2]),end=' ',file=arquivo)
        print ('past tense, 2nd person',file=arquivo)
        
    elif ('em' in sufixo[2:]):
        print ('verb {}en,'.format(palavra[:comprimento-2]),end=' ',file=arquivo)
        print ('past tense, 4th person',file=arquivo)
        
    elif ('im' in sufixo[2:]):
        print ('verb {}en,'.format(palavra[:comprimento-2]),end=' ',file=arquivo)
        print ('past tense, 6th person',file=arquivo)
        
    elif ('ai' in sufixo[2:]):
        print ('verb {}en,'.format(palavra[:comprimento-2]),end=' ',file=arquivo)
        print ('future tensnd 1st person',file=arquivo)
        
    elif ('o' in sufixo[3:]):
        print ('verb {}en,'.format(palavra[:comprimento-1]),end=' ',file=arquivo)
        print ('present tense, 1st person',file=arquivo)
        
    elif ('a' in sufixo[3:]):
        print ('verb {}en,'.format(palavra[:comprimento-1]),end=' ',file=arquivo)
        print ('present tense, 3rd person',file=arquivo)
        
    elif ('e' in sufixo[3:]):
        print ('verb {}en,'.format(palavra[:comprimento-1]),end=' ',file=arquivo)
        print ('past tense, 3rd person',file=arquivo)
        
    elif ('i' in sufixo[2:]):
        print ('verb {}en,'.format(palavra[:comprimento-1]),end=' ',file=arquivo)
        print ('future tense, 3rd person',file=arquivo)

    else:
        print ('not a verb case',file=arquivo)

#fechando arquivos abertos
arquivo.close()
entrada.close()


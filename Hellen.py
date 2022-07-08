# Hellen assistente virtual , ideia principal e colocar no relogio smart ou ate em outros dispositivos , sendo todos os comandos e respostas por voz , com farias funções , ou seja um pc mini com tudo por voz 
# as funções que tem : calculadora / area do quadradro e circulo / porcentagem / conversões de distancia , peso e liquidos

import pyttsx3 # programa de texto >> fala
# o ! estou usando para na hora de saida de fala ter um pausa maior 
falar=pyttsx3.init()  # inicia o programa 

def robor(robo):      # funçao que pega o que ta escrito 
  falar.say(robo)     # depois transmite em saida de audio 
  falar.runAndWait()

def calculadora(cal):
 while cal==1 :
  robor('Andes de começarmos tenho duas opções :\na primeira é a calculadora basíca com mais , menos , vezes , divisão e potência ! essa é 1 \numero a outra é a calculadora de raiz quadrada  , essa digite 2')
  tipo=int(input('>>'))
  if tipo==1 :
    robor("vamos lá {} , digite o primeiro número ".format(nome))
    numero1=float(input(">>")) 
    robor("sabendo que : + soma , traço subtração , / divisão , *  multiplicação e ** potenciação , agora digite o símbolo da operação desejada , ou se quiser , que eu repita , digite r : ")
    operacao=str(input(">>"))
    robor("o segundo número : ")
    numero2=float(input('>>'))
    if operacao==("+"):
      robor("Resposta é {:.3f} , ir de novo é , 1 , para sair , 0".format(numero1+numero2))
      cal=int(input('>>'))
    elif operacao==("-"):
      robor("Resposta é {:.3f} , ir de novo é , 1 , para sair , 0".format(numero1-numero2))
      cal=int(input('>>'))
    elif operacao==("/"):
      robor("Resposta é {:.3f} , ir de novo é , 1 , para sair , 0".format(numero1/numero2))
      cal=int(input('>>'))
    elif operacao==("*"):
      robor("Resposta é {:.3f} , ir de novo é , 1 , para sair , 0".format(numero1*numero2))
      cal=int(input('>>'))    
    elif operacao==('**'):
      robor("Resposta é {:.3f} , ir de novo é , 1 , para sair , 0".format(numero1**numero2))
      cal=int(input('>>'))
  elif tipo==2 :
    robor('Vamos lá {} ! Diga-me o valor !'.format(nome))
    numero1=float(input('>>'))
    robor('a raiz quadrada de {} é {:.3f} , ir de novo digite 1 , sair  0 !'.format(numero1,numero1**(1/2)))
    cal=int(input('>>'))      

def area(medida) :
   while medida >=1:
    if medida==1 :
      robor("Muito bem , diga-me a primeira medida , ou seja , o valor de um dos lados ")       # tentei colocar area de triangulos , mas como pode ficar confuso o usuario saber como tirar as medidas ,tirei 
      area1=float(input(">>"))
      robor('legal ! , o próximo valor , que seria , o valor do lado oposto ao do primeiro ')
      area2=float(input(">>"))
      robor("A Resposta é {} metros quadrados  , vamos novamente , digite 1 , ou trocar para área de círculos  essa é 2 , se não  ,  para sair é 0".format(area1*area2))
      medida=int(input('>>'))
    elif medida==2 :
      robor("Muito bem , para medir qualquer círculo você tem que saber o valor do diâmetro , que será o que vai colocar ")    
      area1=float(input(">>"))
      resultado=(3.14 * (area1 **2))/4
      robor('A Resposta exata é {} , ou arredondando será {} . quer que eu mostre na tela ? , digite s para sim é numero para não '.format(resultado,round(resultado)))
      resposta=input('>>')
      if resposta==('s'):
        print('Resposta exata é {} , ou arredondando será {}'.format(resultado,round(resultado)))
      robor('se quer fazer outro cálculo , coloque 2 , ir fazer a área de quadrados ou retangulos é 1 , ou para sair é 0')
      medida=int(input('>>'))
   
def porcento(porc) : 
  while porc==1 :
    robor('Bora lá {} , diga-me quantos por centos será calculado , mas não precisa colocar o símbolo'.format(nome))
    por_cento=float(input('>>'))
    robor('bom , agora o valor a ser calculado ')
    numero=float(input('>>'))
    resposta=(numero/100)*por_cento
    robor("Então {}% de {} é iqual a {} , pronto , ir  novamente coloque 1 , já para sair é 0 ".format(por_cento,numero,resposta))
    porc=int(input('>>'))
   
def conversao(conver):
  def retorno(voltar):
    if voltar== 1 :
      conver =1
    elif voltar==2 :
      conver=2
  
  while conver==1 :
    robor('Vamos converter ! Conversões de distância( metro , etc..) é 1 , conversões de pezo( quilo , etc..)  é 2 , conversões de líquidos( lítros , etc..) é 3  , Caso deseje sair  0  ')
    tipo_conversao=int(input('>>'))
    if tipo_conversao==1 or conver==2:
      robor('certo ! conversões de distâncias ! diga-me o valor , mas só o número !')
      valor=float(input('>>'))
      robor('Agora coloque o tipo da conversão que quer , Sabendo que ! k m , é (quilometro) ! só  , m , é (metro) !  , c m  , é (centimetro) !')
      tipo=input(' >>')
      if tipo==('km'):
        metro=valor*1000
        centimetro=valor*(10**4)
        robor('{} quilometros ! ou ! {}  metros ! ou ! {}  centimetros , são a mesma coisa ! quer repetir ? , é 2 . para retorno(aos tipos de conversões é 1 . sair é 0'.format(valor,metro,centimetro))
        print('{} km = {} m = {} cm'.format(valor,metro,centimetro))
        retorno(int(input('>>')))
      elif tipo==('m'):
        quilometros=valor/1000
        centimetro=valor*100
        robor('{} quilometros ! ou ! {}  metros ! ou ! {}  centimetros ! são a mesma coisa ! quer repetir ? , é 2 . para retorno(aos tipos de conversões é 1 . sair é 0'.format(quilometros,valor,centimetro))
        print('{} km = {} m = {} cm'.format(quilometros,valor,centimetro))
        retorno(int(input('>>')))
      elif tipo==('cm'):
        quilometros=valor/(10**4)
        metro=valor/100
        robor('{} quilometros ! ou ! {}  metros ! ou ! {}  centimetros ! são a mesma coisa ! quer repetir ? , é 2 . para retorno(aos tipos de conversões é 1 . sair é 0'.format(quilometros,metro,valor))
        print('{} km = {} m = {} cm'.format(quilometros,metro,valor))
        retorno(int(input('>>')))
    elif tipo_conversao==2 or conver==3:
      robor('boa ! {} !, bora medir o pezo ! coloque o valor , mas só o número'.format(nome))
      valor=float(input('>>'))
      robor('Agora coloque o tipo da conversão desejada ! Sabendo que ! t , é (tonelada) . k  g , é (quilo) . e , g , é (grama) ')
      tipo=input('>>')
      if tipo==('t'):
        quilos=valor*1000
        grama=valor*(10**5)
        robor('{} toneladas ! ou ! {} quilos ! ou ! {}  gramas ! são a mesma coisa ! vai de novo ? , 1 ! para sim ! 3 ! para retorno(aos tipos de conversões ! e 0 ! para sair '.format(valor,quilos,grama))
        retorno(int(input('>>')))
      elif tipo == ('kg'):
        ton=valor/1000
        grama=valor*1000
        robor('{} toneladas ! ou ! {} quilos ! ou ! {}  gramas ! são a mesma coisa ! vai de novo ? , 1 ! para sim ! 3 ! para retorno(aos tipos de conversões ! e 0 ! para sair  '.format(ton,valor,grama))
        retorno(int(input('>>')))
      elif tipo == ('g') :
        ton=valor/(10**5)
        quilos=valor/1000
        robor('{} toneladas ! ou ! {} quilos ! ou ! {}  gramas ! são a mesma coisa ! vai de novo ? , 1 ! para sim ! 3 ! para retorno(aos tipos de conversões ! e 0 ! para sair  '.format(ton,quilos,valor)) 
        retorno(int(input('>>')))
    elif tipo_conversao== 3 or conver==4:
      robor('que legal ! líquidos ! diga-me só o numero ! ')
      valor=int(input('>>'))
      robor('muito bom ! digite o tipo da conversão . sabendo que ! m , 3 é mretro cúbico . l , prara litro . m , l para mililitros  ')
      tipo=input('>>')
      if tipo== ('m3'):
        litro=valor*1000
        mililitro=valor*(10**5)
        robor('{} metros cúbicos ! ou ! {} litros ! ou ! {} mililitros ! são a mesma coisa ! fazer novamente ? é 1 ')
    elif tipo_conversao==0:
      conver=0  


robor("Olá ! Meu nome é Hellem , sua assistente virtual , prazer em ti conhecer")                                                   # eliminar no estado final 
robor("Qual seu nome ? ")
nome=input(">>")
robor(nome+", que nome lindo ! O que deseja fazer {}? ".format(nome))
robor("Usar a calculadora ? digite 1 , se não digite 0 ")
calculadora(int(input('>>')))
robor('Quer medir á área ? digite 1 para sim e 0 para não ')
calcular=int(input('>>'))
if calcular ==1 : 
 robor("área de algo quadrado ou retangular , digite 1 , ou de círculos , digite 2 ")   # colocar se o usuario sabe como tirar as medidas e se estao em mesma casa de medida :cm,m,km...
 area(int(input('>>')))
robor('Talvez saber a porcentagem de um número ? já sabe 1 é sim e 0 é não ')
porcento(int(input('>>')))
robor('Bora pra outra opção , Que tal conversões , {} ? que é converter metros em kilometros e muito mais.... , 1 sim , 0 não ! '.format(nome))
conversao(int(input('>>')))
robor('por enquanto é só. tchau !')

#Bovenzo cli

##Considerações

### Mensagem de impacto para dramatizar uma verdade
 Sua vida pode ser mais simples se você automatizar as partes chatas.


###Motivação
Basicamente acordei num dia e notei quantas coisas chatas eu faço e que me gastam um certo tempo digitando tudo.
Eu poderia simplesmente automatizar aos poucos tudo que eu faço de repetitivo.

##Instalação

Quando eu por o setuptools fica mais facil, até lá, execute os comandos:

1) `cd <diretorio/do/projeto/bovenzo-cli/>` 
2) `PATH_CLI=(pwd)` -  para pegar o path full que chamaremos agora de **PATH_CLI**
3) ` ln -s PATH_CLI/bovenzo.py /usr/local/bin/bovenzo`
4) (opcional) Caso queira ter a cli acessando pelo comando de `bo` e `bovenzo`, execute o step a seguir
5) (opcional) `ln -s PATH_CLI/bovenzo.py /usr/local/bin/bo`


#FAQ

Não está conseguindo executar a cli por algum motivo?
    você pode permissionar o arquivo bovenzo.py com `chmod +x /path/do/bovenzo-cli/bovenzo.py`
Com isso você evitará diversos problemas
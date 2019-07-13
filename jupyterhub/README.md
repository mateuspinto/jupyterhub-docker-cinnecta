# [Docker] JupyterHub autenticado pelo Github
Imagem de Docker completa do JupyterHub com todos os pacotes base Anaconda Python3 para codificação de múltiplos desenvolvedores em um cluster, com ambientes individuais de arquivos e uma pasta compartilhada entre todos, além da biblioteca PySpark, que permite a manipulação de dados com  o alto grau de paralelismo do Apache Sparky. Toda a autenticação é feita pelo próprio Github.

![enter image description here](https://i.imgur.com/24DhsSk.png)


## Motivação
Devido a constantes avanços da computação, especialmente da realizada em nuvem, e graças também a mudanças na forma que o mercado de trabalho se organiza, cada vez mais o processamento de dados em nuvem mostra-se como o caminho mais interessante a ser seguido, devido a ser 100% compatível com o homeworking e também por ser mais barato mesmo para trabalho em empresas físicas, que muitas vezes se veem amplamente mais dispostas a alugar um servidor como os da AWS ou Azure do que arcar com um próprio, e mesmo um próprio requer uma solução inteligente que use e abuse de paralelismo. Para isso, foi desenvolvido uma solução para a Cinnecta em parceria com o NESPeD (Núcleo de Estudos em Sistemas Pervasivos e Distribuídos), que permite que vários desenvolvedores trabalhem juntos tendo sua própria área de trabalho privada, podendo compartilhar arquivos entre si, seja de casa, utilizando qualquer sistema operacional ou até mesmo do celular, ou na empresa/universidade em si, e utilizando todo o processamento da máquina instalada.

## Pré-requisitos para instalação no servidor

● [Docker.io](https://www.docker.com/)  
● Sistema operacioal Linux LTS (Ubuntu preferencialmente) - não necessário, mas extremamente recomendado  
● [Docker Compose](https://docs.docker.com/compose/) - não necessário, mas recomendado  
● Git (para clonar o repositório)

## Okay, legal, mas não há um executável. Como posso instalar isso no servidor?

1 - Verifique a instalação dos componentes usando o comando abaixo:

    sudo apt install docker.io docker-compose git
 
2 - Em seguida, clone o repositório na sua máquina/servidor:

    git clone https://github.com/mateusps10/JupyterHub_Complete_Docker

3 - Vá para a pasta do JupyterHub:

    cd jupyterhub
    
4 - Proceda com a instalação usando o makefile:

    make
5 - [OPCIONAL] Caso queira manter a persistencia de arquivos, crie os volumes do Docker com o comando abaixo:

    make volume
 
6 - Crie um container e execute o JupyterHub:

    make run

## Como utilizar [usuário comum]
0 - Envie para o adminstrador sua conta do GitHub para que ele adicione permissões para você.  
  
1 - Acesse o link/IP dado e proceda com o login usando sua conta do GitHub.  
  
2 - Você verá uma tela semelhante a do Jupyter Notebook. É possível enviar arquivos, criar notebooks ou terminais (do Linux). Todos os arquivos da sua pasta são privados, e somente você ou o Root podem acessá-los, embora seus processos podem ser finalizados por qualquer administrador.  
  

### Exemplo 1: Clonando repositório do Git (qualquer um)
1 - Vá em New:

![Cria um novo processo dentro da sua área de trabalho](https://i.imgur.com/gIj6K5H.png)

2 - Terminal:

![enter image description here](https://i.imgur.com/lMC0oSa.png)

3 - Digite o comando padrão "git clone " seguido do link do repositório desejado e aperte Enter:

![enter image description here](https://i.imgur.com/kkQ6zPh.png)

4 - O conteúdo desejado deverá aparecer numa pasta com o mesmo nome do repositório na sua pasta padrão de usuário:

![enter image description here](https://i.imgur.com/mUeEeKI.png)

### Exemplo 2: Git add, commit, push ou pull através do JupyterHub

1 - Utilizando qualquer repositório previamente clonado de qualquer Git, clique em New:

![enter image description here](https://i.imgur.com/75lK4FR.png)

2 - Clique em Terminal:

![enter image description here](https://i.imgur.com/GXwb92d.png)

3 - Dê "cd " seguido do nome do repositório desejado. A partir disso, é possível usar qualquer comando desejado dos Gits:

![enter image description here](https://i.imgur.com/KNyiQ7a.png)

## Compartilhamento de arquivos entre desenvolvedores

É possível compartilhar arquivos entre todos os desenvolvedores somente através do Terminal, devido uma incapacidade do próprio JupyterHub.

### Adicionando novos arquivos compartilhados

1 - Clique em New:

![enter image description here](https://i.imgur.com/75lK4FR.png)

2 - Clique em Terminal:

![enter image description here](https://i.imgur.com/GXwb92d.png)

3 - Utilize o comando "cd /shared/" para ir até a pasta compartilhada:

![enter image description here](https://i.imgur.com/uzW8FFw.png)

4 - Os arquivos dessa pasta são acessíveis por todos. Para adicionar, é possível usar o "wget" do Linux, "cp" para copiar arquivos da sua área de trabalho, "git clone" e afins.  

### Utilizando arquivos compartilhados

Para evitar redundância, é preferível acessar os arquivos da pasta Shared diretamente, ao invés de copiá-los. 

1 - Para isso, crie um novo Notebook ou use algum de sua preferência. Clique em New:

![enter image description here](https://i.imgur.com/75lK4FR.png)

2 - E na parte Notebook, escolha Python 3 (ou outra linguagem de sua preferência que esteja disponível):

![enter image description here](https://i.imgur.com/f9ew6M1.png)

3 - Usando o comando desejado de entrada de arquivo, utilize o caminho absoluto "/shared/ARQUIVO":

![enter image description here](https://i.imgur.com/qVatGPP.png)

## Como utilizar [administrador]

1 - Clique em Control Panel:

![enter image description here](https://i.imgur.com/lQPbCbr.png)

2 - Clique em Admin:

![enter image description here](https://i.imgur.com/RZgTKkP.png)

3 - Aqui é possível interromper os processos, dar administrador para outros usuários, ou iniciar áreas de trabalho de outros desenvolvedores de forma bastante intuitiva:

![enter image description here](https://i.imgur.com/yl1JTx9.png)
> Written with [StackEdit](https://stackedit.io/).

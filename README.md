# Sistema bancário *_PyBank_*.

### Projeto criado no módulo de fundamentos do curso de Python da DIO.me. O Desafio consiste em criar um sistema bancário em python segindo com as funcionalidades e regras de negócio abaixo listadas.
#

## Funcionalidades:

  * Sacar
  * Depositar
  * Visualizar Extrato
  * Criação de usuários
  * Criação de conta corrente
    
## Regras de Negócio:

  * Não é permitido depositar valores negativos
  * registrar todos os saques e depositos realizados
  * Limite de 3 saques por dia
  * Limite de R$500,00 por saque
  * Ao solicitar o extrato, deverá ser exibido todas as operações e o saldo atual da conta
  * Não podem existir dois usuários com o mesmo CPF
  * O mesmo CPF pode conter mais de uma conta associada
  * Determinada conta só pode estar associada a um único usuário
  * Só é permitida a criação de uma conta para CPF's já cadastrados no sistema

## Etapadas do Desenvolvimento

  * Inicialmente o sistema foi desnevolvido seguindo os conhecimentos básicos adquiridos no módulo de fundamentos;
  * Posteriomente foram adcionadas novas regras de negócio e tornou-se necessário implementar funções no sistema;
  * Ao finalizar o módulo de POO, o sistema passou por uma reformulação:
    * Os dados dos clientes passaram a ser armazenados em objetos, substituindo a implementação anterior que armazenava essas infomrações em dicionários;
    * O modelo de classes seguiu o diagrama UML abaixo:
      ![Diagrama UML](./UML.png)
    
    * Foi implementado o conceito de atributos públicos e privados;
    * Foram implementados métodos às classes;

## Próximos passos
  
  * Futuramente o sistema irá ganhar uma implementação para armazenar as informações em um banco de dados MySQL;
  * Sera criado uma interface Desktop e uma implementação web;

<br>

## 🛠 Techs Stack

  <div style="display: inline_block"><br>
  <img align="center" alt="Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
</div>



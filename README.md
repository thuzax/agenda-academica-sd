## Agenda Acadêmica

# Configurações

Primeiro deve-se ter instalado o gerenciador de bibliotecas do python, o pip3.
Para instalar as bibliotecas necessárias para a execução do sistema utilize o comando abaixo:

$ pip3 install -r requirements.txt

Feito isso configure o servidor master com o ip 192.168.43.134 e o slave com 192.168.43.82
Caso deseje aumentar o número de máquinas ou alterar os ips, modifique também a classe banco de dados do aplicativo android e o arquivo ip-config.txt.

Nos arquivos DAO do Slave, conecte-se ao host master nas operações de escrita ao invés do localhost (127.0.0.1) que é o padrão.

Também é necessário estabelecer a conexão master-slave utilizando o mysql.

# Execução

Primeiro execute o servidor Master com o seguinte comando:

$ python3 Connect.py

Após isso execute nos slaves o mesmo comando.

Como a aplicação ainda não fornece a insersão de grupos pelo aplicativo, é necessário inserí-lo usando a interface de testes. Para executá-la utilize o comando:

$ python3 tester.py

# Desenvolvedores
@silventino
@thuzax
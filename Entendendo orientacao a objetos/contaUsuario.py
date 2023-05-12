from time import sleep as loading
class ContaUsuario:

    #esta função serve para nós definirmos quais as variaveis (atributos) que vão ser usados para manipulação dela, o "__init__" define que ela sera executada na sua iniciação (Para criar uma nova conta de usuario, devemos usar o nome da classe e inicializar as variaveis dentro dela). e o self pode ser encarado como "this.object" do java
    def __init__(self, numero_Da_Conta: str, titular_Da_Conta: str, saldo_Da_Conta: float, limite_Da_Conta: float):
        self.__numero_Da_Conta = numero_Da_Conta
        self.__titular_Da_Conta = titular_Da_Conta
        self.__saldo_Da_Conta = saldo_Da_Conta
        self.__limite_Da_Conta = limite_Da_Conta
        #Explicação rapida: "self.__(nome da variavel) = (nome da variavel)" representa o seguinte: a variavel da classe vai ser igual a variavel passada pela pessoa. 

    #Agora definimos getters & setters para que possamos acessar os atributos da classe
    #para os getters, existem 2 declarações possiveis: @property ou @nome da variavel.getter (caso estejamos aplicando verificações OU contas etc) e os setters apenas a opção @nome da variavel.setter
    
    @property
    def numero_Da_Conta(self):
        return self.__numero_Da_Conta
    
    @property
    def titular_Da_Conta(self):
        return self.__titular_Da_Conta
    
    @property
    def saldo_Da_Conta(self):
        return self.__saldo_Da_Conta

    @property
    def limite_Da_Conta(self):
        return self.__limite_Da_Conta
    
    @limite_Da_Conta.setter
    def limite_Da_Conta(self, limite_Da_Conta: float):
        self.__limite_Da_Conta = limite_Da_Conta

    #Em seguida criamos algumas funções RELATIVAS A CONTA DO USUARIO, SEM FUGIR DA IDEIA DE CONTA
    #Este primeiro método é um exemplo de método Estático em pyhton, ele é basicamente acessado sem a necessidade de criar o objeto.
    @staticmethod
    def bancos_Disponiveis():
        return {'ITAU': "0092", 'SANTANDER': "0087", 'BRADESCO': "0063", 'NEXT': "0054"}

    def exibir_Extrato_Da_Conta(self):

        print("| INFORMAÇÕES DO CLIENTE {} |".format(self.__titular_Da_Conta))
        print("")
        print("+--> Saldo em conta: {}".format(self.__saldo_Da_Conta))
        print("+--> Limite em conta: {}".format(self.__limite_Da_Conta))
        print("+--> Saldo + Limite em conta: {}".format(self.__limite_Da_Conta + self.__saldo_Da_Conta))
        print("+--> Numero da conta: {}".format(self.__numero_Da_Conta))

    def depositar_Valor(self, valor_Para_Depositar: float):

        print(">> Valor em conta atual: {}".format(self.__saldo_Da_Conta))
        print("Depositando valor em conta... ")
        loading(2)
        
        self.__saldo_Da_Conta += valor_Para_Depositar
        print("Valor depositado com sucesso!\nTotal em conta: {}".format(self.__saldo_Da_Conta))
    
    #Este é um método privado, que não deve ser acessado por ninguém além do proprio programa, estamos usando o mesmo para APENAS verificar se o cliente tem saldo suficiente para realizar algumas transações
    def __verificar_limite_operacao(self, valor_Da_Operacao: float):
        
        limite_De_Transacao = self.__saldo_Da_Conta + self.__limite_Da_Conta
        return valor_Da_Operacao <= limite_De_Transacao

    def sacar_Valor(self, valor_Para_Sacar: float):

        print(">> Valor em conta atual: {}".format(self.__saldo_Da_Conta))
        print("Sacando valor em conta... ")
        loading(2)
        
        if(self.__verificar_limite_operacao(valor_Para_Sacar)):
            
            self.__saldo_Da_Conta -= valor_Para_Sacar
            print("Valor sacado com sucesso!\nTotal em conta: {}".format(self.__saldo_Da_Conta))
        else:
            print("Infelizmente, você não possui limite suficiente para operação\n+--> Limite: {} | {} <--+ Valor da operação".format(self.__saldo_Da_Conta + self.__limite_Da_Conta, valor_Para_Sacar))

    def transferir_Valores(self, conta_Destino, valor_Transferido):
        
        print("Valor sendo transferido... ")
        loading(2)

        if(self.__verificar_limite_operacao(valor_Transferido)):
            
            self.sacar_Valor(valor_Transferido)
            conta_Destino.depositar_Valor(valor_Transferido)
            print("\nValor transferido com sucesso, exibindo agora extrato da conta.")  
        else:
            print("Infelizmente, você não possui limite suficiente para operação\n+--> Limite: {} | {} <--+ Valor da operação".format(self.__saldo_Da_Conta + self.__limite_Da_Conta, valor_Transferido))
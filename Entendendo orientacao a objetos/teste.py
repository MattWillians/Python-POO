

def criar_Conta(numero_Da_Conta, titular_Da_Conta, saldo_Da_Conta, limite_Da_Conta):
    conta_Criada = {"numero_Da_Conta": numero_Da_Conta, "titular_Da_Conta": titular_Da_Conta, "saldo_Da_Conta": saldo_Da_Conta, "limite_Da_Conta": limite_Da_Conta}
    return conta_Criada

def depositar_Dinheiro(conta_Usuario, valor_Depositado):
    conta_Usuario["saldo_Da_Conta"] += valor_Depositado

def sacar_Dinheiro(conta_Usuario, valor_Sacado):
    conta_Usuario["saldo_Da_Conta"] -= valor_Sacado

def exibir_Info_Conta(conta_Usuario):
    print("+---------------------------+")
    print("| INFORMAÇÕES DO CLIENTE {} |".format(conta_Usuario["titular_DaConta"]))
    print("+---------------------------+")
    print("+--> Saldo em conta: {}".format(conta_Usuario["saldo_Da_Conta"]))
    print("+--> Limite em conta: {}".format(conta_Usuario["limite_Da_Conta"]))
    print("+--> Numero da conta: {}".format(conta_Usuario["numero_Da_Conta"]))

#--------------------------------------------------------------------#

def formatar_data(dia, mes, ano):
    
    print("{}/{}/{}".format(dia, mes, ano))

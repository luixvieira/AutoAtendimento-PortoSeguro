from random import * #import para para gerar um numero de ID aleatorio
from datetime import date #Import para mostrar a data atual da reforma
prontuarios = [""] 

def linhas_titulo(txt):
    print("=" * 60) #obrigado por me ensinar isso professor guanabara
    print(txt)
    print("=" * 60)
    

def exibir_menu():
    linhas_titulo("Bem vindo ao sistema de auto atendimento Porto!")
    print("Selecione o tipo de usuário:")
    print("1. Mecânico Porto")
    print("2. Segurado Porto")
    tipo_usuario = input("Digite o número da opção desejada: ")

    if tipo_usuario == "1":
        exibir_menu_mecanico()
    elif tipo_usuario == "2":
        exibir_menu_segurado()
    else:
        print("Opção inválida. Tente novamente.")

def exibir_menu_mecanico():
    #print("\nMenu Mecânico Porto:")
    linhas_titulo("Menu Mecanico Porto")
    print("1. Visualizar prontuário de um carro")
    print("2. Adicionar uma reforma ao prontuário")
    print("3. Visualizar pré-diagnóstico feito")
    opcao = input("\nDigite o número da opção desejada: ")
    
    if opcao == "1":
        visualizar_prontuario()
    elif opcao == "2":
        adicionar_reforma()
    elif opcao == "3":
        visualizar_pre_diagnostico()
    else:
        print("Opção inválida. Tente novamente.\n")
        exibir_menu_mecanico()
        
def adicionar_reforma():
    placa = input("Digite a placa do carro: ").upper() #Fazer com que deixe todas as letras maiusculas
    id_carro = input("Digite o ID do carro: ")

    # Validação da placa (ver se a placa foi digitada no formato correto)
    if not placa.isalnum() or len(placa) < 7 or len(placa) > 7:
        print("Placa inválida. Digite no formato ABC-1234.")
        return

    # Validação do ID do carro (apenas números)
    if not id_carro.isdigit():
        print("ID do carro errado. Digite apenas números.")
        return

    #No momento ainda nao temos um banco de dados para verificar se o carro existe, mas quando possuirmos, essa seria a logica:
    
    #carro_encontrado = True
    #if not carro_encontrado:
        print(f"Carro com placa {placa} e ID {id_carro} não encontrado.")
        return

    descricao = input("Digite a descrição da reforma: ")

    # Validação da descrição (ver se a descrição nao esta vazia)
    if not descricao:
        print("Descrição da reforma não pode ser vazia.")
        return
    
    # Gerar um id para a reforma de 5 digitos
    id_reforma = randint(10000,90000)

    # mostrar o resumo da reforma
    linhas_titulo("Resumo da reforma")
    print(f"Placa do Carro: {placa} \n Id do carro: {id_carro} \n Id da reforma: {id_reforma} \n Descrição: {descricao}")

    # Confirmação do cadastro
    confirmar = input("Deseja confirmar o cadastro da reforma? (S/N): ").upper()
    
    if confirmar == "S":
        print(f"Reforma cadastrada com sucesso! ID: {id_reforma}")
        exibir_menu()
        #Atualizando a lista de prontuarios
        global prontuarios
        prontuarios.extend ([f"Placa do Carro: {placa} \n Id do carro: {id_carro} \n Id da reforma: {id_reforma} \n Descrição: {descricao} data: {date.today()} "])

    else:
        print("Cadastro da reforma cancelado.")
        exibir_menu_mecanico()
        
def visualizar_prontuario():
    for i in prontuarios:
        print(i)
        
def visualizar_pre_diagnostico():
    placa_consulta = (input("Digite a placa do carro que deseja visualizar o pré prontuario"))


def exibir_menu_segurado():
    print("\nMenu Segurado Porto:")
    print("1. Registrar problemas do carro")
    print("2. Realizar diagnóstico")
    print("3. Sair")
    opcao = input("\nDigite o número da opção desejada: ")
    
def registrar_problemas():
    problemas = input("\n Digite os problemas do carro (separados por vírgula): \n")
    problemas_registrados.extend(problemas.split(", ")) #Adicionando cada problema na lista com o .extend
    print("Problemas registrados:", problemas_registrados)
    return problemas_registrados

def realizar_diagnostico(problemas):
    if "motor" in problemas:
        print("\nPossível problema: motor com defeito\n")
    elif "pneu" in problemas:
        print("Possível problema: pneu danificado\n")
    else:
        print("Não foi possível determinar o problema com base nos dados fornecidos. Entre em nosso site para marcar uma avaliação presencial\n")

problemas_registrados = []

def main():
    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            problemas_registrados.extend(registrar_problemas())
            print("Problemas registrados:", problemas_registrados)
        elif opcao == "2":
            if not problemas_registrados:
                print("É necessário registrar os problemas antes de realizar o diagnóstico.\n")
            else:
                realizar_diagnostico(problemas_registrados)
        elif opcao == "3":
            print("Encerrando o programa. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()

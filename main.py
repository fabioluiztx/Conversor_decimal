 opcao_menu = int(input("\nBem vindo ao conversor de Decimais.\nEscolha abaixo a opção que deseja executar:\n[1] Fazer a conversão do decimal - \n[2] Saber mais sobre o projeto - [3] Sair \n"))

#validação das opções
while opcao_menu != 1 and opcao_menu != 2:
    print("A opção '", opcao_menu, " não é uma opção validá, leia com atenção e tente novamente.")
    opcao_menu = int(input("\nEscolha abaixo a opção que deseja executar:\n[1] Fazer a conversão do decimal \n[2] Saber mais sobre o projeto \n[3] Sair \n"))
    

#repetir o programa
while opcao_menu != 3 or opcao_menu == 0: 

    #Caso o usuario escolha essa opção, iremos executar as conversões solicitadas
    if opcao_menu == 1: 
        num_a_converter = int(input("\nDigite o numero em decimal: \n"))
        num_antigo = num_a_converter
        base = int(input("\nEscolha para qual base deseja converter:\n[1] Binario - [2] Octal - [3] Hexadecimal \n"))
        
        #validação das opções
        while base != 1 and base != 2 and base != 3:
            print("A opção '", base, "' não é uma opção validá, leia com atenção e tente novamente.")
            base = int(input("\nEscolha para qual base deseja converter:\n[1] Binario - [2] Octal - [3] Hexadecimal \n"))
            
        #Caso o usuario escolha essa opção, iremos converter decimal em binário
        if base == 1:
            num_convertido = str(num_a_converter % 2)
            num_a_converter = int(num_a_converter / 2)
            while num_a_converter > 0:
                num_convertido = str(num_a_converter % 2) + num_convertido
                num_a_converter = int(num_a_converter / 2)
            print("O numero", num_antigo, "Convertido em Binario é: ", num_convertido)
            
        #Caso o usuario escolha essa opção, iremos converter decimal em octal
        elif base == 2:
            num_convertido = str(num_a_converter % 8)
            num_a_converter = int(num_a_converter / 8)
            while num_a_converter > 0:
                num_convertido = str(num_a_converter % 8) + num_convertido
                num_a_converter = int(num_a_converter / 8)
            print("O numero", num_antigo, "Convertido em Octal é: ", num_convertido)
            
        #Caso o usuario escolha essa opção, iremos converter decimal em hexadecimal
        elif base == 3:
            num_convertido = int(num_a_converter % 16)
            if num_convertido > 9:
                if num_convertido == 10:
                    num_convertido = 'A'
                if num_convertido == 11:
                    num_convertido = 'B'
                if num_convertido == 12:
                    num_convertido = 'C'
                if num_convertido == 13:
                    num_convertido = 'D'
                if num_convertido == 14:
                    num_convertido = 'E'
                if num_convertido == 15:
                    num_convertido = 'F'
            else:
                num_convertido = str(num_a_converter % 16)
                num_a_converter = int(num_a_converter / 16)
            while num_a_converter > 0:
                num_a_adicionar = int(num_a_converter % 16)
                if num_a_adicionar > 9:
                    if num_a_adicionar == 10:
                        num_a_adicionar = 'A'
                    if num_a_adicionar == 11:
                        num_a_adicionar = 'B'
                    if num_a_adicionar == 12:
                        num_a_adicionar = 'C'
                    if num_a_adicionar == 13:
                        num_a_adicionar = 'D'
                    if num_a_adicionar == 14:
                        num_a_adicionar = 'E'
                    if num_a_adicionar == 15:
                        num_a_adicionar = 'F'
                else:
                    num_a_adicionar = str(num_a_converter % 16)
                num_convertido = num_a_adicionar + num_convertido
                num_a_converter = int(num_a_converter / 16)
            print(f'O número {num_antigo} em Hexadecimal é {num_convertido}')
            

    #Caso o usuario escolha essa opção, iremos exibir as informações sobre o projeto
    elif opcao_menu == 2: 
        print("Projeto Interdisciplinar do curso de Análise e Desenvolvimento de Sistemas da Universidade Cruzeiro do Sul - Turma 4D (Noturna).", "\n\nProgramadores:\nGabriel Gustavo Silva de Souza - RGM: 27422623.\nFabio Luiz Teixeira – RGM: 28031270O.", "\n\nDisciplinas:\nEste tema fora escolhido para demonstrar os conhecimentos adquiridos nas aulas de Organização e Arquitetura de Computadores\ne Programação de Computadores por meio da construção e desenvolvimento de um software na linguagem de programação Python.", "\n\nOrientadores:\nProf. Vera Lucia Almeida Forbeck.\nProf. Alvaro Andre Colombero Prado.", "\n\nConversor de decimais - Versão 1.1.0.0 - 2023®™\n")
        

    #Caso o usuario escolha essa opção, iremos lhe mostrar uma mensagem de agradecimento e encerraremos o programa
    else: 
        print("\nAgradecemos a utilização do nosso programa, até breve! :)", "\nPrograma encerrado.\n")
        exit()
    opcao_menu = int(input("\nDeseja encerrar o programa?\n[0] Sim - [1] Não\n"))




    ###Projeto realizado por:
    ###Fabio Luiz Teixeira            – RGM: 28031270O
    ###Gabriel Gustavo Silva de Souza - RGM: 27422623
    ###Turma de Análise e Desenvolvimento de Sistemas da Universidade Cruzeiro do Sul - Campus Analia Franco - Turma 1º/4ºD (Quinta-feira - Noturno)
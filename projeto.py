import os;
import time;

login = [];
senha = [];
login_test = [];
senha_test = [];
menu = "Menu da Academia";
cadastro = 5;

print("""                      Academia Sistema Linear """);
print("\n");

print(menu.center(66, "-"));
print();

escolha = 1;

while(escolha != 4):
    print("Seleciona uma das alternativas abaixo: ");
    print("Realizar cadastro de 5 pessoas [1]");
    print("Verificar cadastro de uma pessoa [2]");
    print("Excluir um cadastro [3]")
    print("Para sair [4]");
    print();

    escolha = int(input());

    print();

    if(escolha == 1):
        for i in range(cadastro):
            print(i+1,"º usuário")
            login.append(input("Digite o login: "));
            senha.append(input("Digite a senha: "));
            print();

        print("Cadastro de usuários realizado com sucesso.");
        time.sleep(3);
        os.system("cls");

        login_test = login.copy();
        senha_test = senha.copy();
        login.clear();
        senha.clear();


    elif(escolha == 2):

        print();
        print("Área de Login: ");
        print();

        usuario = input("Digite seu login: ");

        if(usuario in login_test):
            password = input("Digite sua senha: ");
            if(password in senha_test):
                print("Usuário cadastrado.");
                time.sleep(3);
                os.system("cls");
            else:
                print("Senha inválida.");
                time.sleep(3);
                os.system("cls")
        else:
                print("Usuário inválido.");
                time.sleep(3);
                os.system("cls");
    elif(escolha == 3):
        
        print("Digite o usuário que deseja retirar do sistema: ");
        usuario = input();
        if(usuario in login_test):
            for i in range(len(login_test)):
                if(usuario == login_test[i]):
                    login_test[i] = "";
                    senha_test[i] = "";
                    print();
                    print("Usuário retirado do sistema com sucesso.");
                    time.sleep(3);
                    os.system("cls");
        else:
            print("Usuário não encontrado em nosso sistema.");
            time.sleep(3);
            os.system("cls");
    
    elif(escolha == 4):
        print("Encerrando o programa.");
        time.sleep(3);
        os.system("cls");
    
    else:
        print("Digite uma das opções.");
        time.sleep(3);
        os.system("cls");

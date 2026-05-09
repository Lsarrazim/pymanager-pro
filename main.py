SYSTEM_NAME = "PyManager Pro"
VERSION = "1.0.0"

from core.auth import register_user

def show_header():
    print("=" * 40)
    print(f" {SYSTEM_NAME} - v{VERSION}")
    print("=" * 40)

def show_main_menu():
    print("\n [1] ENTRAR NO SISTEMA")
    print("\n [2] CRIAR CONTA")
    print("\n [0] SAIR")

    print()

def get_user_choice(prompt: str) -> str:
    return input(prompt).strip()

def show_goodbye(name: str):
    print("=" * 40)
    print (f"\n Até logo{name}! Obrigado por usar o {SYSTEM_NAME}")
    print("=" * 40)


def main():

    running = True

    show_header()

    while running:

        show_main_menu()

        choice = get_user_choice("Escolha a opçao: ")

        if choice == "1":
            print("\n [] Sistema de login...")

        elif choice == "2":
            register_user()

        elif choice == "0":
            show_goodbye("usuario")
            running = False
        else:
            print("\n opcao invalida")

if __name__ =="__main__":
    main()

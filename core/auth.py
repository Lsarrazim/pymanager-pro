
import json
import os 

DATA_FILE = os.path.join(
    os.path.dirname(__file__), "..", "data", "users.json"
)

def load_users() -> list:
    
    if not os.path.exists(DATA_FILE):
        return []
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users: list) -> None:

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

def email_exists(email: str, users: list) ->  bool:

    return any(user["email"] == email for user in users)

def register_user() -> None:

    print("\n" + "=" * 40)
    print(" CRIAR CONTA")
    print("=" * 40)

    users = load_users()

    while True:
        name = input("\n Nome").strip()

        if not name:
            print("nome nao pode ser vazio")
            continue
        
        if len(name) < 2:
            print("Nome muito curto")
            continue

        break

    while True:

        email = input(" Email: ").strip().lower()

        if not email:
            print(" Email não pode vazio. ")
            continue
        
        if "@" not in email:
            print ("Email inválido")
            continue

        if email_exists(email, users):
            print("Email ja cadastrado")
            continue
            
        break

    while True:
        password = input(" Senha: ").strip()

        if not passworld:
            print("  Senha nao pode ser vazia ")
            continue
        
        if len(password) < 4:
            print("  Senha muito curto. Mínimo 4 caracteres.")

        break

        new_user = {
            "name": name,
            "email": email,
            "password": password
        }

        users.append(new_user)
        save_users(users)

        print(f"\n Conta Criada com sucesso!")

def login_user() -> dict | None:

    print("\n" + "=" * 40)
    print(" ENTRAR NO SISTEMA")
    print("=" * 40)

    users = load_users()

    if not users:
        print("\n Nenhum usuario cadastrado. ")
        print(" Crie uma conta primeiro ")
        return None

    email = input("\n Email: ").strip().lower()

    if not email:
        print("\n Email nao pode ser vazio")

    user = next(
        (u for u in users if u["email"] == email)
    ,None
    )

    if user is None:
        print("\n Email nao encontrado")
        return None

    password = input("  senha: ").strip().lower()

    if user["password"] != password:
        print("\n Senha incorreta")
        return None
    
    print(f"\n Bem vindo de volta, {user['name']}!")
    return user 



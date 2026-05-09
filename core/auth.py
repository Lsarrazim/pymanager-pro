import json 
import os

DATA_FILE = os.path.join(
    os.path.dirname(__file__), "..", "data", "users.name"
)

def load_users() -> list:
    if not os.path.exists(DATA_FILE):
        return []
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users: list) -> None:
    with open (DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

def email_exists(email: str, users: list) -> bool:
    return any(user["email"] == email for user in users)

def register_user() -> None:

    print ("\n" + "=" * 40)
    print (" CRIAR CONTA")
    print ("=" * 40)

    users = load_users()

    while True:
        name = input("\n Nome: ").strip()

        if not name:
            print("Nome não pode ser vazio")
            continue

        if len(name) < 2 :
            print("Nome muito curto")
            continue
        break
    
    while True:
        email = input("\n email: ").strip().lower()

        if not email:
            print("email nao pode ser vazio")
            continue
        
        if "@" not in email:
            print("Email invalido")
            continue
        
        if email_exists(email, users):
            print("Email já cadastrado")
            continue

        break

    while True:
        password = input("\n password: ")

        if not password:
            print("password nao pode ser vazio")
            continue

        if len(password) < 4:
            print ("password muito curto")
            continue

        break

    new_user = {
        "name": name,
        "email": email,
        "password": password
    }

    users.append(new_user)
    save_users(users)

    print((f"\n conta criada com sucesso! bem vindo {name}"))
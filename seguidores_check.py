# seguidores_check.py
from instagrapi import Client
import getpass

def login_instagram():
    print("=== LOGIN EN INSTAGRAM ===")
    username = input("Usuario de Instagram: ")
    password = getpass.getpass("Contraseña: ")

    cl = Client()
    try:
        cl.login(username, password)
        print("✅ Login exitoso.\n")
        return cl
    except Exception as e:
        print("❌ Error al iniciar sesión:", e)
        exit()

def obtener_ids(cl):
    user_id = cl.user_id
    print("📦 Obteniendo lista de seguidores y seguidos...")
    seguidores_ids = cl.user_followers(user_id).keys()
    seguidos_ids = cl.user_following(user_id).keys()
    return seguidores_ids, seguidos_ids

def calcular_no_seguidores(seguidores_ids, seguidos_ids):
    no_te_siguen = set(seguidos_ids) - set(seguidores_ids)
    return list(no_te_siguen)

def mostrar_resultados(cl, ids):
    if not ids:
        print("🎉 ¡Todos te siguen de vuelta!")
        return

    print(f"🔍 Usuarios que NO te siguen de vuelta ({len(ids)}):")
    for uid in ids:
        try:
            usuario = cl.user_info(uid).username
            print(f"- {usuario}")
        except:
            print(f"- [No se pudo obtener username para ID {uid}]")

def main():
    cl = login_instagram()
    seguidores_ids, seguidos_ids = obtener_ids(cl)
    no_te_siguen = calcular_no_seguidores(seguidores_ids, seguidos_ids)
    mostrar_resultados(cl, no_te_siguen)

if __name__ == "__main__":
    main()
# seguidores_check.py
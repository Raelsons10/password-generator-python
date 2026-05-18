from generator import generator_password
from utils import is_an_integer, is_valid_password_length


def main_interface():

    print("Bem-Vindo ao Sistema Gerador de Senhas Fortes") 

    while True:
        
        password = input("Informe o tamanho da senha que deseja gerar: ")

        if not is_an_integer(password):
            print("Digite apenas números.")
            continue
        
        new_password = int(password)

        if not is_valid_password_length(new_password):
            print("A senha deve ter no mínimo 12 caracteres.")            
            continue
        
        generated = generator_password(new_password)
        print(f"Sua senha gerada: {generated}")
        break

main_interface()
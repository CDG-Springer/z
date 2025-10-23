import os
from colorama import init, Fore

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

init()

print(Fore.GREEN + "██████╗  █████╗ ████████╗ ██████╗ ██████╗  ██████╗ ████████╗")
print("██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗╚══██╔══╝")
print("██████╔╝███████║   ██║   ██║   ██║██████╔╝██║   ██║   ██║   ")
print("██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗██║   ██║   ██║   ")
print("██║  ██║██║  ██║   ██║   ╚██████╔╝██████╔╝╚██████╔╝   ██║   ")
print("╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝   ")
print("                                                               ")
print("                  Formatador by Kinuzo                         ")
print("                                                               ")

def remove_lines_with_word(file_path, word_to_remove):
    try:
        with open(file_path, 'r', encoding='latin-1') as file:
            lines = file.readlines()

        filtered_lines = [line for line in lines if word_to_remove not in line]

        with open(file_path, 'w', encoding='latin-1') as file:
            file.writelines(filtered_lines)

        print(f"Todas as linhas contendo a palavra '{word_to_remove}' foram removidas de '{file_path}'.")

    except FileNotFoundError:
        print(f"Arquivo '{file_path}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def adicionar_numeracao_ao_arquivo(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            with open(output_file, 'w') as outfile:

                contador = 1

                for linha in infile:
                    linha = linha.strip()
                    linha_modificada = f"{linha}, {contador}\n"
                    outfile.write(linha_modificada)
                    contador += 1

        print("URLs modificadas e gravadas em 'acunetix.txt'.")

    except FileNotFoundError:
        print(f"Arquivo '{input_file}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
    print("[1] Remover palavra especifica")
    print("[2] Converter para formato Acunetix")

    choice = input("Escolha uma opção (1 ou 2): ")

    if choice == '1':
        arquivo_especifico = r'C:\Users\kinuzo\Documents\acunetix\subs.txt'
        palavra_a_remover = input("Digite a palavra que deseja remover: ")
        remove_lines_with_word(arquivo_especifico, palavra_a_remover)
    
    elif choice == '2':
        input_file = 'subs.txt'
        output_file = 'acunetix.txt'
        adicionar_numeracao_ao_arquivo(input_file, output_file)
    
    else:
        print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()

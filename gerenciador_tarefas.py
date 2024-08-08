import os
import time
from datetime import datetime
from peewee import *
from colorama import init, Fore, Style
from tabulate import tabulate
import pytz

# Configuração do banco de dados
db = SqliteDatabase('tarefas.db')

class BaseModel(Model):
    class Meta:
        database = db

class Tarefa(BaseModel):
    nome = CharField()
    descricao = CharField()
    data = CharField()
    status = CharField()

db.connect()
db.create_tables([Tarefa], safe=True)

# Inicializa o colorama
init(autoreset=True)

# Funções auxiliares
def obter_data_hora():
    try:
        saopaulo_time = datetime.now(pytz.timezone('America/Sao_Paulo'))
        return saopaulo_time.strftime('%d-%m-%Y %H:%M:%S')
    except Exception as e:
        print(f"Erro ao obter a data e hora: {e}")
        return 'Data/Hora não disponível'

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def pegar_opcao():
    while True:
        try:
            escolha = int(input('Digite o número que representa sua escolha: '))
            return escolha 
        except ValueError:
            print('Erro, digite apenas o número que representa a sua escolha!')


def logo():
    cian = Fore.CYAN
    print(f"{cian}{'-' * 70}\n{' ' * 22}CADASTRO DE TAREFAS\n{'-' * 70}\n")

def menu_inicial():
    logo()
    verde, azul, amarelo, vermelho, cian = Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.RED, Fore.CYAN
    print(f'1 - {verde}Cadastrar nova tarefa')
    print(f'2 - {azul}Visualizar tarefas')
    print(f'3 - {amarelo}Alterar status da tarefa')
    print(f'4 - {vermelho}Deletar tarefa')
    print(f'5 - {cian}Sair\n')

def cadastro_tarefa(nome, descricao, status='pendente'):
    Tarefa.create(nome=nome, descricao=descricao, data=obter_data_hora()[:10], status=status)

def update_tarefa(id):
    try:
        tarefa = Tarefa.get(Tarefa.id == id)
        tarefa.status = 'concluido' if tarefa.status == 'pendente' else 'pendente'
        tarefa.save()
    except Tarefa.DoesNotExist:
        print('Tarefa não encontrada, verifique o ID')

def exibir_tarefas(filtro_status=None):
    tarefas = Tarefa.select()
    if filtro_status:
        tarefas = tarefas.where(Tarefa.status == filtro_status)
    dados = [
        [t.id, Fore.BLUE + t.nome + Style.RESET_ALL, Fore.YELLOW + t.descricao + Style.RESET_ALL, t.data,
         (Fore.GREEN if t.status == 'concluido' else Fore.RED) + t.status.title() + Style.RESET_ALL]
        for t in tarefas
    ]
    cabecalhos = ['ID', 'Nome', 'Descrição', 'Data de cadastro', 'Status']
    print(tabulate(dados, headers=cabecalhos, tablefmt='fancy_grid'))

def menu_visualizar():
    logo()
    azul, verde, vermelho, cian = Fore.BLUE, Fore.GREEN, Fore.RED, Fore.CYAN
    print(f'1 - {azul}Visualizar todas as tarefas')
    print(f'2 - {verde}Visualizar tarefas concluídas')
    print(f'3 - {vermelho}Visualizar tarefas pendentes')
    print(f'4 - {cian}Voltar ao menu principal\n')
    escolha = pegar_opcao()
    limpar_terminal()
    if escolha == 4:
        return False
    elif escolha in [1, 2, 3]:
        logo()
        filtro = None
        if escolha == 2:
            filtro = 'concluido'
        elif escolha == 3:
            filtro = 'pendente'
        exibir_tarefas(filtro)
        print('\n1 - ' + azul + 'Voltar\n' + Fore.RESET + '2 - ' + Fore.YELLOW + 'Menu inicial\n')
        escolha = pegar_opcao()
        if escolha == 1:
            limpar_terminal()
            return True  
        elif escolha == 2:
            return False 
        else:
            print(Fore.RED + 'Opção inválida. Tente novamente.')
            time.sleep(2)
            limpar_terminal()
            return True 
    else:
        print(Fore.RED + 'Opção inválida. Tente novamente.')
        time.sleep(2)
        limpar_terminal()
        return True

def menu_cadastro():
    logo()
    verde, reset = Fore.GREEN, Style.RESET_ALL
    nome = input(verde + 'Digite o nome da tarefa: ' + reset).title()
    limpar_terminal()
    logo()
    descricao = input(verde + 'Digite a descrição da tarefa: ' + reset).capitalize()
    limpar_terminal()
    logo()
    try:
        cadastro_tarefa(nome, descricao)
        print(verde + 'Cadastro realizado com sucesso!\nVoltando ao menu principal...\n')
        time.sleep(3)
        limpar_terminal()
    except Exception as e:
        print(f'Erro ao cadastrar tarefa: {e}')

def delete_tarefa(id):
    try:
        tarefa = Tarefa.get(Tarefa.id == id)
        tarefa.delete_instance()
    except Tarefa.DoesNotExist:
        print('Tarefa não encontrada, verifique o ID')

def iniciar_programa():
    while True:
        limpar_terminal()
        menu_inicial()
        escolha = pegar_opcao()
        limpar_terminal()
        if escolha == 5:
            logo()
            print(Fore.CYAN + 'Fechando programa...\n')
            time.sleep(3)
            break
        elif escolha == 1:
            menu_cadastro()
        elif escolha == 2:
            while menu_visualizar(): 
                pass
        elif escolha == 3:
            while True:
                limpar_terminal()
                logo()
                exibir_tarefas()
                print(Fore.CYAN + 'Digite o ID da tarefa para alterar o status')
                print(Fore.CYAN + 'Digite 0 para voltar')
                escolha = pegar_opcao()
                if escolha == 0:
                    break
                else:
                    update_tarefa(escolha)
        elif escolha == 4:
            while True:
                limpar_terminal()
                logo()
                exibir_tarefas()
                print(Fore.CYAN + 'Digite o ID da tarefa para deletar\n')
                print(Fore.CYAN + 'Digite 0 para voltar\n')
                escolha = pegar_opcao()
                if escolha == 0:
                    break
                else:
                    delete_tarefa(escolha)
        else:
            print(Fore.RED + 'Opção inválida. Tente novamente.')
            time.sleep(2)

iniciar_programa()

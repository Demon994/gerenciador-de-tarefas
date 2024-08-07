# Gerenciador de Tarefas

Um sistema simples para gerenciamento de tarefas usando Python e SQLite. O sistema permite cadastrar, visualizar, alterar o status e deletar tarefas. O projeto utiliza a biblioteca Peewee para interação com o banco de dados e a biblioteca Colorama para colorir a saída no terminal.

## Funcionalidades

- **Cadastrar nova tarefa**: Permite adicionar uma nova tarefa com um nome, descrição e status padrão "pendente".
- **Visualizar tarefas**: Exibe uma lista de tarefas com base no status ou todas as tarefas.
- **Alterar status da tarefa**: Alterna o status de uma tarefa entre "pendente" e "concluído".
- **Deletar tarefa**: Remove uma tarefa do banco de dados.
- **Sair**: Encerra o programa.

## Requisitos

- Python 3.x
- Bibliotecas:
  - Peewee
  - Colorama
  - Tabulate
  - pytz

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/gerenciador-tarefas.git
2. Navegue até o diretório do projeto:
    ```bash
    cd gerenciador-tarefas
3. Instale as dependências usando o arquivo 'requirements.txt':
    ```bash
    pip install -r requirements.txt
## Uso
1. Execute o script principal:
    ```bash
    python gerenciador_tarefas.py
2. No menu inicial, você pode escolher uma das seguintes opções:
- 1 - Cadastrar nova tarefa
- 2 - Visualizar tarefas
- 3 - Alterar status da tarefa
- 4 - Deletar tarefa
- 5 - Sair
3. **Cadastrar nova tarefa**: Insira o nome e a descrição da tarefa quando solicitado.
4. **Visualizar tarefas**: Escolha visualizar todas as tarefas, tarefas concluídas, ou tarefas pendentes. Você pode voltar ao menu inicial ou ao menu de visualização.
5. **Alterar status da tarefa**: Digite o ID da tarefa para alternar seu status. Digite 0 para voltar ao menu de visualização.
6. **Deletar tarefa**: Digite o ID da tarefa para deletá-la. Digite 0 para voltar ao menu de deleção.
## Contribuição
Sinta-se à vontade para contribuir para o projeto. Caso encontre algum bug ou tenha sugestões de melhorias, abra uma issue ou envie um pull request.


Aqui está o modelo de um `README.md` em Markdown para o seu sistema:


# EFD - Excluir Linhas de NF Canceladas

Este é um sistema desenvolvido com Python e Tkinter, que tem como objetivo processar arquivos de texto no formato EFD (Escrituração Fiscal Digital) e remover linhas relacionadas a notas fiscais canceladas. O usuário seleciona um arquivo de texto, e o programa gera uma versão filtrada do arquivo, excluindo as linhas que correspondem a notas fiscais canceladas.

## Funcionalidades

- **Remoção de Linhas de NF Canceladas:** O programa filtra e remove as linhas que correspondem a notas fiscais canceladas, como as linhas iniciadas com `|C100|1|0||55|02`, `|C100|1|0||55|04` e `|C100|1|0||55|05`.
- **Interface Gráfica:** A interface gráfica foi construída com a biblioteca Tkinter, proporcionando uma forma intuitiva para o usuário selecionar o arquivo e processá-lo.
- **Barra de Progresso:** Durante o processamento do arquivo, uma barra de progresso é exibida para informar o andamento do processo.
- **Arquivos de Entrada e Saída:** O arquivo de entrada deve ser no formato `.txt` e o arquivo resultante será salvo com um sufixo `-filtrado` no mesmo diretório.

## Pré-requisitos

Antes de executar o programa, certifique-se de ter o Python 3 e a biblioteca Tkinter instalados em sua máquina.

- Python 3.x: [Download Python](https://www.python.org/downloads/)
- Tkinter (geralmente já está instalado com o Python)

## Como Usar

1. **Instalar Dependências:**
   
   Se o Tkinter não estiver instalado, você pode instalá-lo usando o seguinte comando:

   ```bash
   pip install tk
   ```

2. **Executar o Sistema:**
   
   Execute o script `main.py` em seu terminal ou ambiente de desenvolvimento preferido:

   ```bash
   python main.py
   ```

3. **Selecionar o Arquivo:**
   
   Clique no botão **"Selecionar Arquivo"** para escolher um arquivo de texto que será processado.

4. **Processar o Arquivo:**
   
   Após selecionar o arquivo, clique no botão **"Processar Arquivo"** para começar o processamento. O sistema irá gerar um novo arquivo com as linhas filtradas e exibir uma mensagem informando o número de linhas removidas.

## Estrutura do Código

### Funções Importantes:

- **`remover_espacos_antes_pipe(linha)`**: Remove espaços antes do caractere pipe (`|`) nas linhas do arquivo.
  
- **`select_file()`**: Abre uma janela para selecionar o arquivo a ser processado.
  
- **`process_file()`**: Processa o arquivo selecionado, removendo as linhas relacionadas às notas fiscais canceladas e salva o arquivo filtrado.

### Componentes da Interface Gráfica:

- **Botão "Selecionar Arquivo"**: Permite ao usuário escolher o arquivo de entrada.
- **Botão "Processar Arquivo"**: Inicia o processamento do arquivo.
- **Barra de Progresso**: Exibe o andamento do processo.

## Exemplo de Uso

### Arquivo de Entrada (Exemplo):
```txt
|C100|1|0||55|02|123456|1234|2025-01-01|1|...|
|C100|1|0||55|03|234567|2345|2025-01-02|1|...|
|C100|1|0||55|05|345678|3456|2025-01-03|1|...|
```

### Arquivo de Saída (Exemplo):
```txt
|C100|1|0||55|03|234567|2345|2025-01-02|1|...|
```

## Contribuições

Se você tiver sugestões ou melhorias para o sistema, sinta-se à vontade para abrir uma **issue** ou fazer um **pull request**.

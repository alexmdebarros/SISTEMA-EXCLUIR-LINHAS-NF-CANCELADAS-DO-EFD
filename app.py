import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os

class Application(tk.Tk):
    
    def remover_espacos_antes_pipe(self, linha):
        return '|'.join(segment.strip() for segment in linha.split('|'))
    
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.title("EFD - Excluir Linhas de NF Canceladas")
        self.geometry("500x300")
        self.configure(bg="#f4f4f4")  # Cor de fundo clara

        # Estilo moderno
        style = ttk.Style(self)
        style.configure("TButton", font=("Arial", 12), padding=6)
        style.configure("TLabel", font=("Arial", 10), background="#f4f4f4")
        style.configure("TProgressbar", thickness=10)

        self.create_widgets()

    def create_widgets(self):
        # Título principal
        title_label = ttk.Label(self, text="Remover Linhas de NF Canceladas", font=("Arial", 16, "bold"))
        title_label.pack(pady=(20, 10))

        # Botão para selecionar o arquivo
        self.select_button = ttk.Button(self, text="Selecionar Arquivo", command=self.select_file)
        self.select_button.pack(pady=10)

        # Label para mostrar o caminho do arquivo selecionado
        self.file_label = ttk.Label(self, text="Nenhum arquivo selecionado", anchor="center", foreground="#555")
        self.file_label.pack(pady=5)

        # Botão para processar o arquivo
        self.process_button = ttk.Button(self, text="Processar Arquivo", command=self.process_file)
        self.process_button.pack(pady=10)

        # Barra de progresso (escondida inicialmente)
        self.progress = ttk.Progressbar(self, orient="horizontal", length=400, mode="indeterminate")
        self.progress.pack(pady=10)
        self.progress.pack_forget()

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if self.file_path:
            self.file_label.config(text=f"Arquivo selecionado: {os.path.basename(self.file_path)}")

    def process_file(self):
        if not hasattr(self, 'file_path') or not self.file_path:
            messagebox.showerror("Erro", "Nenhum arquivo selecionado.")
            return

        # Mostrar a barra de progresso
        self.progress.pack(pady=10)
        self.progress.start()

        try:
            input_file_name = self.file_path
            base_name, ext = os.path.splitext(input_file_name)
            output_file_name = f"{base_name}-filtrado{ext}"

            def filtrar_linhas(linha):
                return not (linha.startswith('|C100|1|0||55|02') or
                            linha.startswith('|C100|1|0||55|04') or
                            linha.startswith('|C100|1|0||55|05'))

            linhas_removidas = 0  # Contador de linhas removidas

            with open(input_file_name, 'r') as file:
                linhas = file.readlines()

            with open(output_file_name, 'w') as file:
                for linha in linhas:
                    linha = self.remover_espacos_antes_pipe(linha)
                    if filtrar_linhas(linha):
                        file.write(linha.rstrip() + '\n')
                    else:
                        linhas_removidas += 1

            messagebox.showinfo("Concluído",
                                f"Arquivo processado com sucesso!\n"
                                f"Total de Linhas removidas: {linhas_removidas}\n"
                                f"Salvo em: {output_file_name}")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar o arquivo: {e}")
        finally:
            self.progress.stop()
            self.progress.pack_forget()

    
if __name__ == "__main__":
    app = Application()
    app.mainloop()

import tkinter as tk 

def mostrar_mensagem():
    texto = caixa_texto.get()
    label_resultado.config(text=texto)
    # Atualizar o texto de rótulo com o texto da caixa 
    label_resultado.config(text=texto)

# Criar a janela principal
janela = tk.Tk()
janela.title("Exemplo de Interface Gráfica")
janela.geometry("400x150")

# Mudando cor de fundo da tela
janela.config(bg="cyan")

# Criar uma caixa de entrada (Entry)
caixa_texto = tk.Entry(janela, width=60)
caixa_texto.pack(pady=10)

# Criar botão 
botao = tk.Button(janela, text="Mostrar texto", command=mostrar_mensagem, bg="blue", fg="white")
botao.pack(pady=5)

# Criar rótulo para mostrar o resultado
label_resultado = tk.Label(janela, text="", bg="cyan")
label_resultado.pack(pady=10)

# Executar a tela principal 
janela.mainloop()
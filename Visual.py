import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Para carregar imagens
import os
class Carro:
    def __init__(self, modelo, preco: float, km_rodados: int, imagem: str):
        self.modelo = modelo  
        self.preco = float(preco)
        self.km_rodados = int(km_rodados)
        self.imagem = imagem #caminho da imagem

# Lista de carros
carros = [
    Carro("Hyundai HB20 Comfort Plus 1.0 2017", 44900.00, 45000, "imgs/hb20.jpg"),
    Carro("Fiat Uno Attractive 1.0 2015", 75000.00, 51615, "imgs/fiat uno.jpg"),
    Carro("Volvo XC60 T8 Ultimate Dark 2023", 327000.00 , 38000, "imgs/volvo.jpg"),
    Carro("Chevrolet Cruze LTZ 1.4 Turbo Automático 2018", 84900.00, 90000, "imgs/cruze.jpg"),
    Carro("Ford Ka SE 1.0 2018", 84999.75, 25000, "imgs/fordka.jpg"),
    Carro("Mercedes-Benz C180 Turbo 2014 Blindado!", 66900.00, 70000, "imgs/mercedez.jpg")
]

def mostrar_carros():
    """Exibe a lista de carros com imagens"""
    for widget in frame_carros_canvas.winfo_children():  
        widget.destroy()  # Limpa os widgets anteriores

    for carro in carros:
        frame = tk.Frame(frame_carros_canvas, bg="white", pady=5)
        frame.pack(fill="x", padx=10, pady=5)

        try:
            img = Image.open(carro.imagem)  # Carregar imagem
            img = img.resize((100, 80))  # tamanho da imagem
            img = ImageTk.PhotoImage(img)
        except:
            img = ImageTk.PhotoImage(Image.new("RGB", (100, 80), (200, 200, 200)))  # Imagem de erro

        img_label = tk.Label(frame, image=img, bg="white")
        img_label.image = img  # Evita que a imagem seja apagada pela coleta de lixo do Python
        img_label.pack(side="left", padx=10)

        info = f"{carro.modelo}\nPreço: R$ {carro.preco:,.2f}\nKM Rodados: {carro.km_rodados} km"
        lbl_info = tk.Label(frame, text=info, font=("Arial", 12), justify="left", bg="white")
        lbl_info.pack(side="left", padx=10)

    # Atualiza a área visível do canvas
    frame_carros_canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# janela do tkinter
janela = tk.Tk()
janela.title("LOMANTO AUTOS")
janela.geometry("600x500")
janela.configure(bg="#2C3E50")

# NOME DA LOJA
titulo = tk.Label(janela, text="LOMANTO AUTOS", font=("Arial", 20, "bold"), fg="white", bg="#2C3E50")
titulo.pack(pady=10)

# Botão pra abrir carros()
btn_carros = tk.Button(janela, text="Carros", font=("Arial", 14), bg="#3498DB", fg="white",
                        width=10, height=2, command=mostrar_carros)
btn_carros.pack(pady=10)

# Scroolbar
canvas = tk.Canvas(janela)
scrollbar = tk.Scrollbar(janela, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Adicionando os carros no canvas
frame_carros_canvas = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame_carros_canvas, anchor="nw")

# Organizando o Canvas e a Scrollbar na janela
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Atualizando a região visível após adicionar novos elementos
frame_carros_canvas.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Rodando a interface do tkinter
janela.mainloop()

import tkinter as tk


def calcular(num1, operacao, num2):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: divisão por zero!"
    else:
        return "Operação inválida!"


def clicar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        operacao = operacao_var.get()

        resultado = calcular(num1, operacao, num2)
        resultado_label.config(text=f"Resultado: {resultado}")

    except ValueError:
        resultado_label.config(text="Erro: digite números válidos!")



janela = tk.Tk()
janela.title("Mini Calculadora")
janela.geometry("500x550")

tk.Label(janela, text="Calculadora", font=("Arial", 16)).pack(pady=10)

entrada1 = tk.Entry(janela)
entrada1.pack(pady=5)

operacao_var = tk.StringVar(value="+")

tk.OptionMenu(janela, operacao_var, "+", "-", "*", "/").pack(pady=5)

entrada2 = tk.Entry(janela)
entrada2.pack(pady=5)

tk.Button(janela, text="Calcular", command=clicar).pack(pady=10)

resultado_label = tk.Label(janela, text="Resultado:")
resultado_label.pack(pady=10)

janela.mainloop()
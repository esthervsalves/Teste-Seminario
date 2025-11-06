def somar(a, b):

    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def executar_operacoes():
    print("--- Operações Base ---")
    print(f"Soma: 10 + 5 = {somar(10, 5)}")
    print(f"Subtração: 10 - 5 = {subtrair(10, 5)}")
    print(f"Multiplicação: 10 * 5 = {multiplicar(10, 5)}")
    print(f"Divisão: 10 / 5 = {dividir(10, 5)}")

if __name__ == "__main__":
    executar_operacoes()
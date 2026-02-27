from calculadora import calcular

def testar():
    
    assert calcular(2, "+", 3) == 5
    assert calcular(5, "-", 2) == 3
    assert calcular(4, "*", 3) == 12
    assert calcular(10, "/", 2) == 5

    assert calcular(-2, "+", 3) == 1
    assert calcular(-4, "*", -2) == 8
    assert calcular(-10, "/", 2) == -5

 
    assert calcular(2.5, "+", 2.5) == 5.0
    assert calcular(5.5, "-", 1.1) == 4.4

  
    assert calcular(5, "/", 0) == "Erro: divisão por zero!"

  
    assert calcular(5, "%", 2) == "Operação inválida!"

    print("✅ Todos os testes passaram!")

testar()
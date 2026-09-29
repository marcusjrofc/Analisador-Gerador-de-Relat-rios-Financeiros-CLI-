import csv

total_geral = 0.0
categorias = {}

with open("dados.csv","r")as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor) # Pula a primeira linha (cabeçalho)
    
    for linha in leitor:
        # Remove tudo o que NÃO for dígito (0-9) ou ponto (.)
        valor_limpo = "".join(caractere for caractere in linha[3] if caractere.isdigit() or caractere == ".")
        valor = float(valor_limpo)
        total_geral += valor # Acumula o valor na variável total_geral
        
        categoria = linha[2].strip()
        categorias[categoria] = categorias.get(categoria, 0.0) + valor
        
# Exibição do relatório final
print("\n--- GASTOS POR CATEGORIA ---")
for cat, total in categorias.items():
    print(f"{cat}: R${total:.2f}")
        
print(f"Total gasto: R${total_geral:.2f}")
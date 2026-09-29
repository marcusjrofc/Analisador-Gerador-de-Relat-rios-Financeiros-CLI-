import csv

# Exceções personalizadas
class ValorInferiorException(Exception):
    pass

class ErroArquivoCSVException(Exception):
    pass


def carregar_transacoes(caminho_arquivo):
    total_geral = 0.0
    categorias = {}

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)  # Pula o cabeçalho

            for numero_linha, linha in enumerate(leitor, start=2):
                try:
                    # Sanitização do valor
                    valor_limpo = "".join(caractere for caractere in linha[3] if caractere.isdigit() or caractere == ".")
                    
                    if not valor_limpo:
                        raise ValorInferiorException(f"Linha {numero_linha}: valor numérico ausente ou inválido.")

                    valor = float(valor_limpo)
                    
                    if valor <= 0:
                        raise ValorInferiorException(f"Linha {numero_linha}: o valor deve ser maior que zero.")

                    # Processamento dos dados válidos
                    total_geral += valor
                    categoria = linha[2].strip()
                    categorias[categoria] = categorias.get(categoria, 0.0) + valor

                except (IndexError, ValueError) as e:
                    print(f"⚠️ Erro ao processar a linha {numero_linha} ({linha}): Formato inválido.")

    except FileNotFoundError:
        print(f"❌ Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None, None

    return total_geral, categorias


# Fluxo Principal de Execução
if __name__ == "__main__":
    total, categorias = carregar_transacoes("dados.csv")

    if total is not None:
        print("\n--- GASTOS POR CATEGORIA ---")
        for cat, subtotal in categorias.items():
            print(f"{cat}: R${subtotal:.2f}")

        print(f"\nTotal gasto: R${total:.2f}")
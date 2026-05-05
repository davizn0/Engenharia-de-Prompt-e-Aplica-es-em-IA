from datetime import datetime

def validar_localizacao(unidade: str, latitude: float) -> bool:
    """
    Valida se a latitude está correta para a unidade.
    
    Args:
        unidade: Nome da unidade (Centro, Sul, etc)
        latitude: Coordenada de latitude do GPS
    
    Returns:
        bool: True se a localização é válida, False caso contrário
    """
    localizacoes = {
        "Centro": -23.5,
        "Sul": -23.8
    }
    
    if unidade not in localizacoes:
        return False
    
    return abs(latitude - localizacoes[unidade]) < 0.01  # Tolerância de 0.01

def registrar_ponto(nome_funcionario: str, unidade: str, latitude: float, longitude: float = None) -> bool:
    """
    Registra o ponto de um funcionário com validação de GPS.
    
    Args:
        nome_funcionario: Nome do funcionário
        unidade: Unidade de trabalho (Centro, Sul)
        latitude: Latitude do GPS
        longitude: Longitude do GPS (opcional)
    
    Returns:
        bool: True se registrado com sucesso, False caso contrário
    """
    
    # Validar localização
    if not validar_localizacao(unidade, latitude):
        print(f"❌ ERRO: Localização inválida para a unidade {unidade}")
        print(f"   Latitude esperada: {-23.5 if unidade == 'Centro' else -23.8}")
        print(f"   Latitude registrada: {latitude}")
        return False
    
    # Criar registro
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro = f"[{timestamp}] Funcionário: {nome_funcionario} | Unidade: {unidade} | Latitude: {latitude} | Longitude: {longitude or 'N/A'}\n"
    
    # Salvar em arquivo
    try:
        with open("registros.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(registro)
        print(f"✅ Ponto registrado com sucesso para {nome_funcionario}")
        return True
    except Exception as e:
        print(f"❌ ERRO ao salvar registro: {e}")
        return False

def listar_registros():
    """Exibe todos os registros de ponto."""
    try:
        with open("registros.txt", "r", encoding="utf-8") as arquivo:
            registros = arquivo.readlines()
            if not registros:
                print("Nenhum registro encontrado.")
                return
            print("\n📋 REGISTROS DE PONTO:")
            print("-" * 80)
            for registro in registros:
                print(registro.strip())
            print("-" * 80)
    except FileNotFoundError:
        print("Arquivo de registros não encontrado.")

def main():
    """Função principal para interagir com o sistema."""
    while True:
        print("\n=== SISTEMA DE PONTO MULTI-UNIDADE ===")
        print("1. Registrar ponto")
        print("2. Listar registros")
        print("3. Sair")
        
opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            nome = input("Nome do funcionário: ").strip()
            unidade = input("Unidade (Centro/Sul): ").strip()
            try:
                latitude = float(input("Latitude do GPS: ").strip())
                longitude = input("Longitude do GPS (opcional): ").strip()
                longitude = float(longitude) if longitude else None
                
                registrar_ponto(nome, unidade, latitude, longitude)
            except ValueError:
                print("❌ ERRO: Coordenadas inválidas. Use valores numéricos.")
        
        elif opcao == "2":
            listar_registros()
        
        elif opcao == "3":
            print("Encerrando sistema...")
            break
        
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()
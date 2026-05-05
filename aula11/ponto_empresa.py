from datetime import datetime
import os

class AttendanceSystem:
    """Sistema de ponto multi-unidade com validação de GPS."""
    
    # Configuração de unidades e suas coordenadas de latitude
    UNITS = {
        "Centro": -23.5,
        "Sul": -23.8
    }
    
    LOG_FILE = "registros.txt"
    
    def __init__(self):
        """Inicializa o sistema de ponto."""
        self.ensure_log_file_exists()
    
    def ensure_log_file_exists(self):
        """Garante que o arquivo de log existe."""
        if not os.path.exists(self.LOG_FILE):
            with open(self.LOG_FILE, 'w', encoding='utf-8') as f:
                f.write("=== REGISTRO DE PONTO MULTI-UNIDADE ===\n")
                f.write(f"Iniciado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
                f.write("=" * 50 + "\n\n")
    
    def validate_gps(self, unit: str, latitude: float) -> bool:
        """
        Valida a latitude de acordo com a unidade.
        
        Args:
            unit: Nome da unidade
            latitude: Latitude do GPS
            
        Returns:
            True se válido, False caso contrário
        """
        if unit not in self.UNITS:
            return False
        
        return abs(latitude - self.UNITS[unit]) < 0.01  # Tolerância de 0.01
    
    def register_attendance(self, employee_name: str, unit: str, latitude: float) -> dict:
        """
        Registra o ponto do funcionário com validação de GPS.
        
        Args:
            employee_name: Nome do funcionário
            unit: Unidade (Centro ou Sul)
            latitude: Latitude do GPS
            
        Returns:
            Dicionário com status do registro
        """
        result = {
            "success": False,
            "message": "",
            "employee": employee_name,
            "unit": unit,
            "latitude": latitude,
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        
        # Validar se a unidade existe
        if unit not in self.UNITS:
            result["message"] = f"Unidade '{unit}' não encontrada. Unidades válidas: {', '.join(self.UNITS.keys())}"
            self.log_attendance(result, False)
            return result
        
        # Validar GPS
        if not self.validate_gps(unit, latitude):
            expected_lat = self.UNITS[unit]
            result["message"] = f"Erro: Latitude inválida. Esperado: {expected_lat}, Recebido: {latitude}"
            self.log_attendance(result, False)
            return result
        
        # Sucesso
        result["success"] = True
        result["message"] = f"Ponto registrado com sucesso para {employee_name} na unidade {unit}"
        self.log_attendance(result, True)
        return result
    
    def log_attendance(self, result: dict, success: bool):
        """
        Salva o registro no arquivo registros.txt.
        
        Args:
            result: Dicionário com informações do registro
            success: Se o registro foi bem-sucedido
        """
        status = "✓ SUCESSO" if success else "✗ FALHA"
        
        log_entry = f"""
[{result['timestamp']}] {status}
Nome: {result['employee']}
Unidade: {result['unit']}
Latitude: {result['latitude']}
Mensagem: {result['message']}
{'-' * 50}
"""
        
        with open(self.LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_entry)
    
    def view_logs(self):
        """Exibe os logs do arquivo."""
        if not os.path.exists(self.LOG_FILE):
            print("Nenhum arquivo de log encontrado.")
            return
        
        with open(self.LOG_FILE, 'r', encoding='utf-8') as f:
            print(f.read())


def main():
    """Função principal - Interface interativa."""
    system = AttendanceSystem()
    
    print("=" * 50)
    print("SISTEMA DE PONTO MULTI-UNIDADE COM VALIDAÇÃO GPS")
    print("=" * 50)
    
    while True:
        print("\nOpções:")
        print("1. Registrar ponto")
        print("2. Ver logs")
        print("3. Sair")
        
        choice = input("\nEscolha uma opção (1-3): ").strip()
        
        if choice == "1":
            employee_name = input("Nome do funcionário: ").strip()
            
            print("\nUnidades disponíveis:")
            for unit, lat in system.UNITS.items():
                print(f"  - {unit} (Latitude: {lat})")
            
            unit = input("Unidade: ").strip()
            
            try:
                latitude = float(input("Latitude do GPS: ").strip())
            except ValueError:
                print("Erro: Latitude deve ser um número.")
                continue
            
            result = system.register_attendance(employee_name, unit, latitude)
            print(f"\n{result['message']}")
        
        elif choice == "2":
            system.view_logs()
        
        elif choice == "3":
            print("Encerrando sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

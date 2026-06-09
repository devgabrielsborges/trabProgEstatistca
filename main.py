from dataclasses import dataclass, field

@dataclass
class discente:
    matricula: str
    nome: str
    num_presencas: int = 0
    notas: list[float] = field(default_factory=lambda: [0.0, 0.0, 0.0])

class discentes:
    def __init__(self):
        self._discentes = {}


    @property
    def discentes_dict(self):
        return self._discentes


    def listar_discentes(self):
        if not self._discentes:
            print("Não existem discentes cadastrados")
            return
        for matricula, d in self._discentes.items():
            print(f"Matrícula: {d.matricula} | Nome: {d.nome} | Presenças: {d.num_presencas} | Notas: {d.notas}")


    def adicionar_discente(self, matricula: str, nome: str):
        if matricula in self._discentes:
            print("Erro: Matrícula já cadastrada")
            return
        self._discentes[matricula] = discente(matricula=matricula, nome=nome)
        print(f"Discente {matricula} | {nome} cadastrado com sucesso")


    def atualizar_notas(self, matricula: str, notas: list[float]):
        if matricula not in self._discentes:
            print("Erro: Discente não encontrado")
            return
        self._discentes[matricula].notas = notas
        nome = self._discentes[matricula].nome
        print(f"Notas do discente {nome} atualizadas com sucesso")


    def atualizar_frequencia(self, matricula: str):
        if matricula not in self._discentes:
            print("Erro: Discente não encontrado")
            return
        self._discentes[matricula].num_presencas += 1
        nome = self._discentes[matricula].nome
        print(f"Frequência do discente {nome} atualizada com sucesso")


    def remover_discente(self, matricula: str):
        if matricula in self._discentes:
            nome = self._discentes[matricula].nome
            self._discentes.pop(matricula)
            print(f"Discente {nome} removido com sucesso")


    def imprimir_relatorio(self):
        aprovados_nota = 0
        reprovados_falta = 0
        for d in self._discentes.values():
            media = sum(d.notas) / 3

            frequencia = d.num_presencas / 30
            
            if media >= 7.0:
                aprovados_nota += 1
            if frequencia < 0.75:
                reprovados_falta += 1
                
        print(f"Quantidade de discentes aprovados por nota: {aprovados_nota}")
        print(f"Quantidade de discentes reprovados por falta: {reprovados_falta}")

def main():
    menu = discentes()
    
    while True:
        print("--- Menu ---")
        print("1. Listar discentes")
        print("2. Cadastrar discente")
        print("3. Atualizar notas")
        print("4. Atualizar frequência")
        print("5. Remover discente")
        print("6. Imprimir relatório")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        match opcao:
            case '1':
                menu.listar_discentes()
                
            case '2':
                matricula = input("Digite o número de matrícula: ")
                nome = input("Digite o nome: ")
                menu.adicionar_discente(matricula, nome)
                
            case '3':
                matricula = input("Digite o número de matrícula: ")
                nota1 = float(input("Digite a nota 1: "))
                nota2 = float(input("Digite a nota 2: "))
                nota3 = float(input("Digite a nota 3: "))
                menu.atualizar_notas(matricula, [nota1, nota2, nota3])
                    
            case '4':
                matricula = input("Digite a matrícula do discente: ")
                menu.atualizar_frequencia(matricula)
                
            case '5':
                matricula = input("Digite a matrícula do discente a ser removido: ")
                menu.remover_discente(matricula)
                
            case '6':
                menu.imprimir_relatorio()
                
            case '7':
                print("Saindo do programa.")
                break
                
            case _:
                print("Opção inválida.")

main()

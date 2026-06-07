from dataclasses import dataclass

@dataclass
class discente:
    matricula: str
    nome: str
    num_presencas: int = 0
    notas: list[int] = []

class discentes:
    def __init__(self):
        self._discentes = {}


    @property
    def discentes(self):
        return self._discentes


    def adicionar_discente(self, matricula: str, nome: str):
        if  matricula in self._discentes.keys():
            print("Matrícula já cadastrada")
            return
        self._discentes.append(discente(matricula=matricula, nome=nome))
        print(f"Discente {nome}, de matrícula {matricula} cadastrado com sucesso")
    

    def remover_discente(self, matricula: str):
        if matricula in self._discentes.keys():
            self._discentes.pop(matricula)


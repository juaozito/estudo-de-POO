class Pessoa:


    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        print(f"Objeto Pessoa base '{self.nome}' criado.")


    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


    def __del__(self):
        pass


    def __str__(self):
        return(
            f"--- Dados da Pessoa ---\n"
            f"Nome: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Instituição: IFAM (Herdado)\n" # Adicionando a Instituição (Como um dado genérico aqui)
            f"-----------------------\n"
        )
    
# INICIO DAS SUBCLASSES (CLASSES FILHAS)

class Professor(Pessoa):

# A subclasse Professor herda de Pessoa (Professor EH uma Pessoa)

    def __init__(self, nome: str, idade: int, disciplina: str):

        #Chama o construtor da Classe Mae(Pessoa) para inicializar nome e idade.
        super().__init__(nome, idade)

        #Inicializa os atributos proprios da calsse Professor
        self.disciplina = disciplina
        print(f"Objeto Professor '{self.nome}' criado.")

    #METODO PROPRIO da calsse Professor (Comportamento extra)
    def lecionar(self):
        print(f"O Professor {self.nome} esta lecionando a disciplina {self.disciplina}.")

    #Opcional: Sobrescreve o __str__ para incluir a disciplina
    def __str__(self):
        #O Professor reusa a apresentacao da Pessoa
        texto_base = super().__str__()
        return texto_base + f"Disciplina: {self.disciplina}\n"
    
class Aluno(Pessoa):

    def __init__(self, nome: str, idade: int, matricula: int):
        super().__init__(nome,idade)

        self.matricula = matricula
        print(f"Objeto Aluno '{self.nome}' criado.")

    def estudar(self):
        print(f"O Aluno {self.nome}, de matricula {self.matricula}, esta estudando.")

    def __str__(self):
        texto_base = super().__str__()
        return texto_base + f"Matricula: {self.matricula}\n"

        

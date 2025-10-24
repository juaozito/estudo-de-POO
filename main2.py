from pessoa import Pessoa, Professor, Aluno

class Main:

    def __init__(self):
        pass

    def executar(self):
        print("--- Início do Programa de Cadastro (Modo Interativo) ---")

        # 1.
        professor = self.entradaDados_Professor()

        # 2.
        aluno = self.entradaDados_Aluno()

        # 3.
        self.exibirDados(professor, aluno)

        print("\n--- Programa Finalizado ---")

    def entradaDados_Professor(self):
        print("\n--- Cadastro de NOVO PROFESSOR ---")
        nome = input("Digite o nome do Professor: ")
        idade = input("Digite a idade do Professor: ")
        disciplina = input("Digite a disciplina do Professor: ")

        # Cria e retorna a instancia do objeto Professor
        return Professor(nome, idade, disciplina)
    
    def entradaDados_Aluno(self):
        print("\n--- Cadastro de NOVO ALUNO ---")
        nome = input("Digite o nome do Aluno: ")
        idade = int(input("Digite a idade do Aluno: "))
        matricula = int(input("Digite a matrícula do Aluno (apenas números): "))

        # Cria e retorna a instancia do objeto Aluno
        return Aluno(nome, idade, matricula)
    
    def exibirDados(self, professor: Professor, aluno: Aluno):
        print("\n=============================================")
        print("RESULTADOS DO CADASTRO (SAÍDA DE DADOS)")
        print("=============================================")

        # Exibicao do Professor (Chama automaticamente __str__ de Professor)
        print("\n--- Dados do Professor ---")
        print(professor)
        professor.lecionar()
        professor.apresentar()

        # Exibicao do Aluno (Chama automaticamente __str__ de Aluno)
        print("\n--- Dados do Aluno ---")
        print(aluno)
        aluno.estudar()
        aluno.apresentar()

# --- BLOCO DE EXECUÇÃO (FORA DA CLASSE) ---
# CORREÇÃO: Estas linhas precisam estar fora de qualquer método ou classe.

# Inicia a execução do programa
app = Main()
app.executar()



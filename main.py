from pessoa import Pessoa, Professor, Aluno

class Main:

    def __init__(self):
        pass

    def executar(self):
        print("--- Início do Teste de Herança --- ")

        #PASSO A: CRIAR UM OBJETO PROFESSOR
        print("\n--- Teste Professor ---")

        #1. CRIA o OBJETO Professro (Instancia da Subclasse)
        # Lembre-se que precisa de 3 argumentos: nome, idade disciplina.
        professor_manoel = Professor("Manoel", 45, "Programacao Orientada a Objetos")

        #2. Chama o metodo HERDADO ( apresentar() veio da classe Pessoa)
        professor_manoel.apresentar()

        #3. Chama o metodo PROPRIO da Subclasse ( lecionar() eh especifico de Professor)
        professor_manoel.lecionar()

        #4. Imprime o objeto (Chama o __str__ sobrescrito)
        print(professor_manoel)


        #PASSO B: CRIAR UM OBJETO ALUNO
        print("\n--- Teste Aluno ---")

        # 1. Cria o objeto Aluno (Instância da Subclasse)
        # Lembre-se que precisa de 3 argumentos: nome, idade, matricula.
        aluno_estrela = Aluno("Joao Silva", 22, 2024001)

        # 2. Chama o metoodo HERDADO ( apresentar() veio da classe PESSOA)
        aluno_estrela.apresentar()

        # 3. Chama o metodo PROPRIO da Subclasse ( estudar() eh especifico ded Aluno)
        aluno_estrela.estudar()

        # 4. Imprime o objeto (Chama o __str__ sobrescrito)
        print(aluno_estrela)

        print("--- Fim do Teste de Herança ---")

# --- BLOCO DE EXECUÇÃO (FORA DA CLASSE) ---
# CORREÇÃO: Estas linhas precisam estar fora de qualquer método ou classe.

# Inicia a execução do programa
app = Main()
app.executar()



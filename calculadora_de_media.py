class Calculadora_de_media:
    def __init__(self,curso,nome):
        self.curso = curso
        self.nome = nome
        self.ciencias = ["Português","Matemática A","Física e Química A","Biologia e Geologia","Educação Física","Filosofia"]
        self.linguas = [ "Português","História A","Filosofia","Geografia A","Educação Física","Inglês","MACS"]
        self.notas = []
        if self.curso == 1:
            self.lista_disciplinas = self.linguas
        elif self.curso == 2:
            self.lista_disciplinas = self.ciencias
    def disciplinas_do_curso(self):
        if self.curso == 1:
            print("você selecionou: Línguas e Humanidades")
            print(f"Disciplinas do curso:")
            for disciplina in self.linguas:
                print(disciplina)
        elif self.curso == 2:
            print("você selecionou: Ciências e Tecnologias")
            print("Disciplinas do curso:")
            for disciplina in self.ciencias:
                print(disciplina)
    def inserir_notas(self):
        for disciplina in self.lista_disciplinas:
            while True:
                try:
                    nota = int(input(f"{disciplina} - insira a nota: "))
                    if nota < 0 or nota > 20:
                        print("Nota inválida! Tem de ser entre 0 e 20.")
                        continue
                    self.notas.append(nota)
                    break
                except ValueError:
                    print("Por favor, insira um número inteiro válido.")

    def calcular_media(self):
        total = sum(self.notas)
        media = total  / len(self.notas)
        print(f"A tua media é de {round(media,2)} valores ")




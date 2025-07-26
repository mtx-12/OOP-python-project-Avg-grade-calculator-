from calculadora_de_media import *


#Execução
nome = input("Nome do aluno(a): ")
curso = int(input("Escolha o curso:\n1. Línguas e Humanidades\n2. Ciências e Tecnologias\n"))
course = Calculadora_de_media(curso,nome)
course.disciplinas_do_curso()
course.inserir_notas()
course.calcular_media()



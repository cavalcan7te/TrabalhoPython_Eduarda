a = input("Nome do aluno:")
d = input("Disciplina:")
n1 = float(input("Sua nota na parcial:"))
n2 = float(input("Sua nota na bimestral:"))
m = (n1 + n2) / 2
if m >= 6:
    s = ("aprovado")
else:
    s = ("reprovado")
print(f'{a} está {s} na disciplina {d}.')
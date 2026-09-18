import json

alunos = [
  {"matricula": "202431737724", "nome": "ARTUR COROA VOLPATO", "situacao": "MATRICULADO"},
  {"matricula": "202431727754", "nome": "ANA VICTORIA B. GOMES", "situacao": "MATRICULADO"},
  {"matricula": "202431716654", "nome": "ALANA PEREIRA ALVES", "situacao": "MATRICULADO"},
  {"matricula": "202431720345", "nome": "GIOVANNA S. DE JESUS", "situacao": "TRANSFERIDO"},
]

total = len(alunos)
matriculados = [a for a in alunos if a["situacao"] == "MATRICULADO"]

print(f"Total: {total}")
print(f"Matriculados: {len(matriculados)}")
for a in matriculados:
  print(f"{a['matricula']} - {a['nome']}")

busca = input("Buscar nome: ").upper()
for a in alunos:
  if busca in a["nome"]:
    print(f"Achei: {a['nome']} - {a['situacao']}")

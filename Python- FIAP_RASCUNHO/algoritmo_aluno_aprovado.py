notas_cursos = {"engenharia_prompt": 10, "matematica": 4, "sustentabilidade": 10, "programacao": 8.7}

media_aprovacao = (notas_cursos["engenharia_prompt"] + notas_cursos["matematica"] + notas_cursos["sustentabilidade"] + notas_cursos["programacao"]) / 4

if media_aprovacao >= 6:
    print(f"Aluno aprovado! Média final: {media_aprovacao :.2f}")
else:
    print(f"Aluno reprovado! Média final: {media_aprovacao :.2f}")
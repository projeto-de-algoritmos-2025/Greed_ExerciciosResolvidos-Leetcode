## 1462. Verificação de Pré-requisitos de Curso IV

**Médio**

Há um total de `numCourses` cursos que você deve fazer, rotulados de `0` a `numCourses - 1`. Você recebe um array `prerequisites` onde `prerequisites[i] = [ai, bi]` indica que você deve fazer o curso `ai` primeiro se quiser fazer o curso `bi`.

Por exemplo, o par `[0, 1]` indica que você precisa fazer o curso 0 antes de poder fazer o curso 1.

Os pré-requisitos também podem ser indiretos. Se o curso `a` for pré-requisito do curso `b` e o curso `b` for pré-requisito do curso `c`, então o curso `a` também é pré-requisito do curso `c`.

Você também recebe um array `queries` onde `queries[j] = [uj, vj]`. Para a `j`-ésima consulta, você deve responder se o curso `uj` é pré-requisito do curso `vj` ou não.

Retorne um array booleano `answer`, onde `answer[j]` é a resposta para a `j`-ésima consulta.

### Exemplo 1:

```
Entrada: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Saída: [false,true]

Explicação: O par [1, 0] indica que você deve fazer o curso 1 antes do curso 0.
O curso 0 não é pré-requisito do curso 1, mas o oposto é verdadeiro.
```

### Exemplo 2:

```
Entrada: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Saída: [false,false]

Explicação: Não há pré-requisitos e cada curso é independente.
```

### Exemplo 3:

```
Entrada: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Saída: [true,true]
```

### Restrições:

- 2 <= numCourses <= 100
- 0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
- prerequisites[i].length == 2
- 0 <= ai, bi <= numCourses - 1
- ai != bi
- Todos os pares [ai, bi] são únicos.
- O grafo de pré-requisitos não possui ciclos.
- 1 <= queries.length <= 10⁴
- 0 <= ui, vi <= numCourses - 1
- ui != vi

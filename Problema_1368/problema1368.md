## 1368. Custo Mínimo para Fazer Pelo Menos um Caminho Válido em uma Grade

**Difícil**

Dada uma grade m x n. Cada célula da grade possui um sinal apontando para a próxima célula que você deve visitar se estiver atualmente nesta célula. O sinal de grid[i][j] pode ser:

- 1, que significa ir para a célula à direita. (ou seja, ir de grid[i][j] para grid[i][j + 1])
- 2, que significa ir para a célula à esquerda. (ou seja, ir de grid[i][j] para grid[i][j - 1])
- 3, que significa ir para a célula inferior. (ou seja, ir de grid[i][j] para grid[i + 1][j])
- 4, que significa ir para a célula superior. (ou seja, ir de grid[i][j] para grid[i - 1][j])

Observe que pode haver alguns sinais nas células da grade que apontam para fora da grade.

Você começará inicialmente na célula superior esquerda (0, 0). Um caminho válido na grade é um caminho que começa na célula superior esquerda (0, 0) e termina na célula inferior direita (m - 1, n - 1), seguindo os sinais na grade. O caminho válido **não** precisa ser o mais curto.

Você pode modificar o sinal em uma célula com **custo = 1**. Você pode modificar o sinal em uma célula apenas **uma vez**.

Retorne o custo mínimo para fazer com que a grade tenha pelo menos um caminho válido.

### Exemplo 1:

```
Entrada: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Saída: 3
Explicação: Você começará no ponto (0, 0).
O caminho até (3, 3) é o seguinte: 
(0, 0) --> (0, 1) --> (0, 2) --> (0, 3) altera a seta para baixo com custo = 1 
--> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) altera a seta para baixo com custo = 1 
--> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) altera a seta para baixo com custo = 1 
--> (3, 3)
O custo total = 3.
```

### Exemplo 2:

```
Entrada: grid = [[1,1,3],[3,2,2],[1,1,4]]
Saída: 0
Explicação: Você pode seguir o caminho de (0, 0) até (2, 2) sem alterações.
```

### Exemplo 3:

```
Entrada: grid = [[1,2],[4,3]]
Saída: 1
```

### Restrições:

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- 1 <= grid[i][j] <= 4

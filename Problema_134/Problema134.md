# 134. Gas Station

Existem `n` estações de gasolina dispostas em uma rota circular, onde a quantidade de gasolina na `i` estação é `gas[i]`.


Você tem um carro com um tanque de gasolina ilimitado e custa `cost[i]` de gasolina para viajar da estação `i` até a próxima estação `(i + 1)`. Você começa a viagem com o tanque vazio em uma das estações de gasolina.

Dadas duas listas de inteiros `gas` e `cost`, retorne o índice da estação de onde você pode começar a viagem para dar a volta completa no circuito no sentido horário. Caso não seja possível completar o circuito, retorne `-1`. Se existir uma solução, ela é garantida como sendo única.

## Exemplo 1:
**Entrada:** `gas = [1,2,3,4,5]`, `cost = [3,4,5,1,2]`  
**Saída:** `3`  
#### Explicação: 
- Comece na estação 3 (índice 3) e encha com 4 unidades de gasolina. Seu tanque = 0 + 4 = 4
- Vá para a estação 4. Seu tanque = 4 - 1 + 5 = 8
- Vá para a estação 0. Seu tanque = 8 - 2 + 1 = 7
- Vá para a estação 1. Seu tanque = 7 - 3 + 2 = 6
- Vá para a estação 2. Seu tanque = 6 - 4 + 3 = 5
- Vá para a estação 3. O custo é 5. Sua gasolina é suficiente apenas para voltar até a estação 3.
- Portanto, retorne 3 como o índice da estação de partida.

## Exemplo 2:
**Entrada:** `gas = [2,3,4]`, `cost = [3,4,3]`  
**Saída:** `-1`  
#### Explicação: 
- Você não pode começar na estação 0 ou 1, pois não há gasolina suficiente para viajar até a próxima estação.
- Vamos começar na estação 2 e abastecer com 4 unidades de gasolina. Seu tanque = 0 + 4 = 4
- Viaje até a estação 0. Seu tanque = 4 - 3 + 2 = 3  
- Viaje até a estação 1. Seu tanque = 3 - 3 + 3 = 3
- Você não pode voltar para a estação 2, pois isso requer 4 unidades de gasolina, mas você só tem 3.
- Portanto, não é possível dar a volta completa no circuito independentemente da estação de partida.


#### Restrições:
- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`
- `A entrada é gerada de forma que a resposta é única.`

# Solução
![Problema 134](https://github.com/projeto-de-algoritmos-2025/Greed_ExerciciosResolvidos-Leetcode/blob/d3537be1a8bf06524a7fafd69072effdf4a3cbdb/Problema_134/img/GasStation.png) <br>
*Problema 134 aceitação*

[Solução](https://github.com/projeto-de-algoritmos-2025/Greed_ExerciciosResolvidos-Leetcode/blob/d3537be1a8bf06524a7fafd69072effdf4a3cbdb/Problema_134/problema134.py)
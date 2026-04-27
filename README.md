# Calculadora de Troco em Python

Exercício em Python que calcula o troco ideal utilizando o menor número de moedas possível.

## Descrição

O programa recebe um valor em centavos (até 99) e exibe quais moedas devem ser usadas para formar esse valor, priorizando sempre as moedas de maior valor — técnica conhecida como **algoritmo guloso (greedy algorithm)**.

**Moedas disponíveis:** 1¢, 5¢, 10¢, 25¢ e 50¢

## Como executar

Certifique-se de ter o [Python 3](https://www.python.org/downloads/) instalado.

```bash
python exertroco.py
```

## Exemplo de uso

```
Digite o valor do pagamento até 99 centavos: 87
1 moeda(s) de 50 centavos
1 moeda(s) de 25 centavos
1 moeda(s) de 10 centavos
2 moeda(s) de 1 centavos
```

## Como funciona

1. O usuário informa o valor em centavos
2. A lista de moedas é ordenada do maior para o menor valor
3. O programa percorre cada moeda e verifica quantas cabem no valor restante
4. Exibe a quantidade de cada moeda e subtrai do total

## Estrutura do projeto

```
exercicio-troco-python/
 └── exertroco.py
```

## Tecnologias

- Python 3

---

Feito como exercício de lógica de programação.

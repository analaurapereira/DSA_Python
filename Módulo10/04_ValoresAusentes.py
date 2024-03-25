'''
Preenchendo Valores Ausentes em DataFrames do Pandas

A função fillna() é usada para preencher os valores ausentes. A função oferece muitas opções. Podemos usar 
um valor específico, uma função agregada (por exemplo, média) ou o valor anterior ou seguinte.

Para esse exemplo usaremos a moda, a estatística que representa o valor que aparece mais vezes em uma 
variável.
'''

import pandas as pd
from pandas import DataFrame

# Primeiro importamos um dataset
dsa_df = pd.read_csv("Módulo10/dataset.csv")
print(dsa_df.head(5))
dsa_df.isna().sum()
# Extraímos a moda da coluna Quantity
moda = dsa_df['Quantidade'].value_counts().index[0]
'''
A moda em Estatística é uma medida de tendência central que representa o valor mais frequente em um conjunto de dados.

A moda é especialmente útil quando queremos saber qual é o valor mais comum ou popular em um conjunto de dados, seja em uma  
distribuição unimodal (com apenas uma moda) ou em uma distribuição bimodal (com duas modas).

No entanto, a moda pode não ser tão representativa quanto outras medidas de tendência central, como a média e a mediana, 
especialmente em distribuições assimétricas ou quando há valores extremos. Por essa razão, é importante analisar diferentes 
medidas de tendência central e usar a que melhor se adequa aos objetivos da análise estatística.
'''
# E por fim preenchemos os valores NA com a moda
dsa_df['Quantidade'].fillna(value = moda, inplace = True)
print(dsa_df.isna().sum())
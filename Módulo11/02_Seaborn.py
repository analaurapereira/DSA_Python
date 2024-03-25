# Statistical Data Visualization com Seaborn
# https://seaborn.pydata.org/

# Imports
import random
import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import seaborn as sea

# Criando Gráficos com Seaborn
# Carregando um dos datasets que vem com o Seaborn
dados = sea.load_dataset("tips")
# O método joinplot cria plot de 2 variáveis com gráficos bivariados e univariados
sea.jointplot(data = dados, x = "total_bill", y = "tip", kind = 'reg')
# O método lmplot() cria plot com dados e modelos de regressão
sea.lmplot(data = dados, x = "total_bill", y = "tip", col = "smoker")
# Construindo um dataframe com Pandas
df = pd.DataFrame()
# Alimentando o Dataframe com valores aleatórios
df['idade'] = random.sample(range(20, 100), 30)
df['peso'] = random.sample(range(55, 150), 30)
# lmplot
sea.lmplot(data = df, x = "idade", y = "peso", fit_reg = True)
# kdeplot
sea.kdeplot(df.idade)
# distplot
sea.distplot(df.peso)
# Histograma
plt.hist(df.idade, alpha = .3)
sea.rugplot(df.idade)
# Box Plot
sea.boxplot(df.idade, color = 'm')
# Box Plot
sea.boxplot(df.peso, color = 'y')
# Violin Plot
sea.violinplot(df.idade, color = 'g')
# Clustermap
sea.clustermap(df)
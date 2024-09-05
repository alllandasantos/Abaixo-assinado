import pandas as pd
import matplotlib.pyplot as plt

# Dados das ruas e número de casas com moradores
data = {
    'Rua': ['Av. Concentrica', 'Av. Radial A', 'Av. Transversal Derba', 'Rua Moreira Cesar',
            'Rua Julio Leitão', 'Rua Coronel Tamarindo', 'Rua Escola Convenio',
            'Rua Maria Emilia', 'Trav. Moreira Cesar', 'Trav. Julio Leitão'],
    'Casas': [26, 10, 57, 32, 83, 133, 49, 57, 29, 17]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Total de casas e assinaturas atuais
total_casas = df['Casas'].sum()
assinaturas_atual = 215
objetivo_assinaturas = 215 * 1.3  # Aumento de 30%

# Calcular a porcentagem de assinaturas
percent_assinaturas_atual = (assinaturas_atual / total_casas) * 100
percent_objetivo = (objetivo_assinaturas / total_casas) * 100

# Visualizar com gráficos
plt.figure(figsize=(10, 6))
plt.bar(df['Rua'], df['Casas'], color='lightblue')
plt.axhline(y=percent_objetivo, color='r', linestyle='--', label=f'Objetivo: {percent_objetivo:.2f}%')
plt.axhline(y=percent_assinaturas_atual, color='g', linestyle='--', label=f'Atual: {percent_assinaturas_atual:.2f}%')
plt.title('Casas por Rua e Progresso das Assinaturas')
plt.xlabel('Ruas')
plt.ylabel('Número de Casas')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import imageio

# Definir pontos iniciais (um quadrado)
pontos = np.array([
    [-1, -1],
    [1, -1],
    [1, 1],
    [-1, 1],
    [-1, -1]  # Fechando o quadrado
])

# Função para aplicar transformação linear
def transformar_pontos(pontos, matriz):
    return np.dot(pontos, matriz.T)

# Criar frames para a animação
frames = []
n_frames = 30

for i in range(n_frames):
    angulo = (i / n_frames) * np.pi  # Rotação de 180 graus ao longo da animação
    escala = 1 + 0.5 * np.sin(i / n_frames * 2 * np.pi)  # Escala oscilante
    translacao = np.array([i * 0.1, i * 0.05])  # Translação progressiva

    # Matrizes de transformação
    matriz_rotacao = np.array([
        [np.cos(angulo), -np.sin(angulo)],
        [np.sin(angulo), np.cos(angulo)]
    ])
    matriz_escala = np.array([
        [escala, 0],
        [0, escala]
    ])
    
    # Aplicar transformações
    pontos_transformados = transformar_pontos(pontos, matriz_escala)
    pontos_transformados = transformar_pontos(pontos_transformados, matriz_rotacao)
    pontos_transformados += translacao  # Aplicar translação

    # Criar figura
    fig, ax = plt.subplots()
    ax.plot(pontos_transformados[:, 0], pontos_transformados[:, 1], 'bo-', markersize=5)
    ax.set_xlim(-3, 5)
    ax.set_ylim(-3, 5)
    ax.set_aspect('equal')
    plt.grid()
    
    # Salvar frame
    plt.savefig(f'frame_{i}.png')
    plt.close(fig)
    frames.append(imageio.imread(f'frame_{i}.png'))

# Criar GIF
imageio.mimsave('transformacao_linear.gif', frames, duration=0.1)

print("GIF criado com sucesso!")

import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

# Criar pasta para armazenar os frames
output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

# Comprimento do pêndulo
L = 5

# Ponto fixo do pêndulo
ponto_fixo = np.array([0, 0])

# Ponto inicial do pêndulo na posição vertical
ponto_pendulo = np.array([0, -L])

# Número de quadros da animação
n_frames = 60

# Lista para armazenar os frames da animação
frames = []

plt.ion()  # Ativar modo interativo para animação, atualizando o gráfico dinamicamente
fig, ax = plt.subplots() # cria figuras e eixos
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 1)
ax.set_aspect('equal') # Garantir que a escala dos eixos X e Y sejam igual.
plt.grid()
linha, = ax.plot([], [], 'bo-', markersize=5)
# b = Cor azul, o = Marca os pontos como círculos, - = Conecta os pontos com uma linha, markersize=5 Define o tamanho dos círculos

for i in range(n_frames):
    angulo = np.radians(30 * np.sin(2 * np.pi * i / n_frames))
    # Oscilação entre -30° e 30°
    # radians = converte o ângulo de graus para radianos, pois a matriz de rotação usa radianos.
    # Matriz de rotação : essa matriz multiplica a posição do pêndulo, girando em torno do ponto fixo (0,0)
    # Quando sin(...) = -1, temos -30° (ponto mais à esquerda).
    # Quando sin(...) = 0, temos 0° (posição central, vertical).
    # Quando sin(...) = 1, temos 30° (ponto mais à direita).
    
    matriz_rotacao = np.array([
        [np.cos(angulo), -np.sin(angulo)],
        [np.sin(angulo), np.cos(angulo)]
    ])
    # 1. Caso 1: Quando (posição vertical)
    # Se 𝜃 = 0°
    # 𝑅(0)=[ cos (0) −sin (0)
    #       sin(0)  cos(0)    ]
    #   =
    # [1 0
    #  0 1]
    # Isso é a matriz identidade, ou seja, não altera a posição do pêndulo.

    # 2. Caso 2: Quando 
    # Se 𝜃 = 30°
    # 𝑅(30°)=[ cos (30°) −sin (30°)
    #          sin(30°)  cos(30°)    ]
    # ⁡=
    # [ 0.866 −0.5
    #   0.5   0.866 ]
    # Isso significa que, ao multiplicar um ponto por essa matriz, ele será rotacionado em 30° no sentido anti-horário.

    # 3. Caso 3: Quando 
    # Se 𝜃 = -30°
    # 𝑅(-30°)=[ cos (-30°) −sin (-30°)
    #           sin(-30°)  cos(-30°)    ]
    # ⁡=
    #  [ 0.866 0.5
    #   -0.5   0.866 ]
    # Isso faz com que o ponto seja rotacionado 30° no sentido horário.

    # Aplicar rotação ao ponto do pêndulo
    ponto_rotacionado = np.dot(matriz_rotacao, ponto_pendulo)
    # Multiplicamos a matriz de rotação pelo vetor do pêndulo, obtendo a nova posição rotacionada.
    # 𝑃′= R(θ) ⋅ P
    
    # 4. Aplicação ao Pêndulo
    # O pêndulo começa na posição (0, -5) (pendurado para baixo), então sua posição inicial é:
    # 𝑃 = [0
    #      −5]
    # Agora, aplicamos a matriz de rotação R(θ) para encontrar sua nova posição 

    # Para 𝜃 = 30°:
    # 𝑃′=[0.866 −0.5
    #     0.5   0.866]
    #       x
    #    [0
    #    −5]

    # Fazendo a multiplicação:
    # 𝑃'x =(0.866 × 0) + (−0.5 × −5) = 2.5
    # 𝑃'y =(0.5 × 0) + (0.866 × −5) = −4.33
    
    # Então, a nova posição do pêndulo é aproximadamente:
    # P′=(2.5,−4.33)
    # Isso significa que o pêndulo se moveu para a direita e subiu um pouco, o que é esperado em um movimento oscilatório
    
    # Atualizar a posição da linha do pêndulo
    linha.set_data([ponto_fixo[0], ponto_rotacionado[0]], [ponto_fixo[1], ponto_rotacionado[1]])
    plt.pause(0.1)  # Criar efeito de animação
    
    # Salvar frame
    frame_path = os.path.join(output_dir, f'frame_{i}.png')
    plt.savefig(frame_path)
    frames.append(imageio.imread(frame_path))

plt.ioff()  # Desativar modo interativo

# Criar GIF
imageio.mimsave('pendulo.gif', frames, duration=0.1)

print("GIF do pêndulo criado com sucesso! As imagens foram salvas na pasta 'frames'.")

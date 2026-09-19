import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os

# Cria pasta para armazenar as imagens
os.makedirs("frames_hanoi", exist_ok=True)

# Função para desenhar as torres e discos
def desenhar_torres(torres, movimento):
    plt.clf()
    cores = ['orange', 'blue', 'green', 'red', 'purple', 'cyan']
    for i in range(3):
        plt.plot([i, i], [0, 10], color='black', linewidth=3)
    for i, torre in enumerate(torres):
        for j, disco in enumerate(torre):
            plt.bar(i, 0.5, bottom=j, width=disco/10, color=cores[disco % len(cores)], align='center')
    plt.xlim(-1, 3)
    plt.ylim(0, 10)
    plt.xticks([0, 1, 2], ['A', 'B', 'C'])
    plt.title(f"Movimento {movimento}")
    plt.savefig(f"frames_hanoi/mov_{movimento:03d}.png")  # salva cada frame
    plt.pause(0.05)  # pausa rápida só para visualização durante execução

# Função recursiva da Torre de Hanói com geração de frames
def torre_hanoi(n, origem, destino, auxiliar, torres, movimento=1):
    if n == 1:
        disco = torres[origem].pop()
        torres[destino].append(disco)
        print(f"{movimento}. Mova o disco de {chr(65+origem)} para {chr(65+destino)}")
        desenhar_torres(torres, movimento)
        return movimento + 1
    movimento = torre_hanoi(n-1, origem, auxiliar, destino, torres, movimento)
    disco = torres[origem].pop()
    torres[destino].append(disco)
    print(f"{movimento}. Mova o disco de {chr(65+origem)} para {chr(65+destino)}")
    desenhar_torres(torres, movimento)
    movimento += 1
    return torre_hanoi(n-1, auxiliar, destino, origem, torres, movimento)

# Programa principal
num_discos = int(input("Digite o número de discos: "))
torres = [list(range(num_discos, 0, -1)), [], []]
plt.figure(figsize=(6, 6))
desenhar_torres(torres, 0)
torre_hanoi(num_discos, 0, 2, 1, torres)
plt.close()

# Cria o GIF a partir dos frames salvos
frames = []
for arquivo in sorted(os.listdir("frames_hanoi")):
    if arquivo.endswith(".png"):
        frames.append(imageio.imread(f"frames_hanoi/{arquivo}"))

# Função de velocidade automática
min_movimentos = 2**num_discos - 1
# Quanto mais discos, menor a duração por frame
duracao = max(0.05, 0.5 - (num_discos * 0.02))

imageio.mimsave("torre_hanoi.gif", frames, duration=duracao)

print(f"\nGIF gerado com sucesso: torre_hanoi.gif 🎞️ (duração por frame: {duracao:.2f}s)")


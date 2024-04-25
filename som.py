import winsound
import time

# Frequência do som em Hertz (Hz)
frequencia = 440  # Exemplo: 440 Hz é a nota musical Lá

# Duração do som em milissegundos (ms)
duracao = 4000  # 1 segundo

# Emitir o som
winsound.Beep(frequencia, duracao)

# Esperar um pouco antes de encerrar o script (opcional)
time.sleep(2)

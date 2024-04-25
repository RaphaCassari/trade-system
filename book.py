import MetaTrader5 as mt5
import time
# estabelecemos a conexão ao MetaTrader 5
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
   # concluímos a conexão ao terminal MetaTrader 5
    mt5.shutdown()
    quit()

# subscreva para receber atualizações no livro de ofertas para o símbolo DOLK24 (Depth of Market)
if mt5.market_book_add('DOLK24'):
  # obtemos 10 vezes em um loop os dados do livro de ofertas
    for i in range(1000):
        # obtemos o conteúdo do livro de ofertas (Depth of Market)
        items = mt5.market_book_get('DOLK24')
        # exibimos todo o livro de ofertas como uma string tal qual como está
        # print(items)
        # agora exibimos cada solicitação separadamente para maior clareza
        if items:
            volume_total = 0
            for it in items:
                volume_total += it.volume
                # conteúdo da solicitação
                # print(it._asdict())
                if it.volume > 300:
                    print("Volume maior que 300")
                    import winsound
                    frequencia = 440
                    duracao = 4000
                    winsound.Beep(frequencia, duracao)
        volume_medio = volume_total / len(items)
        print(f"Volume total: {volume_total}, Volume médio: {volume_medio}")
        # vamos fazer uma pausa de 5 segundos antes da próxima solicitação de dados do livro de ofertas
        time.sleep(5)
  # cancelamos a subscrição de atualizações no livro de ofertas (Depth of Market)
    mt5.market_book_release('DOLK24')
else:
    print("mt5.market_book_add('DOLK24') failed, error code =", mt5.last_error())

# concluímos a conexão ao terminal MetaTrader 5
mt5.shutdown()

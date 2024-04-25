import MetaTrader5 as mt5

if not mt5.initialize():
    print("Falha ao inicializar o MetaTrader 5")
    mt5.shutdown()

ativo = 'DOLK24'

ativos_disponiveis = mt5.symbols_get(group='*' + ativo + '*')
if ativo in [ativo.name for ativo in ativos_disponiveis]:
    mt5.symbol_select(ativo, True)

    # Obter o último tick do ativo
    tick = mt5.symbol_info_tick(ativo)

    print(mt5.market_book_get(ativo))

    if tick is not None:
        preco_atual = tick.bid if tick.bid != 0 else tick.last
        print(f"Preço atual do {ativo}: {preco_atual}")
    else:
        print(f"Não foi possível obter o tick para {ativo}")

mt5.shutdown()

import MeCab
mecab = MeCab.Tagger("-Ochasen") # MeCabオブジェクトを作成
malista = mecab.parse("新しい地図は、皆さんと一緒につくる集いの場所です！") # 形態素解析を行う
print(malista)

from eleicao.sistema import *
arquivo = open("input/Partidos.txt", "r", encoding="utf-8")
for linha in arquivo:
    if linha.startswith("PARTIDO:"):
        dados = linha.replace("PARTIDO:", "").strip().split(",")
        try:
            Partido(dados[0], dados[1], dados[2], dados[3])
        except ErroCadastro:
            pass
arquivo.close()

arquivo = open("input/Eleitores.txt", "r", encoding="utf-8")
for linha in arquivo:
    try:
        if linha.startswith("ELEITOR:"):
            dados = linha.replace("ELEITOR:", "").strip().split(",")
            Eleitor(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5])

        elif linha.startswith("PREFEITO:"):
            dados = linha.replace("PREFEITO:", "").strip().split(",")
            Prefeito(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5],
                    dados[6], dados[7], dados[8], dados[9])

        elif linha.startswith("VEREADOR:"):
            dados = linha.replace("VEREADOR:", "").strip().split(",")
            Vereador(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5],
                    dados[6], dados[7], dados[8], dados[9])
    except ErroCadastro:
        pass


arquivo = open("input/Urnas.txt", "r", encoding="utf-8")

for linha in arquivo:
    if linha.startswith("VOTO:"):
        dados = linha.replace("VOTO:", "").strip().split(",")

        zona = dados[0]
        secao = dados[1]
        cpf = dados[2]
        cargo = dados[3]
        numero = dados[4]

        if (zona, secao) not in Urna.urnas:
            Urna(zona, secao)

        urna = Urna.urnas[(zona, secao)]

        try:
            urna.votar(numero, cargo)
        except ErroCadastro:
            pass

arquivo.close()



eleicao = Eleicao()
eleicao.eleitores()
eleicao.partidos()
eleicao.urnas()
eleicao.resultado_geral()
eleicao.erros()

print("Partidos:", Partido.total_partidos())
print("Eleitores:", Eleitor.contar_eleitores())
print("Prefeitos:", Prefeito.total_prefeitos())
print("Vereadores:", Vereador.total_vereadores())
print("Urnas:", len(Urna.urnas))
print("Relatóios criados em um novo arquivo .txt")

print("Prefeitos cadastrados:", Prefeito.prefeitos.keys())
print("Vereadores cadastrados:", Vereador.vereadores.keys())



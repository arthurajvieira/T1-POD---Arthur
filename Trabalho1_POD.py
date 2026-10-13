class Partido:
    def __init__(self, num, sigla, nome, cnpj): # nome max 50 carac cnpj max 14 num
        self.num = num
        self.sigla = sigla
        self.nome = nome
        self.cnpj = cnpj

        if len(nome) > 50:
            raise ValueError("Nome maior do que o permitido")
        if len(cnpj) > 14:
            raise ValueError("CNPJ inválido")

class Eleitor:
    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao): # nome max 50 e cpf max 11
        self.nome = nome
        self.cpf = cpf
        self.dat_nasc = dat_nasc
        self.titulo = titulo
        self.zona = zona
        self.secao = secao

        if len(nome) > 50:
            raise ValueError("Nome maior do que o permitido")
        if len(cpf) > 11:
            raise ValueError("CPF inválido!")

class Candidato(Eleitor): # -> conferir com class partido (def verificar candidato)
    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao, numero, partido):
        super().__init__(nome, cpf, dat_nasc, titulo, zona, secao)
        self.numero = numero
        self.partido = partido

    def verificar_candidato(self, numero): # assinatura de metodo
        pass # conferir se sao 2 numeros = pref ou 5 = vereador ???

class Prefeito(Candidato): # sub de candidato (cpf do vice e plano governo) // deve verificar o numero de partido class candid -> 2 digitos
    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao, numero, partido, cpf_vice, plano):
        super().__init__(nome, cpf, dat_nasc, titulo, zona, secao, numero, partido)
        self.cpf_vice = cpf_vice
        self.plano = plano

class Vereador(Candidato): #  deve verificar o numero (num de partido da class candid.) -> 5 digitos
    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao, numero, partido, bairro, projeto_lei):
            super().__init__(nome, cpf, dat_nasc, titulo, zona, secao, numero, partido)
            self.bairro = bairro
            self.projeto_lei = projeto_lei

class Urna: # zona, secao, votos p prefeito, votos p vereador
    def __init__(self, zona, secao, votos_p, votos_v):
        self.zona = zona
        self.secao = secao
        self.votos_p = votos_p
        self.votos_v = votos_v

class Eleicao: # relatorio dos candidatos, numeros, nomes
    pass
    def eleitores(self): # total de eleitores (inclui candidatos), total de candidatos a pref, tot cand veread, numero eleitores por zona
        pass

    def partidos(self): # total de partidos, para cada partido nome sigla e num cand a pref e veread
        pass

    def urnas(self): 
        pass

    def resultado_geral(self): # nome pref vencedor (mais 50%), se nao, segundo turno, nome 10 vereadores maior quant votos e seu qntd de votos
        pass

class ErroCadasto(Exception):
    pass
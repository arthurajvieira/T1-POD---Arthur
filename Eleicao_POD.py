from abc import ABC, abstractmethod

class Partido:
  erro = 0
  partidos = []

    def __init__(self, num, sigla, nome, cnpj): # nome max 50 carac cnpj max 14 num
        self.num = num
        self.sigla = sigla
        self.nome = nome
        self.cnpj = cnpj

        if len(nome) > 50:
            erro += 1
            raise ValueError("Nome maior do que o permitido")
        if len(cnpj) > 14:
            erro += 1
            raise ValueError("CNPJ inválido")

        Partido.partidos.append(self)

      def total_partidos():
        return len(Partido.partidos)

class Eleitor:
  erro = 0
  eleitores = []

    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao): # nome max 50 e cpf max 11
        self.nome = nome
        self.cpf = cpf
        self.dat_nasc = dat_nasc
        self.titulo = titulo
        self.zona = zona
        self.secao = secao

        if len(nome) > 50:
            erro += 1
            raise ValueError("Nome maior do que o permitido")
        if len(cpf) > 11:
            erro += 1
            raise ValueError("CPF inválido!")

        Eleitor.eleitores.append(self)

    def contar_eleitores():
      return len(Eleitor.eleitores)

class Candidato(Eleitor): # -> conferir com class partido (def verificar candidato)
    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao, numero, partido):
        super().__init__(nome, cpf, dat_nasc, titulo, zona, secao)
        self.numero = numero
        self.partido = partido

    @abstractmethod
    def verificar_candidato(self): # assinatura de metodo
        pass

class Prefeito(Candidato): # sub de candidato (cpf do vice e plano governo) // deve verificar o numero de partido class candid -> 2 digitos
  erro = 0
  prefeitos = []

    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao, numero, partido, cpf_vice, plano):
        super().__init__(nome, cpf, dat_nasc, titulo, zona, secao, numero, partido)
        self.cpf_vice = cpf_vice
        self.plano = plano

        if len(cpf_vice) != 11
        raise ErroCadastro("CPF do Vice Prefeito Inválido!") 

        Prefeito.prefeitos.append(self)

    def total_prefeitos():
      return len(Prefeito.prefeitos)

    def verificar_candidato(self):
      if len(self.numero) == 2:
        print("Candidato a prefeito válido!")
      else:
        erro += 1
        raise ErroCadastro("Candidato para prefeito inválido!")

class Vereador(Candidato): #  deve verificar o numero (num de partido da class candid.) -> 5 digitos
  erro = 0
  vereadores = []

    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao, numero, partido, bairro, projeto_lei):
            super().__init__(nome, cpf, dat_nasc, titulo, zona, secao, numero, partido)
            self.bairro = bairro
            self.projeto_lei = projeto_lei

            Vereador.vereadores.append(self)

    def total_vereadores():
      return len(Vereador.vereadores)

    def verificar_candidato(self):
      if len(self.numero) == 5:
        print("Candidato a vereador válido!")
      else:
        erro += 1
        raise ErroCadastro("Candidato para vereador inválido!")

class Urna: # zona, secao, votos p prefeito, votos p vereador
    def __init__(self, zona, secao, votos_p, votos_v):
        self.zona = zona
        self.secao = secao
        self.votos_p = votos_p
        self.votos_v = votos_v

    def __add__(self, votos_p, votos_v, outrosvotos_p, outrosvotos_v, p_totalvotos, v_totalvotos): # sobrecarga (?)
      self.p_totalvotos = self.votos_p + outrosvotos_p.votos_p     
      self.v_totalvotos = self.votos_v + outrosvotos_v.votos_v
      return Urna("Total votos para prefeito: ", self.votos_p + outrosvotos_p.votos_p, "Total de votos para vereador: ", self.votos_v + outrosvotos_v.votos_v)

class Eleicao: # relatorio dos candidatos, numeros, nomes
    pass
    def eleitores(self): # total de eleitores (inclui candidatos), total de candidatos a pref, tot cand veread, numero eleitores por zona
        pass

    def partidos(self): # total de partidos, para cada partido nome sigla e num cand a pref e veread
        pass

    def urnas(self):
        pass

    def resultado_geral(self): # nome pref vencedor (mais 50%), se nao, segundo turno, nome 10 vereadores maior quant votos e seu qntd de votos
        

class ErroCadasto(Exception):
    pass

class TotalErros():
  return "Total de erros: ", erro.Partido + erro.Eleitor + erro.Prefeito + erro.Vereador

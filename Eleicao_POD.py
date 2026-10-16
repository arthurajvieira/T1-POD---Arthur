from abc import ABC, abstractmethod

class Partido:
  erro = []
  partidos = {}

    def __init__(self, num, sigla, nome, cnpj): # nome max 50 carac cnpj max 14 num
        self.num = num
        self.sigla = sigla
        self.nome = nome
        self.cnpj = cnpj

        if len(nome) > 50:
            Partido.erro.append(1)
            raise ValueError("Nome maior do que o permitido")
        if len(cnpj) != 14:
            Partido.erro.append(1)
            raise ValueError("CNPJ inválido")

        Partido.partidos[self.num] = self

      @classmethod
      def total_partidos(cls):
        return len(cls.partidos)

      @classmethod
      def total_erros(cls):
        return len(cls.erro)

class Eleitor:
  erro = []
  eleitores = {}

    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao): # nome max 50 e cpf max 11
        self.nome = nome
        self.cpf = cpf
        self.dat_nasc = dat_nasc
        self.titulo = titulo
        self.zona = zona
        self.secao = secao

        if len(nome) > 50:
            Eleitor.erro.append(1)
            raise ValueError("Nome maior do que o permitido")
        if len(cpf) != 11:
            Eleitor.erro.append(1)
            raise ValueError("CPF inválido!")

        Eleitor.eleitores[self.nome] = self

    @classmethod
    def contar_eleitores(cls):
      return len(cls.eleitores)

    @classmethod
    def quantidade_erros(cls):
      return len(cls.erro)

class Candidato(Eleitor): # -> conferir com class partido (def verificar candidato)
  candidadtos = {}
  erros = []

    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao, numero, partido):
        super().__init__(nome, cpf, dat_nasc, titulo, zona, secao)
        self.numero = numero
        self.partido = partido

        if numero in Partido.partidos.items()
            Candidato.candidatos[self.numero] = self
        else:
          Candidato.erro.append(1)
          raise ValueError("Candidato Inválido!")

    @abstractmethod
    def verificar_candidato(self): # assinatura de metodo
        pass

    @classmethod
    def total_candidatos(cls):
      return len(cls.candidatos)

class Prefeito(Candidato): # sub de candidato (cpf do vice e plano governo) // deve verificar o numero de partido class candid -> 2 digitos
  erro = []
  prefeitos = {}

    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao, numero, partido, cpf_vice, plano):
        super().__init__(nome, cpf, dat_nasc, titulo, zona, secao, numero, partido)
        self.cpf_vice = cpf_vice
        self.plano = plano

        if len(cpf_vice) != 11
            Prefeito.erro.append(1)
            raise ErroCadastro("CPF do Vice Prefeito Inválido!")

        verificador_candidato(self)

    @classmethod
    def total_prefeitos(cls):
      return len(cls.prefeitos)

    def verificar_candidato(self):
      if len(self.numero) == 2:
        print("Candidato a prefeito válido!")
        Prefeito.prefeitos[self.numero] = self
      else:
        Prefeito.erro.append(1)
        raise ErroCadastro("Candidato para prefeito inválido!")

class Vereador(Candidato): #  deve verificar o numero (num de partido da class candid.) -> 5 digitos
  erro = []
  vereadores = {}

    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao, numero, partido, bairro, projeto_lei):
            super().__init__(nome, cpf, dat_nasc, titulo, zona, secao, numero, partido)
            self.bairro = bairro
            self.projeto_lei = projeto_lei

            verificar_candidato(self)
           

    @classmethod
    def total_vereadores(cls):
      return len(cls.vereadores)

    def verificar_candidato(self):
      if len(self.numero) == 5:
        Vereador.vereadores[self.numero] = self
        print("Candidato a vereador válido!")
      else:
        Vereador.erro.append(1)
        raise ErroCadastro("Candidato para vereador inválido!")

class Urna: # zona, secao, votos p prefeito, votos p vereador
    urna = {}
    total_votos = {}

    def __init__(self, zona, secao, voto):
        self.zona = zona
        self.secao = secao
        self.voto = voto

    def total_votos(self, votos_validos=0, votos_brancos=0, votos_nulos=0):
      self.votos_validos = votos_validos
      self.votos_brancos = votos_brancos
      self.votos_nulos = votos_nulos

      # puxar os numeros dos candidatos para testar com os numeros, pra saber se eh valido ou nao

        for self.voto, numero in Prefeito.prefeitos.items()  
           if len(self.voto) == 2 and self.voto == numero:
              votos_validos += 1

           elif len(self.voto) == 5 and self.voto == numero:
            votos_validos += 1

           elif self.voto == "":
            votos_branco += 1

           elif len(self.voto) != 2 and != 5 and != numero:
            votos_nulos += 1

      Urna.total_votos[self.votos_validos] = self


    def __add__(): # sobrecarga (?)
        total_votos /


class Eleicao: # relatorio dos candidatos, numeros, nomes
    pass
    def eleitores(self): # total de eleitores (inclui candidatos), total de candidatos a pref, tot cand veread, numero eleitores por zona
        total_eleitores = Eleitor.contar_eleitores()
        total_prefeitos = Prefeito.total_prefeitos()
        total_vereadores = Vereadores.total_vereadores()
        print("Relatório da Apuração dos Eleitores e Candidatos:")
        print()
        print("Total de Eleitores:", total_eleitores)
        print("Total de Candidatos a Prefeito:", total_prefeitos)
        print("Total de Candidatos a Vereador:", total_vereadores)
        print("Número de Eleitores por Zona:")
        print()

    def partidos(self): # total de partidos, para cada partido nome sigla e num cand a pref e veread
        total_partidos = Partidos.total_partidos()
        print("Relatório da Apuração dos Partidos:")
        print()
        print("Total de partidos:", Partidos.total_partidos())

        for nome, sigla, num in Partido.partidos.items():
          print("Partido:", nome, "Sigla:", sigla.partidos, " e número de candidato:", num.partidos)

    def urnas(self):
        print("Resultado Individual de Urna:")
        print()
        

    def resultado_geral(self): # nome pref vencedor (mais 50%), se nao, segundo turno, nome 10 vereadores maior quant votos e seu qntd de votos


class ErroCadasto(Exception):
    pass

class TotalErros():
  return "Total de erros: ", Partido.erro + Eleitor.erro + Prefeito.erro + Vereador.erro

from abc import ABC, abstractmethod

class Partido:
  erro = 0
  partidos = {}

  def __init__(self, num, sigla, nome, cnpj): # nome max 50 carac cnpj max 14 num
        self.num = str(num)
        self.sigla = sigla
        self.nome = nome
        self.cnpj = cnpj

        if len(nome) > 50:
            Partido.contar_erros()
            raise ErroCadastro("Nome maior do que o permitido")
        if len(cnpj) != 14:
            Partido.contar_erros()
            raise ErroCadastro("CNPJ inválido")

        if not cnpj.isdigit():
            Partido.contar_erros()
            raise ErroCadastro("CNPJ não pode conter letras!")

        if self.num in Partido.partidos:
          Partido.contar_erros()
          raise ErroCadastro("Partido já cadastrado!")

        Partido.partidos[self.num] = self

  @classmethod
  def total_partidos(cls):
        return len(cls.partidos)

  @classmethod
  def contar_erros(cls):
    cls.erro += 1

  @classmethod
  def total_erros(cls):
    return cls.erro

class Eleitor:
  erro = 0
  eleitores = {}

  def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao): # nome max 50 e cpf max 11
        self.nome = nome
        self.cpf = cpf
        self.dat_nasc = dat_nasc
        self.titulo = titulo
        self.zona = zona
        self.secao = secao

        if len(nome) > 50:
            Eleitor.contar_erros()
            raise ErroCadastro("Nome maior do que o permitido")
        if len(cpf) != 11:
            Eleitor.contar_erros()
            raise ErroCadastro("CPF inválido!")
        
        if not cpf.isdigit():
            Eleitor.contar_erros()
            raise ErroCadastro("CPF não pode conter letras!")

        if self.cpf in Eleitor.eleitores:
          Eleitor.contar_erros()
          raise ErroCadastro("Eleitor já cadastrado!")

        Eleitor.eleitores[self.cpf] = self

  @classmethod
  def contar_eleitores(cls):
      return len(cls.eleitores)

  @classmethod
  def contar_erros(cls):
    cls.erro += 1

  @classmethod
  def total_erros(cls):
    return cls.erro

class Candidato(Eleitor, ABC): # -> conferir com class partido (def verificar candidato)
  candidatos = {}
  erro = 0

  def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao, numero, partido):
        super().__init__(nome, cpf, dat_nasc, titulo, zona, secao)
        self.numero = numero
        self.partido = partido

        if self.partido not in Partido.partidos:
          Candidato.contar_erros()
          raise ErroCadastro("Partido Inválido!")
        
        if self.numero in Candidato.candidatos:
          Candidato.contar_erros()
          raise ErroCadastro("Candidato já cadastrado!")

  @abstractmethod
  def verificar_candidato(self): # assinatura de metodo
        pass

  @classmethod
  def total_candidatos(cls):
      return len(cls.candidatos)

  @classmethod
  def contar_erros(cls):
    cls.erro += 1

  @classmethod
  def total_erros(cls):
    return cls.erro

class Prefeito(Candidato): # sub de candidato (cpf do vice e plano governo) // deve verificar o numero de partido class candid -> 2 digitos
  erro = 0
  prefeitos = {}

  def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao, numero, partido, cpf_vice, plano):
        super().__init__(nome, cpf, dat_nasc, titulo, zona, secao, numero, partido)
        self.cpf_vice = cpf_vice
        self.plano = plano

        if len(cpf_vice) != 11:
            Prefeito.contar_erros()
            raise ErroCadastro("CPF do Vice Prefeito Inválido!")

        if not cpf_vice.isdigit()
          Prefeito.contar_erros()
          raise ErroCadastro("CPF deve conter apenas números!")

      

  @classmethod
  def total_prefeitos(cls):
      return len(cls.prefeitos)

  @classmethod
  def contar_erros(cls):
    cls.erro += 1

  @classmethod
  def total_erros(cls):
    return cls.erro

  def verificar_candidato(self):
      if len(self.numero) != 2 or not self.numero.isdigit():
        Prefeito.contar_erros()
        raise ErroCadastro("Candidato para prefeito inválido!")

    Prefeito.prefeitos[self.numero] = self

class Vereador(Candidato): #  deve verificar o numero (num de partido da class candid.) -> 5 digitos
  erro = 0
  vereadores = {}

  def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao, numero, partido, bairro, projeto_lei):
            super().__init__(nome, cpf, dat_nasc, titulo, zona, secao, numero, partido)
            self.bairro = bairro
            self.projeto_lei = projeto_lei

            self.verificar_candidato()

            Candidato.candidatos[self.numeros] = self
            Eleitor.eleitores[self.cpf] = self

           

  @classmethod
  def total_vereadores(cls):
      return len(cls.vereadores)

  @classmethod
  def contar_erros(cls):
    cls.erro += 1

  @classmethod
  def total_erros(cls):
    return cls.erro


  def verificar_candidato(self):
      if len(self.numero) != 5 or not self.numero.isdigit():
        Vereador.contar_erros()
        raise ErroCadastro("Candidato para vereador inválido!")

    Vereador.vereadores[self.numero] = self

class Urna: # zona, secao, votos p prefeito, votos p vereador
    urna = {}
    erro = 0

    def __init__(self, zona, secao, voto):
        self.zona = zona
        self.secao = secao
        
        self.votos_prefeito = {}
        self.votos_vereador = {}

        self.votos_validos = 0
        self.votos_brancos = 0
        self.votos_nulos = 0

        Urna.urnas[(zona, secao)] = self

    def votar(self, voto, cargo):
      voto = str(voto) # transformar o voto em string e nao em int

      if cargo == "prefeito":
        candidatos = Prefeito.prefeitos
        votos = self.votos_prefeitos

      elif cargo == "vereador":
        candidatos = Vereador.vereadores
        votos = self.votos_vereador

      else:
        raise ErroCadastro("Cargo Inválido!")

      if voto == ""
        self.votos_brancos += 1

      elif voto in candidatos:
        self.votos_validos += 1

      else:
        self.votos_nulos += 1

    @classmethod
    def contar_erros(cls):
      cls.erro += 1

    @classmethod
    def total_erros(cls):
      return cls.erro

    def total_votos(self, votos_validos=0, votos_brancos=0, votos_nulos=0):
      self.votos_validos = votos_validos
      self.votos_brancos = votos_brancos
      self.votos_nulos = votos_nulos

      # puxar os numeros dos candidatos para testar com os numeros, pra saber se eh valido ou nao

        for self.voto, numero in Prefeito.prefeitos.items():
           if len(self.voto) == 2 and self.voto == numero:
              votos_validos += 1

           elif len(self.voto) == 5 and self.voto == numero:
            votos_validos += 1

           elif self.voto == "":
            votos_branco += 1

           elif len(self.voto) != 2 and len(self.voto) != 5 and len(self.voto) != numero:
            votos_nulos += 1

      Urna.total_votos[self.votos_validos] = self


    def __add__(self, outra_urna): # sobrecarga (?)
        nova_urna = object.__new__(Urna)
        nova_urna.zona = None
        nova_urna.secao = None
        nova_urna.votos_prefeito = {}
        nova_urna.votos_vereador = {}

        nova_urna.votos_validos = self.votos_validos + outra_urna.votos_validos
        nova_urna.votos_brancos = self.votos_brancos + outra_urna.votos_validos
        nova_urna.votos_nulos = self.votos_nulos + outra_urna.votos_nulos

    for numero, quantidade in self.votos_prefeito.items():
        nova_urna.votos_prefeito[numero] = quantidade

    for numero, quantidade in outra.votos_prefeito.items():
        if numero not in nova_urna.votos_prefeito:
            nova_urna.votos_prefeito[numero] = 0

        nova_urna.votos_prefeito[numero] += quantidade

    for numero, quantidade in self.votos_vereador.items():
        nova_urna.votos_vereador[numero] = quantidade

    for numero, quantidade in outra.votos_vereador.items():
        if numero not in nova_urna.votos_vereador:
            nova_urna.votos_vereador[numero] = 0

        nova_urna.votos_vereador[numero] += quantidade

    return nova_urna



class Eleicao: # relatorio dos candidatos, numeros, nomes
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
        print("Número de Eleitores por Zona:")

        zonas = {}

        for eleitor in Eleitor.eleitores.values():
          if eleitor.zona not in zonas:
            zonas[eleitor.zona] = 0

        zonas[eleitor.zona] += 1

    for zona, quantidade in zonas.items():
        print("Zona:", zona, "- Eleitores:", quantidade)

    def partidos(self): # total de partidos, para cada partido nome sigla e num cand a pref e veread
        total_partidos = Partidos.total_partidos()
        print("Relatório da Apuração dos Partidos:")
        print()
        print("Total de partidos:", total_partidos())

        for numero, partido in Partido.partidos.items():
            prefeitos = 0
            vereadores = 0

        for candidato in Prefeito.prefeitos.values():
            if candidato.partido == numero:
                prefeitos += 1

        for candidato in Vereador.vereadores.values():
            if candidato.partido == numero:
                vereadores += 1

        print("Partido:", partido.nome)
        print("Sigla:", partido.sigla)
        print("Número:", numero)
        print("Candidatos a prefeito:", prefeitos)
        print("Candidatos a vereador:", vereadores)
        print()

    def urnas(self):
        
def urnas(self):
    print("Resultado Individual de Urna:")
    print()

    for urna in Urna.urnas.values():
        print("Zona:", urna.zona)
        print("Seção:", urna.secao)
        print()

        print("Votos válidos:", urna.votos_validos)
        print("Votos brancos:", urna.votos_brancos)
        print("Votos nulos:", urna.votos_nulos)
        print()

        print("Votos para Prefeito:")

        for numero, quantidade in urna.votos_prefeito.items():
            candidato = Prefeito.prefeitos[numero]
            print(candidato.nome, "-", quantidade, "votos")

        print("Votos para Vereador:")

        for numero, quantidade in urna.votos_vereador.items():
            candidato = Vereador.vereadores[numero]
            print(candidato.nome, "-", quantidade, "votos")

        print()


    def resultado_geral(self): # nome pref vencedor (mais 50%), se nao, segundo turno, nome 10 vereadores maior quant votos e seu qntd de votos
        
def resultado_geral(self):
    votos_prefeitos = {}
    votos_vereadores = {}

    for urna in Urna.urnas.values():

        for numero, quantidade in urna.votos_prefeito.items():
            if numero not in votos_prefeitos:
                votos_prefeitos[numero] = 0

            votos_prefeitos[numero] += quantidade

        for numero, quantidade in urna.votos_vereador.items():
            if numero not in votos_vereadores:
                votos_vereadores[numero] = 0

            votos_vereadores[numero] += quantidade

    print("RESULTADO GERAL DA ELEIÇÃO")
    print()

    print("Resultado para Prefeito:")

    if votos_prefeitos:
        total_validos = sum(votos_prefeitos.values())

        ranking = sorted(
            votos_prefeitos.items(),
            key=lambda item: item[1],
            reverse=True
        )

        numero, quantidade = ranking[0]
        prefeito = Prefeito.prefeitos[numero]

        percentual = quantidade / total_validos * 100

        print("Candidato mais votado:", prefeito.nome)
        print("Quantidade de votos:", quantidade)
        print("Percentual:", round(percentual, 2), "%")

        if percentual > 50:
            print("Prefeito eleito em primeiro turno!")
        else:
            print("Será necessário segundo turno!")

    else:
        print("Nenhum voto válido para prefeito.")

    print()
    print("10 Vereadores mais votados:")

    ranking_vereadores = sorted(
        votos_vereadores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for numero, quantidade in ranking_vereadores[:10]:
        vereador = Vereador.vereadores[numero]
        print(vereador.nome, "-", quantidade, "votos")


class ErroCadastro(Exception):
    pass


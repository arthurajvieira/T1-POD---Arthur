from abc import ABC, abstractmethod

class Partido:
    erro = 0
    partidos = {}

    def __init__(self, num, sigla, nome, cnpj): # nome max 50 carac cnpj max 14 num
        self.num = str(num)
        self.sigla = sigla
        self.nome = nome
        self.cnpj = str(cnpj)

        if len(nome) > 50 or len(self.cnpj) != 14 or not self.cnpj.isdigit():
            Partido.erro += 1
            raise ErroCadastro("Nome ou CNPJ do partido inválido")
        
        if len(self.num) != 2 or not self.num.isdigit() or self.num in Partido.partidos:
            Partido.erro += 1
            raise ErroCadastro("Número do partido inválido ou repetido")
        
        Partido.partidos[self.num] = self

    @classmethod
    def total_partidos(cls):
        return len(cls.partidos)


class Eleitor:
    erro = 0
    eleitores = {}

    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao): # nome max 50 e cpf max 11
        self.nome = nome
        self.cpf = str(cpf)
        self.dat_nasc = dat_nasc
        self.titulo = titulo
        self.zona = str(zona)
        self.secao = str(secao)

        if len(nome) > 50 or len(self.cpf) != 11 or not self.cpf.isdigit():
            Eleitor.erro += 1
            raise ErroCadastro("Nome ou CPF do eleitor inválido")
        if self.cpf in Eleitor.eleitores:
            Eleitor.erro += 1
            raise ErroCadastro("CPF já cadastrado")

        if type(self) == Eleitor:  # antes os objetos sem o if nao eram cadastrados diretamente pela classe
            Eleitor.eleitores[self.cpf] = self

    @classmethod
    def contar_eleitores(cls):
        return len(cls.eleitores)


class Candidato(Eleitor, ABC): # -> conferir com class partido (def verificar candidato)
    candidatos = {}
    erro = 0

    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao, numero, partido):
        super().__init__(nome, cpf, dat_nasc, titulo, zona, secao)
        self.numero = str(numero)
        self.partido = str(partido)

        if self.partido not in Partido.partidos:
            Candidato.erro += 1
            raise ErroCadastro("Partido do candidato não encontrado")
        if self.numero in Candidato.candidatos:
            Candidato.erro += 1
            raise ErroCadastro("Número de candidato repetido")

    @abstractmethod
    def verificar_candidato(self): # assinatura de metodo
        pass

    @classmethod
    def total_candidatos(cls):
        return len(cls.candidatos)


class Prefeito(Candidato): # sub de candidato (cpf do vice e plano governo) // deve verificar o numero de partido class candid -> 2 digitos
    erro = 0
    prefeitos = {}

    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao, numero, partido, cpf_vice, plano):
        super().__init__(nome, cpf, dat_nasc, titulo, zona, secao, numero, partido)
        self.cpf_vice = str(cpf_vice)
        self.plano = plano

        if len(self.cpf_vice) != 11 or not self.cpf_vice.isdigit():
            Prefeito.erro += 1
            raise ErroCadastro("CPF do vice-prefeito inválido")

        self.verificar_candidato()
        Prefeito.prefeitos[self.numero] = self
        Candidato.candidatos[self.numero] = self
        Eleitor.eleitores[self.cpf] = self

    def verificar_candidato(self):
        if len(self.numero) != 2 or not self.numero.isdigit() or self.numero != self.partido:
            Prefeito.erro += 1
            raise ErroCadastro("Número de prefeito inválido")

    @classmethod
    def total_prefeitos(cls):
        return len(cls.prefeitos)


class Vereador(Candidato): #  deve verificar o numero (num de partido da class candid.) -> 5 digitos
    erro = 0
    vereadores = {}

    def __init__(self, nome, cpf, dat_nasc, titulo, zona, secao, numero, partido, bairro, projeto_lei):
        super().__init__(nome, cpf, dat_nasc, titulo, zona, secao, numero, partido)
        self.bairro = bairro
        self.projeto_lei = projeto_lei

        self.verificar_candidato()
        Vereador.vereadores[self.numero] = self
        Candidato.candidatos[self.numero] = self
        Eleitor.eleitores[self.cpf] = self

    def verificar_candidato(self):
        if len(self.numero) != 5 or not self.numero.isdigit() or self.numero[:2] != self.partido:
            Vereador.erro += 1
            raise ErroCadastro("Número de vereador inválido")

    @classmethod
    def total_vereadores(cls):
        return len(cls.vereadores)


class Urna:  # zona, secao, votos p prefeito, votos p vereador
    urnas = {}

    def __init__(self, zona, secao):
        self.zona = str(zona)
        self.secao = str(secao)

        self.votos_prefeito = {}
        self.votos_vereador = {}

        self.brancos_prefeito = 0
        self.brancos_vereador = 0
        self.nulos_prefeito = 0
        self.nulos_vereador = 0

        Urna.urnas[(self.zona, self.secao)] = self

    def votar(self, voto, cargo):
        
        if cargo == "prefeito":
            candidatos = Prefeito.prefeitos
            votos = self.votos_prefeito

        elif cargo == "vereador":
            candidatos = Vereador.vereadores
            votos = self.votos_vereador

        else:
            raise ErroCadastro("Cargo inválido")

        if voto == "":
            if cargo == "prefeito":
                self.brancos_prefeito += 1
            else:
                self.brancos_vereador += 1

        elif voto in candidatos:
            if voto not in votos:
                votos[voto] = 0
            votos[voto] += 1

        else:
            if cargo == "prefeito":
                self.nulos_prefeito += 1

            else:
                self.nulos_vereador += 1

    def __add__(self, outra):
        soma = object.__new__(Urna)

        soma.zona = "TOTAL"
        soma.secao = "TOTAL"
        soma.votos_prefeito = self.votos_prefeito.copy()
        soma.votos_vereador = self.votos_vereador.copy()

        soma.brancos_prefeito = self.brancos_prefeito + outra.brancos_prefeito
        soma.brancos_vereador = self.brancos_vereador + outra.brancos_vereador
        soma.nulos_prefeito = self.nulos_prefeito + outra.nulos_prefeito
        soma.nulos_vereador = self.nulos_vereador + outra.nulos_vereador

        for numero, quantidade in outra.votos_prefeito.items():
            if numero not in soma.votos_prefeito:
                soma.votos_prefeito[numero] = 0
            soma.votos_prefeito[numero] += quantidade

        for numero, quantidade in outra.votos_vereador.items():
            if numero not in soma.votos_vereador:
                soma.votos_vereador[numero] = 0
            soma.votos_vereador[numero] += quantidade

        return soma


class TotalErros:
    @classmethod
    def total_erros(cls):
        return Partido.erro + Eleitor.erro + Candidato.erro + Prefeito.erro + Vereador.erro

class ErroCadastro(Exception):
    mensagens = [] # pra guardar os erros certinho

    def __init__(self, mensagem):
        ErroCadastro.mensagens.append(mensagem)
    
class Eleicao:
    def eleitores(self):
        zonas = {}
        secoes = {}

        for eleitor in Eleitor.eleitores.values():
            zona = eleitor.zona
            chave = (eleitor.zona, eleitor.secao)

            if zona not in zonas:
                zonas[zona] = 0

            if chave not in secoes:
                secoes[chave] = 0

            zonas[zona] += 1
            secoes[chave] += 1

        with open("relatorio_eleitores.txt", "w", encoding="utf-8") as arquivo: # usei o chat pra essa parte de abrir txt!!!
            arquivo.write("Relatorio de Eleitores:")
            arquivo.write("Total: " + str(Eleitor.contar_eleitores()) + "\n")
            arquivo.write("Prefeitos: " + str(Prefeito.total_prefeitos()) + "\n")
            arquivo.write("Vereadores: " + str(Vereador.total_vereadores()) + "\n")

            for zona, quantidade in zonas.items():
                arquivo.write("Zona " + zona + ": " + str(quantidade) + " eleitores\n")
            for chave, quantidade in secoes.items():
                arquivo.write("Zona " + chave[0] + " / Seção " + chave[1] + ": " + str(quantidade) + "\n")

    def partidos(self):
        with open("relatorio_partidos.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("RELATÓRIO DE PARTIDOS\n")
            arquivo.write("Total: " + str(Partido.total_partidos()) + "\n")
            for numero, partido in Partido.partidos.items():
                prefeitos = 0
                vereadores = 0
                for candidato in Prefeito.prefeitos.values():
                    if candidato.partido == numero:
                        prefeitos += 1
                for candidato in Vereador.vereadores.values():
                    if candidato.partido == numero:
                        vereadores += 1
                arquivo.write(partido.nome + " (" + partido.sigla + ") - " + numero + "\n")
                arquivo.write("Prefeitos: " + str(prefeitos) + " / Vereadores: " + str(vereadores) + "\n")

    def urnas(self):
        with open("relatorio_urnas.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("RELATÓRIO DAS URNAS\n")

            # tudo em string pra transformar o resultado numérico e poder contatenar e pro write conseguir usar
            for urna in Urna.urnas.values():
                arquivo.write("\nZona " + urna.zona + " / Seção " + urna.secao + "\n")
                arquivo.write("Prefeito - válidos: " + str(sum(urna.votos_prefeito.values())) +
                              ", brancos: " + str(urna.brancos_prefeito) +
                              ", nulos: " + str(urna.nulos_prefeito) + "\n")
                arquivo.write("Vereador - válidos: " + str(sum(urna.votos_vereador.values())) +
                              ", brancos: " + str(urna.brancos_vereador) +
                              ", nulos: " + str(urna.nulos_vereador) + "\n")
                
                for numero, quantidade in urna.votos_prefeito.items():
                    arquivo.write("Prefeito " + numero + ": " + str(quantidade) + " votos\n")
                    
                for numero, quantidade in urna.votos_vereador.items():
                    arquivo.write("Vereador " + numero + ": " + str(quantidade) + " votos\n")

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
                
        # encoding pro python nao brigar com os caracteres do pt br
        # w é o modo de escrita (tipo terminal linux)
        
        with open("relatorio_resultado.txt", "w", encoding="utf-8") as arquivo: 
            arquivo.write("RESULTADO GERAL\n")
            if votos_prefeitos:
                # sorted p ordenar do menor p maior, reverse pra pegar e deixar do mais votado pro menos, key pra mostrar a quantia de votos
                ranking = sorted(votos_prefeitos, key=votos_prefeitos.get, reverse=True) 
                numero = ranking[0]
                quantidade = votos_prefeitos[numero]
                total = sum(votos_prefeitos.values())
                arquivo.write("Mais votado: " + Prefeito.prefeitos[numero].nome + "\n")
                arquivo.write("Votos: " + str(quantidade) + "\n")
                arquivo.write("Percentual: " + str(round(quantidade / total * 100, 2)) + "%\n")
                if quantidade * 2 >= total:
                    arquivo.write("Prefeito eleito (regra do exercício)\n")
                else:
                    arquivo.write("Segundo turno necessário\n")
            else:
                arquivo.write("Nenhum voto válido para prefeito\n")
                
            arquivo.write("\n10 Vereadores mais votados!\n")
            ranking = sorted(votos_vereadores, key=votos_vereadores.get, reverse=True)
            
            for numero in ranking[:10]: # os 10 mais votados, do 0 ao 9
                quantidade = votos_vereadores[numero]
                arquivo.write(Vereador.vereadores[numero].nome + " - " + str(quantidade) + " votos\n")

    def erros(self):
        with open("relatorio_erros.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("Relatorio de Erros\n")
            for mensagem in ErroCadastro.mensagens:
                arquivo.write(mensagem + "\n")
            arquivo.write("Erros de partidos: " + str(Partido.erro) + "\n")
            arquivo.write("Erros de eleitores: " + str(Eleitor.erro) + "\n")
            arquivo.write("Erros de candidatos: " + str(Candidato.erro) + "\n")
            arquivo.write("Erros de prefeitos: " + str(Prefeito.erro) + "\n")
            arquivo.write("Erros de vereadores: " + str(Vereador.erro) + "\n")
            arquivo.write("Total: " + str(TotalErros.total_erros()) + "\n")

# o r aqui é pra ler o arquivo e nao escrever <-
arquivo = open("Partidos.txt", "r", encoding="utf-8")

for linha in arquivo:
    if linha.startswith("PARTIDO:"): # se a linha começar com PARTIDO vai executar 
        # replace vai tirar o partido (por causa dos dados do txt)
        # split pra conseguir separar as informações bonitinhas ao invés de tudo em uma linha
        dados = linha.replace("PARTIDO:", "").strip().split(",") 
        try:
            # 0 [numero] / 1 [sigla] / 2 [nome partido] / 3 [cpf]
            Partido(dados[0], dados[1], dados[2], dados[3])
        except ErroCadastro:
            pass
arquivo.close()

arquivo = open("Eleitores.txt", "r", encoding="utf-8")
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

arquivo = open("Urnas.txt", "r", encoding="utf-8")
for linha in arquivo:
    if linha.startswith("VOTO:"):
        dados = linha.replace("VOTO:", "").strip().split(",")
        zona = dados[0]
        secao = dados[1]
        cpf = dados[2]
        cargo = dados[3]
        numero = dados[4]

        # A urna é identificada pela zona e seção do arquivo.
        if (zona, secao) not in Urna.urnas:
            Urna(zona, secao)
        urna = Urna.urnas[(zona, secao)]
        try:
            urna.votar(numero, cargo)
        except ErroCadastro:
            pass


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

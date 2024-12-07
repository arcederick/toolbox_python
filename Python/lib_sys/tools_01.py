#################################
#################################
# 1 - Manipulação de exceções não tratadas
# 2 - Obtenção de Informações sobre o Ambiente Python
# 3 - Manipulação de Configurações do Interpretador
# 4 - Manipulação de Entradas e Saídas Padrão
# 5 - Interagindo com o Gerenciador de Contexto do sys
#################################
#################################
import sys

# 1 - Manipulação de exceções não tratadas
class ExcecaoNaoTratada:
    def __init__(self):
        pass

    def excecao_nao_tratada(self, exc_type, exc_value, exc_traceback):
        print("Ocorreu uma exceção não tratada:")
        print("Tipo:", exc_type)
        print("Valor:", exc_value)
        print("Rastreamento:", exc_traceback)

    def ativar_monitoramento_excecoes(self):
        sys.excepthook = self.excecao_nao_tratada

excecao_monitor = ExcecaoNaoTratada()
excecao_monitor.ativar_monitoramento_excecoes()
# Aqui você pode adicionar código que gera uma exceção não tratada para testar a funcionalidade
# raise ValueError("Exemplo de exceção não tratada")

# 2 - Obtenção de Informações sobre o Ambiente Python
class InformacoesAmbientePython:
    def __init__(self):
        pass

    def obter_info_ambiente(self):
        print("Versão do Python:", sys.version)
        print("Plataforma:", sys.platform)
        print("Prefixo do Executável:", sys.exec_prefix)
        print("Caminho do Módulo:", sys.path)

info_ambiente = InformacoesAmbientePython()
info_ambiente.obter_info_ambiente()

# 3 - Manipulação de Configurações do Interpretador
class ConfiguracaoInterpretador:
    def __init__(self):
        pass

    def alterar_variavel_interpretador(self, variavel, valor):
        setattr(sys, variavel, valor)

config_interpretador = ConfiguracaoInterpretador()
config_interpretador.alterar_variavel_interpretador("maxsize", 99999)
print("Tamanho máximo de um objeto:", sys.maxsize)

# 4 - Manipulação de Entradas e Saídas Padrão
class ManipulacaoEntradaSaida:
    def __init__(self):
        pass

    def ler_linhas_entrada_padrao(self):
        for linha in sys.stdin:
            print("Entrada Padrão:", linha)

    def redirecionar_saida_padrao(self):
        sys.stdout = open('saida.txt', 'w')
        print("Este é um teste de saída padrão redirecionada.")
        sys.stdout.close()

manipulador_io = ManipulacaoEntradaSaida()
manipulador_io.ler_linhas_entrada_padrao()
manipulador_io.redirecionar_saida_padrao()

# 5 - Interagindo com o Gerenciador de Contexto do sys
class GerenciadorContextoSys:
    def __init__(self):
        pass

    def __enter__(self):
        print("Entrando no contexto")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Saindo do contexto")
        if exc_type:
            print("Ocorreu uma exceção:", exc_type)

with GerenciadorContextoSys() as contexto:
    print("Dentro do contexto")
    # Adicione código que pode lançar exceções para testar a funcionalidade de saída do contexto
    # raise ValueError("Exemplo de exceção")

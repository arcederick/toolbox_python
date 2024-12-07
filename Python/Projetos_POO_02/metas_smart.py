class MetaSMART:
    def __init__(self, titulo, descricao, data_limite, metrica, resultado_esperado):
        self.titulo = titulo
        self.descricao = descricao
        self.data_limite = data_limite
        self.metrica = metrica
        self.resultado_esperado = resultado_esperado
        self.concluida = False

    def __str__(self):
        estado = "Concluída" if self.concluida else "Pendente"
        return (
            f"Título: {self.titulo}\n"
            f"Descrição: {self.descricao}\n"
            f"Data Limite: {self.data_limite}\n"
            f"Métrica: {self.metrica}\n"
            f"Resultado Esperado: {self.resultado_esperado}\n"
            f"Status: {estado}\n"
        )

class GerenciadorMetas:
    def __init__(self):
        self.metas = []

    def adicionar_meta(self, meta):
        self.metas.append(meta)

    def marcar_meta_como_concluida(self, titulo):
        for meta in self.metas:
            if meta.titulo == titulo:
                meta.concluida = True

    def listar_metas(self):
        return self.metas

if __name__ == "__main__":
    gerenciador = GerenciadorMetas()

    # Adicionar metas
    meta1 = MetaSMART("Aprender Python", "Dominar Python em 6 meses", "31/12/2023", "Nível de conhecimento", "Domínio das principais bibliotecas")
    meta2 = MetaSMART("Projeto de Desenvolvimento Web", "Concluir projeto de site pessoal", "15/11/2023", "Entrega do projeto", "Site totalmente funcional")
    
    gerenciador.adicionar_meta(meta1)
    gerenciador.adicionar_meta(meta2)

    # Marcar uma meta como concluída
    gerenciador.marcar_meta_como_concluida("Aprender Python")

    # Listar todas as metas
    metas = gerenciador.listar_metas()
    for meta in metas:
        print(meta)
from projeto.organizador import OrganizadorDeFilmes

if __name__ == "__main__":
    organizador = OrganizadorDeFilmes("movies.csv")
    organizador.renomear_colunas()
    organizador.limpar_titulos_e_generos()
    organizador.tratar_valores_nulos()
    organizador.remover_duplicatas()
    organizador.organizar_e_renumerar()
    organizador.mostrar_amostra()
    organizador.salvar_novo_csv("filmes_organizados.csv")


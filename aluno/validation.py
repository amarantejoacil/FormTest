def verificar_senha_iguais(senha, repete_senha, lista_de_erros):
    """Verifica se os campos são iguais"""
    if senha != repete_senha:
        lista_de_erros['repete_senha'] = 'Atenção: As senhas digitadas não são IGUAIS!'


def verifica_numero_existe_em_texto(input_dados, campo_validado, lista_de_erros):
    """Verifica se a senha possui numero, só pode letra"""
    if any(char.isdigit() for char in input_dados):
        lista_de_erros[campo_validado] = 'Atenção: Não inclua numero neste campo!'
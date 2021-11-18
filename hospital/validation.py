def verifica_num_text(texto,campo_validado, lista_erros):
    """Verifica se a senha possui numero, só pode letra"""
    if any(char.isdigit() for char in texto):
        lista_erros[campo_validado] = 'Atenção: Não inclua numero neste campo!'

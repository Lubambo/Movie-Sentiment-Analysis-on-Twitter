def translate_words(names_list):

    translated_list = []

    for i in range(len(names_list)):
        if names_list[i] == 'movie':
            translated_list.append('Filme')

        elif names_list[i] == 'soundtrack':
            translated_list.append('Trilha sonora')

        elif names_list[i] == 'plot':
            translated_list.append('Enredo')

        elif names_list[i] == 'director':
            translated_list.append('Direção')

        elif names_list[i] == 'music':
            translated_list.append('Música')

        elif names_list[i] == 'cast':
            translated_list.append('Elenco')

    return translated_list
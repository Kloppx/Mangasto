from django.shortcuts import render
# Dicionário com as cores associadas a cada gênero de mangá
GENRE_COLORS = {
    'Ação': '#b81414',
    'Aventura': '#e5e619',
    'Fantasia': '#f17ea1',
    'Terror': '#111111',
    'Comédia': '#ff8c00',
    'Drama': '#723172',
    'Ficção Científica': '#0c6834',
    'Sobrenatural': '#6a0c68',
    'Épico': '#0c6868'
}

mangas = [
    {
        'id' : 1,
        'title': 'Solo Leveling',
        'description': 'Solo Leveling é um manhwa sul-coreano que segue Sung Jin-Woo, um caçador considerado o mais fraco de todos. Após um evento misterioso em uma dungeon, ele ganha a habilidade de ficar mais forte sozinho, como em um jogo de RPG. Com isso, ele sobe de nível rapidamente, se tornando um dos caçadores mais poderosos do mundo. A história mistura ação, fantasia e muita evolução de personagem.',
        'img_path': 'https://m.media-amazon.com/images/I/816hywlmu-L.jpg',
        'gender': ['Ação','Fantasia'],
        'color_gender': [GENRE_COLORS['Ação'], GENRE_COLORS['Fantasia']]
    },
    {
        'id' : 2,
        'title': 'Attack on Titan',
        'description': 'Attack on Titan se passa em um mundo onde a humanidade vive cercada por muralhas para se proteger de Titãs gigantes devoradores de pessoas. A história segue Eren Yeager, que jura exterminar todos os Titãs após sua cidade ser destruída. Com reviravoltas intensas, batalhas brutais e segredos chocantes, o anime e mangá exploram temas como liberdade, guerra e sobrevivência.',
        'img_path': 'https://m.media-amazon.com/images/I/91k+L3q+25L._SY466_.jpg',
        'gender': ['Ação', 'Fantasia'],
        'color_gender': [GENRE_COLORS['Ação'], GENRE_COLORS['Fantasia']]
    },
    {
        'id' : 3,
        'title': 'Jujutsu Kaisen',
        'description': 'Jujutsu Kaisen segue Yuji Itadori, um estudante colegial que se torna um feiticeiro após ingerir um dedo amaldiçoado. Ele se junta a outros feiticeiros para combater maldições e proteger a humanidade. Com lutas intensas, personagens carismáticos e uma trama envolvente, o anime e mangá se tornaram um sucesso mundial.',
        'img_path': 'https://i0.wp.com/blogbbm.com/wp-content/uploads/2020/07/Jujutsu-kaisen.jpg?fit=614%2C900&ssl=1',
        'gender': ['Aventura', 'Fantasia'],
        'color_gender': [GENRE_COLORS['Aventura'], GENRE_COLORS['Fantasia']]
    },
    {
        'id' : 4,
        'title': 'DanDaDan',
        'description': 'DanDaDan é um mangá de terror que segue a história de Dan, um garoto que se muda para uma nova cidade e descobre que ela é assombrada por fantasmas. Com um estilo de arte único e uma atmosfera assustadora, DanDaDan é uma leitura envolvente para os fãs de terror.',
        'img_path': 'https://d14d9vp3wdof84.cloudfront.net/image/589816272436/image_825auoj75l5pld1tcjc2c4u503/-S897-FWEBP',
        'gender': ['Ação', 'Comédia'],
        'color_gender': [GENRE_COLORS['Ação'], GENRE_COLORS['Comédia']]
    },
    {
        'id' : 5,
        'title': 'Viland Saga',
        'description': 'Viland Saga é um mangá de ação e drama histórico que segue a jornada de Thorfinn, um jovem viking em busca de vingança contra o assassino de seu pai. Com batalhas épicas, personagens complexos e uma narrativa emocionante, o mangá é uma leitura imperdível para os fãs de histórias de vikings e aventuras.',
        'img_path': 'https://d14d9vp3wdof84.cloudfront.net/image/589816272436/image_p4uugvjt7p6e93tqi1hh3kkt7p/-S897-FWEBP',
        'gender': ['Aventura', 'Épico'],
        'color_gender': [GENRE_COLORS['Aventura'], GENRE_COLORS['Épico']]
    },
    {
        'id' : 6,
        'title': 'Kaiju No. 8',
        'description': 'Kaiju No. 8 é um mangá de ação e comédia que segue Kafka Hibino, um funcionário de limpeza de kaijus que sonha em se tornar um caçador de kaijus. Quando ele acidentalmente se transforma em um kaiju, Kafka se vê no meio de uma batalha entre humanos e monstros. Com uma mistura de humor e ação, o mangá é uma leitura divertida para os fãs de kaijus e aventuras.',
        'img_path': 'https://m.media-amazon.com/images/I/812qiXhyN+L.jpg',
        'gender': ['Ação', 'Aventura', 'Ficção Científica'],
        'color_gender': [GENRE_COLORS['Ação'], GENRE_COLORS['Aventura'], GENRE_COLORS['Ficção Científica']]
    }
]

# Combina os gêneros e as cores para garantir que é uma lista de tuplas
for manga in mangas:
    manga['genders_with_colors'] = list(zip(manga['gender'], manga['color_gender']))

def detail_manga(request, manga_id):
    try:
        manga = mangas[int(manga_id) - 1]  # Obtém o mangá pelo índice
        context = {
            'manga': manga  # Passando como 'manga', e não 'mangas'
        }
        return render(request, 'mangas/detail_manga.html', context)
    except (IndexError, ValueError):
        return render(request, 'mangas/detail_manga.html', {'manga': None})
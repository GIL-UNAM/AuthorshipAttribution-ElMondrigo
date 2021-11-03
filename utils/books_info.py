books = {
    231: ['Alberto Chimal', 'El carnaval de Ray Bradbury'],
    232: ['Alberto Chimal', 'La ciudad invisible'],
    233: ['Alberto Chimal', 'Manifiesto del cuento mutante'],
    234: ['Alberto Chimal', 'El juego más antiguo'],
    235: ['Alberto Chimal', 'La idea de México'],
    236: ['Alberto Chimal', 'JLB y la CF'],
    237: ['Alberto Chimal', 'Lo fantástico en México: la vida en el margen'],
    238: ['Alberto Chimal', 'Mogo'],
    239: ['Alberto Chimal', 'La pasión según la sombra'],
    68781: ['Gregorio Ortega Hernández','México resistió a la C.I.A. y a Fidel Castro'],
    68783: ['Gregorio Ortega Hernández','Un chamaco de Tepito da una lección de civismo'],
    68785: ['Gregorio Ortega Hernández','Un injusto artículo de Blanco Moheno'],
    68787: ['Anónimo','El Móndrigo'],
    68793: ['Roberto Blanco Moheno','La noticia detrás de la noticia 2'],
    68795: ['Roberto Blanco Moheno','La noticia detrás de la noticia 3'],
    68797: ['Jorge Joseph','Picaluga Vende a los Rojo Gomistas por una Curul Senatorial'],
    68799: ['Jorge Joseph', 'Pitoloco en Palacio'],
    68801: ['Jorge Joseph','Aviso'],
    68803: ['Jorge Joseph' ,'Pruebas de la existencia de la Atlántida'],
    68805: ['Jorge Joseph' ,'Esoterismo en Anahuac'],
    68807: ['Gregorio Ortega Molina','¿Hacia la extrema derecha?'],
    68809: ['Gregorio Ortega Molina','La guerra de los zombies'],
    68811: ['Gregorio Ortega Molina','La sociedad del átomo'],
    68813: ['Emilio Uranga','Universidad Popular'],
    68815: ['Emilio Uranga','La Represión Extremada'],
    68817: ['Emilio Uranga','La Ambigüedad Universitaria'],
    68819: ['Emilio Uranga','Ornato y Orden'],
    68821: ['Emilio Uranga','Viaje del Canciller'],
    68823: ['Emilio Uranga','Prólogo de Astucias literarias'],
    68825: ['Emilio Uranga','De Astucias literarias 1'],
    68827: ['Emilio Uranga','De Astucias literarias 2'],
    68829: ['Emilio Uranga','Lectura de galeras de De Astucias literarias'],
    68831: ['Roberto Blanco Moheno','Tlatelolco. Historia de una infamia'],
    68833: ['Roberto Blanco Moheno','La noticia detrás de la noticia 1'],
}

train_keys_base = [68781, 68783, 68795, 68799, 68805, 68807, 68811, 68819, 68823, 68827, 68829, 68831]
test_keys_base = [68785, 68793, 68797, 68801, 68803, 68809, 68813, 68815, 68817, 68821, 68825, 68833]

train_keys_full = [231, 233, 235, 238, 68781, 68783, 68795, 68799, 68805, 68807, 68811, 68819, 68823, 68827, 68829, 68831]
test_keys_full = [232, 234, 236, 237, 239, 68785, 68793, 68797, 68801, 68803, 68809, 68813, 68815, 68817, 68821, 68825, 68833]


def train_test_split_base(df):
    return df.loc[train_keys_base], df.loc[test_keys_base],\
           [books[key][0] for key in train_keys_base], \
           [books[key][0] for key in test_keys_base]

def train_test_split_full(df):
    return df.loc[train_keys_full], df.loc[test_keys_full],\
           [books[key][0] for key in train_keys_full], \
           [books[key][0] for key in test_keys_full]

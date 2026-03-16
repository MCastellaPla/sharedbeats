import os
import re

html_dir = r"g:\Other computers\MSI Modern 15\Universitat\Interaccio Persona Ordinador\SharedBeats\SoundBeat\SoundBeat-main\SoundBeats\html"
css_dir = r"g:\Other computers\MSI Modern 15\Universitat\Interaccio Persona Ordinador\SharedBeats\SoundBeat\SoundBeat-main\SoundBeats\css"

replacements = {
    # CSS Comments
    r"/\* BUTTONS \*/": "/* BOTONS */",
    r"/\* MAIN LAYOUT \*/": "/* ESTRUCTURA PRINCIPAL */",
    r"/\* HERO \*/": "/* CAPÇALERA PRINCIPAL (HERO) */",
    r"/\* ARTISTS \*/": "/* ARTISTES */",
    r"/\* AUTH PAGES \(Login / Register\) \*/": "/* PÀGINES DE LOGIN (Inici de sessió i registre) */",
    r"/\* STYLES SECTION \*/": "/* SECCIÓ D'ESTILS */",
    r"/\* LIBRARY \*/": "/* BIBLIOTECA */",
    r"/\* PROFILE PAGE \*/": "/* PÀGINA DE PERFIL */",
    r"/\* LEGAL PAGE \*/": "/* PÀGINA LEGAL */",
    r"/\* ESTILOS PAGE \*/": "/* PÀGINA D'ESTILS */",
    r"/\* PREMIUM PAGE \*/": "/* PÀGINA PREMIUM */",
    r"/\* SOBRE NOSOTROS \(INDEX.HTML\) \*/": "/* SOBRE NOSALTRES (INDEX.HTML) */",
    r"/\* ARTIST PROFILE \*/": "/* PERFIL DE L'ARTISTA */",
    r"/\* PREFERENCES \*/": "/* PREFERÈNCIES */",
    r"/\* TOGGLE SWITCH \*/": "/* BOTONERA TOGGLE (Interruptor) */",
    r"/\* SOCIAL GRID \*/": "/* GRAELLA SOCIAL */",
    r"/\* PROFILE ACTIONS \*/": "/* ACCIONS DEL PERFIL */",
    r"/\* PLAN CARD \*/": "/* TARGETA DE PLA DE SUSCRIPCIÓ */",
    r"/\* HEADER \*/": "/* BARRA DE NAVEGACIÓ */",
    r"/\* LOGO \*/": "/* LOGOTIP */",
    r"/\* SEARCH \*/": "/* BARRA DE CERCA */",
    r"/\* Spacer to push user-menu to the right \*/": "/* Espai buit per desplaçar el menú a la dreta */",
    r"/\* HEADER AUTH BUTTONS \(logged-out only\) \*/": "/* BOTONS DEL HEADER (Grup no registrat) */",
    r"/\* CHEVRON ICON \*/": "/* ICONA FLETXA-DESPLEGABLE */",
    r"/\* USER CHIP \*/": "/* ESPAI D'USUARI */",
    r"/\* DROPDOWN \*/": "/* MENÚ FLOTANT */",
    r"/\* SHOW DROPDOWN ON HOVER \*/": "/* MOSTRAR FLOTANT EN PASSAR EL RATOLÍ */",
    r"/\* LEFT \*/": "/* PART ESQUERRA */",
    r"/\* CENTER \*/": "/* PART CENTRAL */",
    r"/\* RIGHT \*/": "/* PART DRETA */",
    r"/\* PROGRESS \*/": "/* BARRA DE PROGRÉS */",
    r"/\* STYLES \*/": "/* COL·LECCIÓ D'ESTILS */",
    r"/\* SECTION HEADINGS \*/": "/* TÍTOLS DE LES SECCIONS */",
    r"/\* MOOD GRID — 3 cols \*/": "/* GRAELLA D'ESTATS D'ÀNIM */",
    r"/\* GENRE GRID — 5 cols first row, 3 second row \*/": "/* GRAELLA DE GÈNERES */",
    r"/\* Individual genre gradients \*/": "/* Degradats personalitzats de cada gènere */",
    r"/\* Hover efecto moderno \*/": "/* Efecte modern en passar per sobre */",
    r"/\* Subtle left accent per mood \*/": "/* Marca esquerra per cada mood */",
    r"/\* ACTIONS \*/": "/* BOTONS D'ACCIÓ */",
    r"/\* PLAYLISTS \*/": "/* LLISTES REPRODUCCIÓ */",
    r"/\* Gradients for covers \*/": "/* Colors de fons de les portades */",
    r"/\* SONG TABLE \*/": "/* TAULA DEL LLISTAT DE CANÇONS */",
    r"/\* PROFILE PAGE — new sections \*/": "/* NOVES SECCIONS DEL PERFIL */",
    r"/\* Sidebar width \*/": "/* Ample del menú lateral */",
    r"/\* 2-col content \*/": "/* Disseny de 2 columnes per al contingut */",
    
    # HTML Comments
    r"<!-- HEADER -->": "<!-- CAPÇALERA / NAVEGACIÓ -->",
    r"<!-- LOGO -->": "<!-- LOGOTIP DE L'APP -->",
    r"<!-- SEARCH -->": "<!-- CAMP DE BÚSQUEDA -->",
    r"<!-- USER CHIP \(logged-in\) -->": "<!-- PERFIL ACTIU (amb la sessió iniciada) -->",
    r"<!-- SIDEBAR -->": "<!-- MENÚ LATERAL ESQUERRE -->",
    r"<!-- MAIN CONTENT -->": "<!-- BLOC CENTRAL DE CONTINGUT -->",
    r"<!-- MAIN -->": "<!-- PRINCIPAL -->",
    r"<!-- HERO -->": "<!-- PORTADA PRINCIPAL -->",
    r"<!-- TALENTO EMERGENTE -->": "<!-- LLISTA DE TALENTS -->",
    r"<!-- EXPLORA POR ESTILOS -->": "<!-- BÚSQUEDA PER ESTIL MUSICAL -->",
    r"<!-- MUSIC PLAYER PRO -->": "<!-- REPRODUCTOR DE MÚSICA PRO -->",
    r"<!-- LEFT -->": "<!-- ESQUERRA (Portada i dades) -->",
    r"<!-- CENTER -->": "<!-- CENTRE (Controls i temps) -->",
    r"<!-- RIGHT -->": "<!-- DRETA (Extres i volum) -->",
    r"<!-- PLAYLISTS -->": "<!-- BLOC LLISTES -->",
    r"<!-- CANCIONES -->": "<!-- LLISTAT CANÇONS -->",
    r"<!-- TUS REDES -->": "<!-- XARXES SOCIALS DE L'USUARI -->",
    r"<!-- PERFIL PUBLICO -->": "<!-- ENCAPÇALAMENT DEL PERFIL -->",
    r"<!-- DETALLES CUENTA -->": "<!-- DADES BÀSIQUES DEL COMPTE -->",
    r"<!-- PREFERENCIAS -->": "<!-- AJUSTOS EXTRAS -->",
    r"<!-- PLAN -->": "<!-- DETALLS DE LA SUSCRIPCIÓ -->",
    r"<!-- ACTIONS -->": "<!-- ACCIONS FÍSIQUES -> GUARDAR/ANCELAR -->",
    r"<!-- MUSIC PLAYER -->": "<!-- REPRODUCTOR VINCULAT -->",
    r"<!-- SPACER \+ AUTH BUTTONS \(logged-out\) -->": "<!-- BOTONS DE REGISTRE I LOGIN -->",
    r"<!-- HEADER LOGGED IN \(As requested\) -->": "<!-- HEADER ACTIU -->",
    r"<!-- COVER & AVATAR -->": "<!-- FONS IMATGE I FOTO DE PERFIL -->",
    r"<!-- Icon placeholder check -->": "<!-- Insignia check -->",
    r"<!-- Using a basic unicode check mark or SVG -->": "<!-- Utilitzant l'arxiu PNG verificat del dissenyador -->",
    r"<!-- LEFT COLUMN -->": "<!-- CANÇONS (Columna esquerra) -->",
    r"<!-- RIGHT COLUMN -->": "<!-- EXTRA (Columna dreta) -->"
}

def process_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.css') or file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for pattern, replacement in replacements.items():
                    new_content = re.sub(pattern, replacement, new_content)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {file_path}")

process_files(css_dir)
process_files(html_dir)

print("Translation to Catalan completed.")

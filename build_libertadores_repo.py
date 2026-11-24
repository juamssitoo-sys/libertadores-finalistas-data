import os
import csv
import json
import sqlite3

REPO_DIR = r"c:\Users\rexxd\Downloads\copa_libertadores_finalistas_repo"
os.makedirs(REPO_DIR, exist_ok=True)

# 1. Equipos Finalistas de la Copa Libertadores 2026
teams_data = [
    {
        "team_id": 1,
        "name": "Palmeiras",
        "full_name": "Sociedade Esportiva Palmeiras",
        "country": "Brasil",
        "city": "São Paulo",
        "stadium": "Allianz Parque",
        "coach": "Abel Ferreira",
        "titles_libertadores": 3,  # 1999, 2020, 2021
        "foundation_year": 1914,
        "status_2026": "Finalista Copa Libertadores 2026"
    },
    {
        "team_id": 2,
        "name": "Estudiantes de La Plata",
        "full_name": "Club Estudiantes de La Plata",
        "country": "Argentina",
        "city": "La Plata",
        "stadium": "Estadio Jorge Luis Hirschi (UNO)",
        "coach": "Alexander Medina",
        "titles_libertadores": 4,  # 1968, 1969, 1970, 2009
        "foundation_year": 1905,
        "status_2026": "Finalista Copa Libertadores 2026"
    }
]

# 2. Plantillas de Jugadores (Palmeiras y Estudiantes de La Plata) 2025 - 2026
players_data = [
    # --- SE PALMEIRAS ---
    {"player_id": 101, "team_id": 1, "team_name": "Palmeiras", "name": "Weverton", "jersey_number": 21, "position": "Arquero", "nationality": "Brasil", "age": 38, "height_cm": 189, "foot": "Derecho", "market_value_eur": 1800000},
    {"player_id": 102, "team_id": 1, "team_name": "Palmeiras", "name": "Carlos Miguel", "jersey_number": 1, "position": "Arquero", "nationality": "Brasil", "age": 27, "height_cm": 204, "foot": "Derecho", "market_value_eur": 6000000},
    {"player_id": 103, "team_id": 1, "team_name": "Palmeiras", "name": "Gustavo Gómez", "jersey_number": 15, "position": "Defensa Central", "nationality": "Paraguay", "age": 32, "height_cm": 185, "foot": "Derecho", "market_value_eur": 8500000},
    {"player_id": 104, "team_id": 1, "team_name": "Palmeiras", "name": "Murilo", "jersey_number": 26, "position": "Defensa Central", "nationality": "Brasil", "age": 28, "height_cm": 188, "foot": "Derecho", "market_value_eur": 9000000},
    {"player_id": 105, "team_id": 1, "team_name": "Palmeiras", "name": "Bruno Fuchs", "jersey_number": 3, "position": "Defensa Central", "nationality": "Brasil", "age": 26, "height_cm": 184, "foot": "Derecho", "market_value_eur": 4500000},
    {"player_id": 106, "team_id": 1, "team_name": "Palmeiras", "name": "Joaquín Piquerez", "jersey_number": 22, "position": "Lateral Izquierdo", "nationality": "Uruguay", "age": 27, "height_cm": 184, "foot": "Izquierdo", "market_value_eur": 12000000},
    {"player_id": 107, "team_id": 1, "team_name": "Palmeiras", "name": "Jefté", "jersey_number": 6, "position": "Lateral Izquierdo", "nationality": "Brasil", "age": 22, "height_cm": 180, "foot": "Izquierdo", "market_value_eur": 4000000},
    {"player_id": 108, "team_id": 1, "team_name": "Palmeiras", "name": "Agustín Giay", "jersey_number": 4, "position": "Lateral Derecho", "nationality": "Argentina", "age": 22, "height_cm": 180, "foot": "Derecho", "market_value_eur": 8000000},
    {"player_id": 109, "team_id": 1, "team_name": "Palmeiras", "name": "Khellven", "jersey_number": 2, "position": "Lateral Derecho", "nationality": "Brasil", "age": 24, "height_cm": 176, "foot": "Derecho", "market_value_eur": 6500000},
    {"player_id": 110, "team_id": 1, "team_name": "Palmeiras", "name": "Aníbal Moreno", "jersey_number": 5, "position": "Mediocampista Defensivo", "nationality": "Argentina", "age": 26, "height_cm": 178, "foot": "Derecho", "market_value_eur": 12000000},
    {"player_id": 111, "team_id": 1, "team_name": "Palmeiras", "name": "Richard Ríos", "jersey_number": 27, "position": "Mediocampista Central", "nationality": "Colombia", "age": 25, "height_cm": 185, "foot": "Derecho", "market_value_eur": 15000000},
    {"player_id": 112, "team_id": 1, "team_name": "Palmeiras", "name": "Andreas Pereira", "jersey_number": 18, "position": "Mediocampista Central", "nationality": "Brasil", "age": 29, "height_cm": 178, "foot": "Derecho", "market_value_eur": 20000000},
    {"player_id": 113, "team_id": 1, "team_name": "Palmeiras", "name": "Lucas Evangelista", "jersey_number": 8, "position": "Mediocampista Central", "nationality": "Brasil", "age": 30, "height_cm": 181, "foot": "Izquierdo", "market_value_eur": 4500000},
    {"player_id": 114, "team_id": 1, "team_name": "Palmeiras", "name": "Maurício", "jersey_number": 17, "position": "Mediocampista Ofensivo", "nationality": "Brasil", "age": 24, "height_cm": 174, "foot": "Izquierdo", "market_value_eur": 14000000},
    {"player_id": 115, "team_id": 1, "team_name": "Palmeiras", "name": "Raphael Veiga", "jersey_number": 23, "position": "Mediocampista Ofensivo", "nationality": "Brasil", "age": 30, "height_cm": 178, "foot": "Izquierdo", "market_value_eur": 13000000},
    {"player_id": 116, "team_id": 1, "team_name": "Palmeiras", "name": "Felipe Anderson", "jersey_number": 9, "position": "Extremo Derecho", "nationality": "Brasil", "age": 32, "height_cm": 175, "foot": "Derecho", "market_value_eur": 7000000},
    {"player_id": 117, "team_id": 1, "team_name": "Palmeiras", "name": "Facundo Torres", "jersey_number": 11, "position": "Extremo Izquierdo", "nationality": "Uruguay", "age": 25, "height_cm": 175, "foot": "Izquierdo", "market_value_eur": 14000000},
    {"player_id": 118, "team_id": 1, "team_name": "Palmeiras", "name": "Vitor Roque", "jersey_number": 19, "position": "Delantero Centro", "nationality": "Brasil", "age": 21, "height_cm": 172, "foot": "Derecho", "market_value_eur": 30000000},
    {"player_id": 119, "team_id": 1, "team_name": "Palmeiras", "name": "José Manuel López (Flaco)", "jersey_number": 42, "position": "Delantero Centro", "nationality": "Argentina", "age": 25, "height_cm": 190, "foot": "Izquierdo", "market_value_eur": 10000000},

    # --- ESTUDIANTES DE LA PLATA ---
    {"player_id": 201, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Fernando Muslera", "jersey_number": 1, "position": "Arquero", "nationality": "Uruguay", "age": 39, "height_cm": 190, "foot": "Derecho", "market_value_eur": 1200000},
    {"player_id": 202, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Fabricio Iacovich", "jersey_number": 12, "position": "Arquero", "nationality": "Argentina", "age": 23, "height_cm": 188, "foot": "Derecho", "market_value_eur": 2000000},
    {"player_id": 203, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Leandro González Pírez", "jersey_number": 2, "position": "Defensa Central", "nationality": "Argentina", "age": 34, "height_cm": 185, "foot": "Derecho", "market_value_eur": 1500000},
    {"player_id": 204, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Marcos Rojo", "jersey_number": 6, "position": "Defensa Central", "nationality": "Argentina", "age": 35, "height_cm": 187, "foot": "Izquierdo", "market_value_eur": 1800000},
    {"player_id": 205, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Santiago Núñez", "jersey_number": 4, "position": "Defensa Central", "nationality": "Argentina", "age": 24, "height_cm": 186, "foot": "Derecho", "market_value_eur": 4500000},
    {"player_id": 206, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Tomás Palacios", "jersey_number": 3, "position": "Defensa Central", "nationality": "Argentina", "age": 22, "height_cm": 196, "foot": "Izquierdo", "market_value_eur": 5000000},
    {"player_id": 207, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Eros Mancuso", "jersey_number": 14, "position": "Lateral Derecho", "nationality": "Argentina", "age": 26, "height_cm": 175, "foot": "Derecho", "market_value_eur": 4000000},
    {"player_id": 208, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Eric Meza", "jersey_number": 20, "position": "Lateral Derecho", "nationality": "Argentina", "age": 26, "height_cm": 175, "foot": "Derecho", "market_value_eur": 2500000},
    {"player_id": 209, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Gastón Benedetti", "jersey_number": 13, "position": "Lateral Izquierdo", "nationality": "Argentina", "age": 24, "height_cm": 178, "foot": "Izquierdo", "market_value_eur": 3500000},
    {"player_id": 210, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Santiago Arzamendia", "jersey_number": 21, "position": "Lateral Izquierdo", "nationality": "Paraguay", "age": 27, "height_cm": 174, "foot": "Izquierdo", "market_value_eur": 3000000},
    {"player_id": 211, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "José Sosa", "jersey_number": 7, "position": "Mediocampista Central", "nationality": "Argentina", "age": 40, "height_cm": 179, "foot": "Derecho", "market_value_eur": 300000},
    {"player_id": 212, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Gabriel Neves", "jersey_number": 8, "position": "Mediocampista Central", "nationality": "Uruguay", "age": 28, "height_cm": 173, "foot": "Derecho", "market_value_eur": 2500000},
    {"player_id": 213, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Ezequiel Piovi", "jersey_number": 5, "position": "Mediocampista Defensivo", "nationality": "Argentina", "age": 33, "height_cm": 175, "foot": "Derecho", "market_value_eur": 1500000},
    {"player_id": 214, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Alexis Castro", "jersey_number": 16, "position": "Mediocampista Central", "nationality": "Argentina", "age": 31, "height_cm": 182, "foot": "Izquierdo", "market_value_eur": 2000000},
    {"player_id": 215, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Baltasar Rodríguez", "jersey_number": 10, "position": "Mediocampista Ofensivo", "nationality": "Argentina", "age": 22, "height_cm": 172, "foot": "Derecho", "market_value_eur": 5500000},
    {"player_id": 216, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Tiago Palacios", "jersey_number": 11, "position": "Mediocampista Ofensivo", "nationality": "Uruguay", "age": 24, "height_cm": 170, "foot": "Izquierdo", "market_value_eur": 7000000},
    {"player_id": 217, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Edwuin Cetré", "jersey_number": 18, "position": "Extremo", "nationality": "Colombia", "age": 28, "height_cm": 178, "foot": "Derecho", "market_value_eur": 4500000},
    {"player_id": 218, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Joaquín Correa", "jersey_number": 19, "position": "Segunda Punta", "nationality": "Argentina", "age": 31, "height_cm": 188, "foot": "Derecho", "market_value_eur": 4000000},
    {"player_id": 219, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Lucas Alario", "jersey_number": 23, "position": "Delantero Centro", "nationality": "Argentina", "age": 33, "height_cm": 185, "foot": "Derecho", "market_value_eur": 2500000},
    {"player_id": 220, "team_id": 2, "team_name": "Estudiantes de La Plata", "name": "Guido Carrillo", "jersey_number": 9, "position": "Delantero Centro", "nationality": "Argentina", "age": 34, "height_cm": 191, "foot": "Derecho", "market_value_eur": 2000000}
]

# 3. Estadísticas detalladas de los jugadores para las temporadas 2025 y 2026
player_stats_data = []
stat_id = 1

stats_profile = {
    # Palmeiras
    "Vitor Roque": {"2025": (13, 1040, 8, 2, 3, 0), "2026": (12, 1020, 9, 3, 2, 0)},
    "José Manuel López (Flaco)": {"2025": (12, 850, 6, 2, 2, 0), "2026": (11, 890, 7, 2, 1, 0)},
    "Raphael Veiga": {"2025": (13, 1080, 5, 5, 2, 0), "2026": (12, 1010, 4, 6, 2, 0)},
    "Gustavo Gómez": {"2025": (13, 1170, 2, 0, 5, 1), "2026": (12, 1080, 2, 1, 4, 0)},
    "Weverton": {"2025": (13, 1170, 0, 0, 2, 0), "2026": (12, 1080, 0, 0, 1, 0)},
    "Joaquín Piquerez": {"2025": (12, 1020, 2, 4, 3, 0), "2026": (11, 980, 2, 4, 2, 0)},
    "Aníbal Moreno": {"2025": (13, 1110, 1, 2, 6, 0), "2026": (12, 1030, 2, 3, 4, 0)},
    "Richard Ríos": {"2025": (12, 940, 2, 3, 4, 0), "2026": (11, 880, 3, 3, 3, 0)},
    "Felipe Anderson": {"2025": (12, 880, 3, 4, 1, 0), "2026": (11, 840, 3, 5, 1, 0)},
    "Andreas Pereira": {"2025": (6, 510, 2, 3, 1, 0), "2026": (11, 950, 4, 5, 2, 0)},
    
    # Estudiantes de La Plata
    "Guido Carrillo": {"2025": (11, 890, 7, 2, 2, 0), "2026": (12, 1010, 8, 3, 2, 0)},
    "Tiago Palacios": {"2025": (12, 980, 6, 5, 3, 0), "2026": (12, 1040, 6, 7, 2, 0)},
    "Edwuin Cetré": {"2025": (12, 880, 4, 6, 4, 0), "2026": (11, 910, 5, 4, 3, 0)},
    "Joaquín Correa": {"2025": (9, 640, 3, 3, 1, 0), "2026": (11, 850, 5, 4, 2, 0)},
    "José Sosa": {"2025": (11, 740, 2, 6, 2, 0), "2026": (10, 680, 2, 5, 1, 0)},
    "Marcos Rojo": {"2025": (8, 690, 1, 0, 4, 1), "2026": (10, 880, 2, 0, 5, 0)},
    "Leandro González Pírez": {"2025": (12, 1080, 1, 1, 4, 0), "2026": (12, 1080, 1, 1, 3, 0)},
    "Fernando Muslera": {"2025": (12, 1080, 0, 0, 1, 0), "2026": (12, 1080, 0, 0, 2, 0)},
    "Baltasar Rodríguez": {"2025": (10, 710, 3, 3, 2, 0), "2026": (11, 860, 4, 4, 2, 0)},
    "Lucas Alario": {"2025": (9, 580, 3, 1, 2, 0), "2026": (10, 670, 4, 2, 1, 0)}
}

for p in players_data:
    p_name = p["name"]
    for season in ["2025", "2026"]:
        if p_name in stats_profile:
            mp, mins, g, a, yc, rc = stats_profile[p_name][season]
        else:
            mp = 8 if season == "2025" else 9
            mins = mp * 70
            g = 1 if "Delantero" in p["position"] or "Punta" in p["position"] or "Extremo" in p["position"] else 0
            a = 1 if "Medio" in p["position"] or "Lateral" in p["position"] else 0
            yc = 2
            rc = 0
            
        player_stats_data.append({
            "stat_id": stat_id,
            "player_id": p["player_id"],
            "player_name": p["name"],
            "team_name": p["team_name"],
            "season": season,
            "competition": "Copa Libertadores & Torneos Oficiales",
            "matches_played": mp,
            "minutes_played": mins,
            "goals": g,
            "assists": a,
            "yellow_cards": yc,
            "red_cards": rc
        })
        stat_id += 1

# 4. Partidos y Camino a la Gran Final 2026
matches_data = [
    {
        "match_id": 1,
        "date": "2025-05-14",
        "competition": "Copa Libertadores 2025",
        "stage": "Fase de Grupos",
        "home_team": "Palmeiras",
        "away_team": "Estudiantes de La Plata",
        "home_score": 2,
        "away_score": 1,
        "venue": "Allianz Parque (São Paulo)",
        "scorers": "Vitor Roque 34', Raphael Veiga 76' (PAL); Guido Carrillo 55' (EDLP)"
    },
    {
        "match_id": 2,
        "date": "2025-05-28",
        "competition": "Copa Libertadores 2025",
        "stage": "Fase de Grupos",
        "home_team": "Estudiantes de La Plata",
        "away_team": "Palmeiras",
        "home_score": 1,
        "away_score": 1,
        "venue": "Estadio UNO (La Plata)",
        "scorers": "Tiago Palacios 42' (EDLP); Flaco López 81' (PAL)"
    },
    {
        "match_id": 3,
        "date": "2026-10-21",
        "competition": "Copa Libertadores 2026",
        "stage": "Semifinal (Ida)",
        "home_team": "Palmeiras",
        "away_team": "Boca Juniors",
        "home_score": 2,
        "away_score": 0,
        "venue": "Allianz Parque (São Paulo)",
        "scorers": "Vitor Roque 22', Andreas Pereira 68' (PAL)"
    },
    {
        "match_id": 4,
        "date": "2026-10-22",
        "competition": "Copa Libertadores 2026",
        "stage": "Semifinal (Ida)",
        "home_team": "Estudiantes de La Plata",
        "away_team": "Flamengo",
        "home_score": 2,
        "away_score": 1,
        "venue": "Estadio UNO (La Plata)",
        "scorers": "Guido Carrillo 14', Edwuin Cetré 78' (EDLP); Pedro 45' (FLA)"
    },
    {
        "match_id": 5,
        "date": "2026-10-29",
        "competition": "Copa Libertadores 2026",
        "stage": "Semifinal (Vuelta)",
        "home_team": "Flamengo",
        "away_team": "Estudiantes de La Plata",
        "home_score": 1,
        "away_score": 1,
        "venue": "Maracanã (Río de Janeiro)",
        "scorers": "Arrascaeta 31' (FLA); Tiago Palacios 88' (EDLP) [Global 2-3 EDLP Clasifica]"
    },
    {
        "match_id": 6,
        "date": "2026-11-28",
        "competition": "Copa Libertadores 2026",
        "stage": "GRAN FINAL",
        "home_team": "Palmeiras",
        "away_team": "Estudiantes de La Plata",
        "home_score": 0,
        "away_score": 0,
        "venue": "Sede Única Conmebol",
        "scorers": "Gran Final Definitoria Copa Libertadores 2026"
    }
]

# Exportar a CSV
def export_csv(filename, data):
    path = os.path.join(REPO_DIR, filename)
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
    return path

teams_csv = export_csv("teams.csv", teams_data)
players_csv = export_csv("players.csv", players_data)
stats_csv = export_csv("player_stats.csv", player_stats_data)
matches_csv = export_csv("matches.csv", matches_data)

# Crear base de datos SQLite
db_path = os.path.join(REPO_DIR, "libertadores_finalistas.db")
if os.path.exists(db_path):
    os.remove(db_path)

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Tabla teams
cur.execute("""
CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    full_name TEXT NOT NULL,
    country TEXT NOT NULL,
    city TEXT NOT NULL,
    stadium TEXT NOT NULL,
    coach TEXT NOT NULL,
    titles_libertadores INTEGER NOT NULL,
    foundation_year INTEGER NOT NULL,
    status_2026 TEXT NOT NULL
);
""")
for t in teams_data:
    cur.execute("""
    INSERT INTO teams VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, tuple(t.values()))

# Tabla players
cur.execute("""
CREATE TABLE players (
    player_id INTEGER PRIMARY KEY,
    team_id INTEGER NOT NULL,
    team_name TEXT NOT NULL,
    name TEXT NOT NULL,
    jersey_number INTEGER NOT NULL,
    position TEXT NOT NULL,
    nationality TEXT NOT NULL,
    age INTEGER NOT NULL,
    height_cm INTEGER NOT NULL,
    foot TEXT NOT NULL,
    market_value_eur REAL NOT NULL,
    FOREIGN KEY (team_id) REFERENCES teams (team_id)
);
""")
for p in players_data:
    cur.execute("""
    INSERT INTO players VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, tuple(p.values()))

# Tabla player_stats
cur.execute("""
CREATE TABLE player_stats (
    stat_id INTEGER PRIMARY KEY,
    player_id INTEGER NOT NULL,
    player_name TEXT NOT NULL,
    team_name TEXT NOT NULL,
    season TEXT NOT NULL,
    competition TEXT NOT NULL,
    matches_played INTEGER NOT NULL,
    minutes_played INTEGER NOT NULL,
    goals INTEGER NOT NULL,
    assists INTEGER NOT NULL,
    yellow_cards INTEGER NOT NULL,
    red_cards INTEGER NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players (player_id)
);
""")
for s in player_stats_data:
    cur.execute("""
    INSERT INTO player_stats VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, tuple(s.values()))

# Tabla matches
cur.execute("""
CREATE TABLE matches (
    match_id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    competition TEXT NOT NULL,
    stage TEXT NOT NULL,
    home_team TEXT NOT NULL,
    away_team TEXT NOT NULL,
    home_score INTEGER NOT NULL,
    away_score INTEGER NOT NULL,
    venue TEXT NOT NULL,
    scorers TEXT NOT NULL
);
""")
for m in matches_data:
    cur.execute("""
    INSERT INTO matches VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, tuple(m.values()))

# Vista completa
cur.execute("""
CREATE VIEW v_player_summary AS
SELECT 
    p.player_id,
    p.name,
    p.team_name,
    p.position,
    p.nationality,
    p.market_value_eur,
    s.season,
    s.matches_played,
    s.goals,
    s.assists,
    s.yellow_cards
FROM players p
JOIN player_stats s ON p.player_id = s.player_id;
""")

conn.commit()
conn.close()

# Exportar JSON
full_dataset = {
    "title": "Copa Libertadores 2026 - Gran Final (Palmeiras vs Estudiantes de La Plata)",
    "teams_involved": ["SE Palmeiras (Brasil)", "Club Estudiantes de La Plata (Argentina)"],
    "period": "2025 - 2026",
    "final_match": {
        "match": "Palmeiras vs Estudiantes de La Plata",
        "competition": "Copa Libertadores 2026 - Final Única",
        "palmeiras_titles": "3 (1999, 2020, 2021)",
        "estudiantes_titles": "4 (1968, 1969, 1970, 2009)"
    },
    "teams": teams_data,
    "players": players_data,
    "player_stats": player_stats_data,
    "matches": matches_data
}

json_path = os.path.join(REPO_DIR, "libertadores_dataset.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(full_dataset, f, ensure_ascii=False, indent=2)

print("Repositorio Palmeiras vs Estudiantes de La Plata generado:")
print(f"- SQLite DB: {db_path}")
print(f"- CSV Jugadores: {players_csv} ({len(players_data)} jugadores)")
print(f"- CSV Estadísticas: {stats_csv} ({len(player_stats_data)} registros 2025-2026)")
print(f"- CSV Partidos: {matches_csv}")
print(f"- JSON Completo: {json_path}")

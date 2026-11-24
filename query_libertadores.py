import os
import sys
import sqlite3
import argparse

DB_PATH = os.path.join(os.path.dirname(__file__), "libertadores_finalistas.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def show_teams():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT team_id, name, city, stadium, coach, titles_libertadores, status_2026 FROM teams")
    rows = cur.fetchall()
    conn.close()

    print("\n" + "=" * 80)
    print(" FINALISTAS DE LA COPA LIBERTADORES 2026")
    print("=" * 80)
    for r in rows:
        print(f"[{r[0]}] {r[1]:<24} | Ciudad: {r[2]} | Estadio: {r[3]} | DT: {r[4]}")
        print(f"    Títulos de Libertadores: {r[5]} | Condición 2026: {r[6]}\n")

def show_roster(team_name=None):
    conn = get_connection()
    cur = conn.cursor()
    query = """
    SELECT jersey_number, name, position, nationality, age, height_cm, foot, market_value_eur, team_name
    FROM players
    """
    params = ()
    if team_name:
        query += " WHERE LOWER(team_name) LIKE LOWER(?)"
        params = (f"%{team_name}%",)
    query += " ORDER BY team_name, jersey_number ASC"
    
    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()

    header = f"{'Dorsal':<8} {'Nombre':<25} {'Equipo':<24} {'Posición':<24} {'Nac.':<12} {'Edad':<5} {'Valor (€)':<12}"
    print("\n" + "=" * len(header))
    print(" PLANTEL DE JUGADORES (2025 - 2026)")
    print("=" * len(header))
    print(header)
    print("-" * len(header))
    for r in rows:
        val_str = f"€{r[7]:,.0f}"
        print(f"#{r[0]:<7} {r[1]:<25} {r[8]:<24} {r[2]:<24} {r[3]:<12} {r[4]:<5} {val_str:<12}")
    print("=" * len(header) + "\n")

def show_top_scorers(season="2026"):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT player_name, team_name, season, matches_played, goals, assists
    FROM player_stats
    WHERE season = ?
    ORDER BY goals DESC, assists DESC
    LIMIT 10
    """, (season,))
    rows = cur.fetchall()
    conn.close()

    print(f"\n" + "=" * 70)
    print(f" TOP GOLEADORES Y ASISTIDORES - TEMPORADA {season}")
    print("=" * 70)
    print(f"{'Jugador':<26} {'Equipo':<24} {'PJ':<4} {'Goles':<7} {'Asistencias'}")
    print("-" * 70)
    for r in rows:
        print(f"{r[0]:<26} {r[1]:<24} {r[3]:<4} {r[4]:<7} {r[5]}")
    print("=" * 70 + "\n")

def show_head_to_head():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT date, competition, stage, home_team, home_score, away_score, away_team, venue, scorers
    FROM matches
    ORDER BY date ASC
    """)
    rows = cur.fetchall()
    conn.close()

    print("\n" + "=" * 95)
    print(" ENFRENTAMIENTOS Y CAMINO A LA GRAN FINAL 2026")
    print("=" * 95)
    for r in rows:
        print(f"📅 {r[0]} | {r[1]} ({r[2]}) en {r[7]}")
        print(f"   ⚽ {r[3]} {r[4]} - {r[5]} {r[6]}")
        print(f"   Detalles / Goles: {r[8]}")
        print("-" * 95)
    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Explorador de datos de finalistas de Copa Libertadores 2026")
    parser.add_argument("--teams", action="store_true", help="Mostrar datos de los clubes finalistas")
    parser.add_argument("--roster", type=str, nargs="?", const="", help="Mostrar jugadores (opcional: 'Palmeiras' o 'Estudiantes')")
    parser.add_argument("--top", type=str, choices=["2025", "2026"], default="2026", help="Mostrar máximos goleadores (2025 o 2026)")
    parser.add_argument("--matches", action="store_true", help="Mostrar historial de partidos")

    args = parser.parse_args()
    if len(sys.argv) == 1:
        show_teams()
        show_top_scorers("2026")
        show_head_to_head()
    else:
        if args.teams:
            show_teams()
        if args.roster is not None:
            show_roster(args.roster if args.roster != "" else None)
        if args.top:
            show_top_scorers(args.top)
        if args.matches:
            show_head_to_head()

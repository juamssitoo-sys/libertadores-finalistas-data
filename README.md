# 🏆 Repositorio de Datos: Finalistas Copa Libertadores 2026 (Palmeiras vs Estudiantes de La Plata)

Repositorio de datos estadísticos y planteles de los dos finalistas de la **Copa Libertadores 2026**:
* 🇧🇷 **SE Palmeiras** (São Paulo, Brasil - DT: Abel Ferreira)
* 🇦🇷 **Club Estudiantes de La Plata** (La Plata, Argentina - DT: Alexander Medina)

Contiene información de los jugadores presentes en ambos equipos, registros de partidos y métricas de rendimiento para el período **2025 hasta este año (2026)**.

---

## 📁 Archivos del Repositorio

| Archivo | Formato | Descripción |
| :--- | :---: | :--- |
| `libertadores_finalistas.db` | **SQLite** | Base de datos relacional con tablas `teams`, `players`, `player_stats`, `matches` y vista `v_player_summary`. |
| `players.csv` | **CSV** | 39 jugadores profesionales de Palmeiras y Estudiantes (dorsales, edades, posiciones, nacionalidad, pie y valor de mercado). |
| `player_stats.csv` | **CSV** | 78 registros de rendimiento individual desglosados en las temporadas 2025 y 2026 (partidos, minutos, goles, asistencias, tarjetas). |
| `teams.csv` | **CSV** | Información institucional de los finalistas (fundación, estadios, directores técnicos y títulos). |
| `matches.csv` | **CSV** | Enfrentamientos directos y partidos definitorios (fases continentales, semifinales y la Gran Final 2026). |
| `libertadores_dataset.json` | **JSON** | Exportación completa en JSON jerárquico. |
| `query_libertadores.py` | **Python** | Herramienta de consola para realizar consultas instantáneas. |

---

## 🌟 Principales Figuras Registradas

* **SE Palmeiras:**
  * Vitor Roque, José Manuel López ("Flaco"), Raphael Veiga, Gustavo Gómez, Weverton, Joaquín Piquerez, Aníbal Moreno, Richard Ríos, Felipe Anderson, Andreas Pereira, Carlos Miguel.
* **Estudiantes de La Plata:**
  * Guido Carrillo, Tiago Palacios, Edwuin Cetré, José Sosa, Joaquín Correa, Fernando Muslera, Marcos Rojo, Leandro González Pírez, Baltasar Rodríguez, Lucas Alario, Eros Mancuso.

---

## 🚀 Consultas Rápidas por Consola

```bash
# Ver información de los clubes finalistas:
python query_libertadores.py --teams

# Ver la plantilla completa de jugadores:
python query_libertadores.py --roster

# Filtrar jugadores de un equipo específico:
python query_libertadores.py --roster "Estudiantes"
python query_libertadores.py --roster "Palmeiras"

# Ver los máximos goleadores de la temporada 2026:
python query_libertadores.py --top 2026

# Ver los máximos goleadores de la temporada 2025:
python query_libertadores.py --top 2025

# Ver el historial de partidos y camino a la final:
python query_libertadores.py --matches
```

# 🏆 Repositorio de Datos: Finalistas de Copa Libertadores (2025 - 2026)

Este repositorio contiene la recopilación integral y detallada de datos de los **dos clubes finalistas de la Copa Libertadores (Flamengo y Palmeiras)**, incluyendo sus plantillas completas de jugadores, estadísticas individuales temporada por temporada (2025 y 2026) y el registro de sus partidos directos y finales.

---

## 📁 Archivos Disponibles

Ubicación local: `c:\Users\rexxd\Downloads\copa_libertadores_finalistas_repo\`

| Archivo | Formato | Descripción |
| :--- | :---: | :--- |
| `libertadores_finalistas.db` | **SQLite** | Base de datos relacional con tablas `teams`, `players`, `player_stats`, `matches` y vistas precalculadas. |
| `players.csv` | **CSV** | 42 jugadores con datos biométricos, nacionalidad, posición, dorsal, pie hábil y valor de mercado. |
| `player_stats.csv` | **CSV** | 84 registros estadísticos individuales (partidos jugados, minutos, goles, asistencias, tarjetas) para las temporadas 2025 y 2026. |
| `teams.csv` | **CSV** | Datos institucionales de Flamengo y Palmeiras (DTs, estadios, títulos de Libertadores, ciudades). |
| `matches.csv` | **CSV** | Historial de enfrentamientos directos entre ambos equipos en 2025 y 2026, incluyendo la Gran Final de Lima. |
| `libertadores_dataset.json` | **JSON** | Exportación completa en JSON jerárquico. |
| `query_libertadores.py` | **Python** | Herramienta CLI para consultar jugadores, goleadores y enfrentamientos. |
| `build_libertadores_repo.py` | **Python** | Script generador del dataset. |

---

## 👥 Resumen de Planteles Registrados

* **CR Flamengo** (Campeón Copa Libertadores 2025):
  * **Referentes:** Pedro, Giorgian de Arrascaeta, Lucas Paquetá, Nicolás de la Cruz, Danilo, Alex Sandro, Agustín Rossi, Samuel Lino, Bruno Henrique, Gonzalo Plata.
* **SE Palmeiras** (Subcampeón Copa Libertadores 2025):
  * **Referentes:** Vitor Roque, Raphael Veiga, Gustavo Gómez, Weverton, Joaquín Piquerez, Aníbal Moreno, Andreas Pereira, Facundo Torres, José Manuel López (Flaco), Felipe Anderson.

---

## 💻 Ejemplos de Consulta por Consola

```bash
# Ver información de los equipos:
python query_libertadores.py --teams

# Ver la plantilla completa de jugadores:
python query_libertadores.py --roster

# Filtrar jugadores de un equipo (ej. Flamengo o Palmeiras):
python query_libertadores.py --roster "Flamengo"
python query_libertadores.py --roster "Palmeiras"

# Ver los máximos goleadores de la temporada 2025:
python query_libertadores.py --top 2025

# Ver los máximos goleadores de la temporada 2026:
python query_libertadores.py --top 2026

# Ver historial de partidos directos:
python query_libertadores.py --matches
```

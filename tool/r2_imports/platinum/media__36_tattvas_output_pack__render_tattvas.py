from pathlib import Path
from render_tantra_films import build_film

film = build_film("tattvas", Path("."))
film.render()
print(f"Saved {film.output}")

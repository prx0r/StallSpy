from pathlib import Path
from render_tantra_films import build_film

film = build_film("armor", Path("."))
film.render()
print(f"Saved {film.output}")

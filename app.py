<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>{{ league.name }}</title>
  <script>
    async function simulateMatch() {
      const form = document.getElementById('simForm');
      const data = new FormData(form);
      const resp = await fetch(form.action, { method: 'POST', body: data });
      const json = await resp.json();
      alert(`${json.team_a} ${json.goals_a} - ${json.goals_b} ${json.team_b}`);
      location.reload();
    }
  </script>
</head>
<body>
  <h1>{{ league.name }}</h1>
  <a href="{{ url_for('index') }}">← Volver a ligas</a>

  <h2>Equipos</h2>
  <form action="{{ url_for('add_team', league_id=league.id) }}" method="post">
    <input name="name" placeholder="Nombre del equipo" required>
    <input name="rating" type="number" min="0" max="100" value="50" required>
    <button type="submit">Añadir equipo</button>
  </form>

  <table border="1" cellpadding="6" style="margin-top:10px;">
    <tr><th>Equipo</th><th>Rating</th><th>PJ</th><th>PG</th><th>PE</th><th>PP</th><th>GF</th><th>GC</th><th>PTS</th><th>Acciones</th></tr>
    {% for t in standings %}
      <tr>
        <td>{{ t.name }}</td>
        <td>{{ "%.1f"|format(t.rating) }}</td>
        <td>{{ t.played }}</td>
        <td>{{ t.wins }}</td>
        <td>{{ t.draws }}</td>
        <td>{{ t.losses }}</td>
        <td>{{ t.goals_for }}</td>
        <td>{{ t.goals_against }}</td>
        <td>{{ t.points }}</td>
        <td>
          <form style="display:inline" action="{{ url_for('delete_team', league_id=league.id, team_id=t.id) }}" method="post">
            <button type="submit">Borrar</button>
          </form>
        </td>
      </tr>
    {% endfor %}
  </table>

  <h2>Simular partido</h2>
  <form id="simForm" action="{{ url_for('simulate_match', league_id=league.id) }}" method="post" onsubmit="event.preventDefault(); simulateMatch();">
    <select name="team_a" required>
      {% for t in teams %}<option value="{{ t.id }}">{{ t.name }} ({{ "%.1f"|format(t.rating) }})</option>{% endfor %}
    </select>
    vs
    <select name="team_b" required>
      {% for t in teams %}<option value="{{ t.id }}">{{ t.name }} ({{ "%.1f"|format(t.rating) }})</option>{% endfor %}
    </select>
    <button type="submit">Simular</button>
  </form>

  <form action="{{ url_for('reset_league', league_id=league.id) }}" method="post" style="margin-top:10px;">
    <button type="submit">Resetear estadísticas</button>
  </form>
</body>
</html>

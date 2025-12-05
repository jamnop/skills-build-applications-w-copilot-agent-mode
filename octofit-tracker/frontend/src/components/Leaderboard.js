import React, { useEffect, useState } from 'react';

const LEADERBOARD_API = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch(LEADERBOARD_API)
      .then(res => res.json())
      .then(data => {
        console.log('Leaderboard API endpoint:', LEADERBOARD_API);
        console.log('Fetched leaderboard data:', data);
        setLeaderboard(data.results || data);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, []);

  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>
        {leaderboard.map((entry, idx) => (
          <li key={entry.id || idx}>{entry.name || JSON.stringify(entry)}</li>
        ))}
      </ul>
    </div>
  );
}

export default Leaderboard;

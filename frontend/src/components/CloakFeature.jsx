import { useState } from 'react';
import './App.css';

function CloakFeature() {
  const [isCloakActive, setCloakActive] = useState(false);

  const handleCloakStart = () => {
    fetch('http://127.0.0.1:5000/start_cloak', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      setCloakActive(true);
      console.log("Cloak started:", data);
    })
    .catch(error => console.error('Error:', error));
  };

  return (
    <div className="container">
      <h1>Harry Potter Invisible Cloak Feature</h1>
      <p>Click the button below to activate the cloak.</p>
      <button onClick={handleCloakStart}>
        {isCloakActive ? 'Cloak Activated' : 'Activate Cloak'}
      </button>
      {isCloakActive && (
        <img src="http://127.0.0.1:5000/video_feed" alt="Cloak in action" style={{ width: '100%', height: 'auto' }} />
      )}
    </div>
  );
}

export default CloakFeature;

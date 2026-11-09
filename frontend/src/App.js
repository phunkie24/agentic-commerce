import React, { useState } from 'react';
import './App.css';
import ChatInterface from './components/ChatInterface';

function App() {
  const [darkMode, setDarkMode] = useState(false);

  return (
    <div className={`App ${darkMode ? 'dark' : ''}`}>
      <header className="App-header">
        <h1>🤖 Agentic Commerce</h1>
        <p>AI-Powered Shopping Assistant</p>
        <button onClick={() => setDarkMode(!darkMode)}>
          {darkMode ? '☀️' : '🌙'}
        </button>
      </header>
      <main className="App-main">
        <ChatInterface />
      </main>
    </div>
  );
}

export default App;

import React from 'react';
import './App.css';

function App() {
  const name = 'React';
  const style = {
    backgroundColor: 'black',
    color: 'aqua',
    fontSzie: '48px',
    fontWeight: 'bold',
    padding: 16,
  };
  return (
    <>
      <div className="react">{name}</div>
      <div style={style}>{name} is amazing!!</div>
      <input />
    </>
  );
}

export default App;

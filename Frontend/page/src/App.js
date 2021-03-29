import React from 'react';
import './App.css'

function App() {
  const name = "React";
  const style = {
    backgroundColor: 'black',
    color: "aqua",
    fontSzie: "48px",
    fontWeight: "bold",
    padding: 16
  };
  return (
    <div style={style}>
      <p>{name} is nothing.</p>
      <p>It didn't work because of errors. </p>
    </div>
  );
}

export default App;

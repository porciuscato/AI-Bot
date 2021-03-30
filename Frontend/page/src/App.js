import React from 'react';
import './App.css';
import MyComponent from './MyComponent';
import MyComponentClass from './MyComponentClass';

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
      {/* <input /> */}
      <MyComponent name="react" favoriteNumber={3}>
        애기들
      </MyComponent>{' '}
      {/* name="React" */}
      <MyComponentClass favoriteNumber={5}>이것도 애기들</MyComponentClass>
    </>
  );
}

export default App;

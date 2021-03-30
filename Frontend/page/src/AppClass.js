import React, { Component } from 'react';
import './App.css';

// 클래스형 컴포넌트에는 render 함수가 꼭 있어야하며 반환하는 JSX가 있어야 한다.
class AppClass extends Component {
  render() {
    const name = '리액트';
    return <div style="react">{name}</div>;
  }
}

export default AppClass;

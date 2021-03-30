import React from 'react';
import './App.css';
import PropTypes from 'prop-types';

// const MyComponent = (props) => {
//   const { name, children } = props;
const MyComponent = ({ name, favoriteNumber, children }) => {
  return (
    <>
      <div className="react">어썸한 컴포넌트! 이건 바로 {name}지!!</div>
      <div>제일 좋아하는 숫자는 {favoriteNumber}</div>
      <div>children 값은 {children}</div>
    </>
  );
};

MyComponent.defaultProps = {
  name: 'Angular',
};

MyComponent.propTypes = {
  name: PropTypes.string,
  favoriteNumber: PropTypes.number.isRequired,
};

export default MyComponent;

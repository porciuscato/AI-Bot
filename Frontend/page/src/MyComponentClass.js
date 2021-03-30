import React, { Component } from 'react';
import PropTypes from 'prop-types';

class MyComponentClass extends Component {
  // static defaultProps = {
  //     name: 'cato',
  // }
  // static propTypes = {
  //     name: PropTypes.string,
  //     favoriteNumber: PropTypes.number.isRequired,
  // }
  render() {
    const { name, favoriteNumber, children } = this.props;
    return (
      <div>
        안녕! 난 {name}이야 <br />
        children은 {children}이고 <br />
        favoriteNumber는 {favoriteNumber}
      </div>
    );
  }
}

MyComponentClass.defaultProps = {
  name: 'cato',
};

MyComponentClass.propTypes = {
  name: PropTypes.string,
  favoriteNumber: PropTypes.number.isRequired,
};

export default MyComponentClass;

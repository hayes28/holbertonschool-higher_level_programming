#!/usr/bin/node
// Class Square that defines a square and inherits from Rectangle of 4-rectangle.js
// Must use the class notation for defining your class and extends
// The constructor must take 1 argument: size
// The constructor of Rectangle must be called (by using super())

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;

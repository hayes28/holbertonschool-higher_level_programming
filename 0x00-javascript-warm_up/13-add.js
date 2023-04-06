#!/usr/bin/node
// This script prints the addition of 2 integers
// The function must be visible from outside
// The name of the function must be add
// You are not allowed to use var
exports.add = function (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  return a + b;
};

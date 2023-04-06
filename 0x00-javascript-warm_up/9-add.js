#!/usr/bin/node
// This script prints the addition of 2 integers
// The first argument is the first integer
// The second argument is the second integer
// You have to define a function with this prototype: function add(a, b)
// You must use console.log(...) to print all output
// You are not allowed to use var

const args = process.argv;
function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  return (a + b);
}
console.log(add(args[2], args[3]));

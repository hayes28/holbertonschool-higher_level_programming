#!/usr/bin/node
// This script computes and prints a factorial
// The first argument is integer (argument can be cast as integer) used for computing the factorial
// Factorial of NaN is 1
// You must do it recursively
// You must use a function
// You must use console.log(...) to print all output
// You are not allowed to use var
const args = process.argv;
function factorial (a) {
  if (isNaN(a) || a === 1) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}
console.log(factorial(args[2]));

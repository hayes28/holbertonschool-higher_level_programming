#!/usr/bin/node
// This script prints x times “C is fun”
// Where x is the first argument of the script
// The first argument is the number of times the message will be printed
// If the first argument can’t be converted to an integer, print “Missing number of occurrences”
// You must use console.log(...) to print all output
// You are not allowed to use var
// You can use only two console.log
// You must use a loop (while, for, etc.)
const args = process.argv;
const x = parseInt(args[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
let i = 0;
while (i < x) {
  console.log('C is fun');
  i++;
}

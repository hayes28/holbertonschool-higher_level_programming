#!/usr/bin/node
// This script searches the second biggest integer in the list of arguments
// You can assume all arguments can be converted to integer
// If no argument passed, print 0
// If the number of arguments is 1, print 0
// You must use console.log(...) to print all output
// You are not allowed to use var

const args = process.argv;
const len = args.length;
if (len <= 3) {
  console.log(0);
} else {
  const arr = args.slice(2);
  const max = Math.max(...arr);
  const index = arr.indexOf(max.toString());
  arr.splice(index, 1);
  console.log(Math.max(...arr));
}

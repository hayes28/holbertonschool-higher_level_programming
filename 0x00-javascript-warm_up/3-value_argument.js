#!/usr/bin/node
// Prints the first argument passed to it
// If no arguments are passed to the script, print "No argument"
// You must use console.log(...) to print all output
// You are not allowed to use var
// You are not allowed to use length
const args = process.argv;
if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}

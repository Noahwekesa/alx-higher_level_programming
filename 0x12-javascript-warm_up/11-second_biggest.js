#!/usr/bin/node

const argument = process.argv;

if (argument.length === 2) {
    console.log(0);
} else {
    const args = argument
    .map(Number)
    .slice(2, argument.length)
    .sort((a, b) => a - b); 

    console.log(args[args.length - 2]);
}

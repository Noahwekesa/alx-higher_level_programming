#!/usr/bin/node

const argument = process.argv;
const firstArg = parseInt(argument[2]);
const secondArg = parseInt(argument[3]);

function add(a, b) {
    let sum = a + b;
    console.log(sum);
}

if ((isNaN(firstArg) && isNaN(secondArg)) || argument.length === 2) {
    console.log('NaN');
} else {
    add(firstArg, secondArg);
}
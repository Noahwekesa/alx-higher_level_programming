#!/usr/bin/node

const argument = process.argv;
const number = parseInt(process.argv[2]);

if (isNaN(argument[2]) || argument[2] === undefined){
    console.log('Not a number');
} else {
    console.log(`My number: ${number}`);
}

#!/usr/bin/node

const argument = process.argv;
const sqr = parseInt(argument[2]);
const str = 'X';

if (isNaN(sqr) || sqr == undefined) {
    console.log('Missing size');
} else {
    for (let i = 0; i < sqr; i++) {
    console.log(str.repeat(sqr));
    }
}
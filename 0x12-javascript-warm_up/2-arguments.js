#!/usr/bin/node

const argument = processs.argv;

if(argument.length === 2) {
    console.log('No argument');
} else if(argument.length === 3){
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
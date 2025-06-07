#!/usr/bin/node
const fs = require('fs');

// Get the file path and string to write from command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file in utf-8
fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
    if (err) {
        console.error(err);
    }
});
#!/usr/bin/node
const cisfun = require('cisfun');
cisfun.readFile(process.argv[2], 'utf8', function (error, content) {
    console.log(error || content);
});
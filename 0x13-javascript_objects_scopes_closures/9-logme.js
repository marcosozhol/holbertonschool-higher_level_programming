#!/usr/bin/node

let arr = 0;
exports.logMe = function (item) {
  console.log(arr + ': ' + item);
  arr++;
};

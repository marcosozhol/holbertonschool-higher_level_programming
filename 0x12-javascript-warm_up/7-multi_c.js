#!/usr/bin/node
let cont = 1;
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
}
while (cont <= process.argv[2]) {
  cont++;
  console.log('C is fun');
}

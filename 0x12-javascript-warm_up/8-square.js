#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
let cont = 1;
while (cont <= process.argv[2]) {
  cont++;
  console.log('X'.repeat(process.argv[2]));
}

#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  console.log(process.argv.splice(2).sort().reverse()[1]);
}

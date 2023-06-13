#!/usr/bin/node

if (!isNaN(Number(process.argv[2]))) {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    let msg = '';
    for (let j = 0; j < Number(process.argv[2]); j++) {
      msg = msg + 'X';
    }
    console.log(msg);
  }
} else {
  console.log('Missing size');
}

#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length > 1) {
  const sortArr = args.sort((x, y) => y - x);
  console.log(sortArr[1]);
} else {
  console.log(0);
}

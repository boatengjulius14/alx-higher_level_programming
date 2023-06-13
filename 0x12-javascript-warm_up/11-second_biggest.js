#!/usr/bin/node

function findSecondLargest (arr) {
  if (arr.length <= 3) {
    return (0);
  }

  let max = arr[0];
  let secondMax = arr[1];

  for (let i = 2; i < arr.length; i++) {
    if (arr[i] > max) {
      secondMax = max;
      max = arr[i];
    } else if (arr[i] > secondMax) {
      secondMax = arr[i];
    }
  }

  return (secondMax);
}

console.log(findSecondLargest(process.argv.slice(2).map(Number)));

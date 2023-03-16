#!/usr/bin/node

function esrever (list) {
  const len = list.length;
  const middleIndex = Math.floor(len / 2);

  for (let i = 0; i < middleIndex; i++) {
    const temp = list[i];
    list[i] = list[len - i - 1];
    list[len - i - 1] = temp;
  }
  return list;
}

exports.esrever = esrever;

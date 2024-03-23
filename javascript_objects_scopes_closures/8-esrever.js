#!/usr/bin/node
exports.esrever = function (list) {
  const j = list.length;
  const listreverse = [];
  for (let i = 0; i < list.length; i++) {
    listreverse[j - i - 1] = list[i];
  }
  return listreverse;
};

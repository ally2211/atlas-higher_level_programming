#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let countOccurrences = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { countOccurrences += 1; }
  }
  return countOccurrences;
};

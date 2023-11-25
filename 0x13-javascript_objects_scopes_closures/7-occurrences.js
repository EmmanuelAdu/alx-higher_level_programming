#!/usr/bin/node
/**
 * Function to return no. of occurences in a list
 */

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    count = (list[i] === searchElement ? count + 1 : count);
  }
  return count;
};

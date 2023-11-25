#!/usr/bin/node
/**
 * Reverse a list
 */

exports.esrever = function (list) {
  let left = 0;
  let right = list.length - 1;

  while (left < right) {
    const temp = list[left];
    list[left] = list[right];
    list[right] = temp;

    left++;
    right--;
  }
  return list;
};

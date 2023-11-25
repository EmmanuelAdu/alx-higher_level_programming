#!/usr/bin/node
// key = occurrences & value = userID.
const dict = require('./101-data').dict;

const newDict = {};
for (const userID in dict) {
  const occurrences = dict[userID];

  if (!newDict[occurrences]) {
    newDict[occurrences] = [userID];
  } else {
    newDict[occurrences].push(userID);
  }
}

console.log(newDict);

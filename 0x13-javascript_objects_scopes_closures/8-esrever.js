#!/usr/bin/node
/*
function that returns the reversed version of a list:

  Prototype: exports.esrever = function (list)
  You are not allow to use the built-in method reverse
*/

exports.esrever = function (list) {
  const newlist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newlist.push(list[i]);
  }
  return newlist;
};

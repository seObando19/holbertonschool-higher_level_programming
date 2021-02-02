#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

require('process');
const data = process.argv;

if (data.length > 3) {
  data.splice(0, 2);
  const maxNum = Math.max(...data);
  const newArry = data.filter(element => element !== maxNum.toString());
  console.log(Math.max(...newArry));
} else {
  console.log(0);
}

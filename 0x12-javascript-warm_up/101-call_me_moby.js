#!/usr/bin/node

exports.callMeMoby = function (X, _function) {
  for (let i = 0; i < X; i++) {
    _function();
  }
};

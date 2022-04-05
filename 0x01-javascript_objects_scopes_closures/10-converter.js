#!/usr/bin/node
exports.converter = function (base) {
  function myConverter (j) {
    return j.toString(base);
  }
  return myConverter;
};

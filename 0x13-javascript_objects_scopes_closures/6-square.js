#!/usr/bin/node

const Sq = require('./5-square');

module.exports = class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i = 0;
      for (i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};

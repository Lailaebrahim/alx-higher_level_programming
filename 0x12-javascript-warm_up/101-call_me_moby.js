#!/usr/bin/node
function callMeMoby (x, theFunction) {
  for (let i = x; i > 0; i--) {
    theFunction();
  }
}

module.exports = { callMeMoby };

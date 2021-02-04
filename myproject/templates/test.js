// test.js
'use strict';

const assert = require('assert');
const python = require('python-bridge');

const py = python(); // return value

const {
  ex, // no return value
  end,
} = py;

const list = [3, 4, 2, 1];

ex`import math`

async function pyscript() {
  try {
    let math = await py`math.sqrt(9)`;
    let sort = await py`sorted(${list})`;

    assert.equal(math, 3);
    assert.deepEqual(sort, list.sort());

  } catch (e) {
    console.log(e)
  }
  end();
}
pyscript();
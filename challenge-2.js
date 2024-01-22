/*
Write an application http sd exporter.

Your application needs write blackbox exporter check the difference in block number between two providers Ankr and Infura.:

if Ankr blocknumber - Infura blocknumber < 5 => success
else => fail
We're assuming that Infrura is the trusted source for checking the block number.
*/

const express = require('express');
const app = express();
const port = 3000;

const axios = require('axios');

const ankrUrl = '';

const infuraUrl = '';

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.get('/health', (req, res) => {
  res.send('OK');
});

app.get('/metrics', async (req, res) => {
  const ankrBlockNumber = await getAnkrBlockNumber();
  const infuraBlockNumber = await getInfuraBlockNumber();

  const difference = ankrBlockNumber - infuraBlockNumber;

  if (difference < 5) {
    res.send('ankr_block_number - infura_block_number < 5');
  } else {
    res.send('ankr_block_number - infura_block_number >= 5');
  }
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});

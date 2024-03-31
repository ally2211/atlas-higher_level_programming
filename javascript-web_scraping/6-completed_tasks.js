#!/usr/bin/node
const request = require('request');
const webpage = process.argv[2];

if (!webpage) {
  console.log('Usage: <script> <webpage>');
  process.exit(1);
}

request(webpage, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the JSON string into an object
  const jsonData = JSON.parse(body);

  if (!Array.isArray(jsonData)) {
    console.error('Error: Expected an array but got something else.');
    return;
  }

  // console.log("Array length:", jsonData.length); // Check the length of the array

  // Check if the array is not empty and log the first item
  // if (jsonData.length > 0) {
  //  console.log("First item in array:", jsonData[0]);
  // } else {
  //  console.log("The array is empty.");
  //  return;
  // }

  let runningCount = 0;
  const usersDone = [];
  const dictionary = {};
  const keys = [];
  const values = [];

  // Assuming jsonData is defined and populated correctly
  // console.log('jsonData length:', jsonData.length); // Debug jsonData length

  for (let i = 0; i < jsonData.length; i++) {
    // console.log('Loop i:', i); // Debug current iteration of i
    let currentUser = jsonData[i].userId;
    if (!usersDone.includes(jsonData[i].userId)) {
      for (let j = 0; j < jsonData.length; j++) {
        if (jsonData[i].userId === jsonData[j].userId && jsonData[j].completed === true) {
          // console.log('Match found for userId:', jsonData[i].userId, 'with completed:', jsonData[j].completed);
          runningCount += 1;
          usersDone.push(jsonData[j].userId);
          currentUser = jsonData[j].userId;
        }
      }

      // console.log(currentUser + ':' + runningCount);
      keys.push(currentUser);
      values.push(runningCount);
      runningCount = 0; // Reset for the next user
    }
  }
  keys.forEach((key, index) => {
    dictionary[key] = values[index];
  });

  console.log(dictionary);
});

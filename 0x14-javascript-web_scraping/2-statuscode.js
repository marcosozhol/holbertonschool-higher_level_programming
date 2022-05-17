#!/usr/bin/node
import axios from 'axios';
status_code = await axios.get(process.argv[2])
.then(Response => {
  console.log("code: ", status_code);
})
.catch(error => {
  console.log(error);
});
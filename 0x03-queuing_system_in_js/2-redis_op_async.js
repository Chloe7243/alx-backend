import { promisify } from "util";
import { createClient, print } from "redis";

const client = createClient();
client.on("error", (err) =>
  console.log(`Redis client not connected to the server: ${err}`)
);
client.on("connect", () => {
  console.log("Redis client connected to the server");
});

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
  const getValue = promisify(client.GET).bind(client);
  const value = await getValue(schoolName);
  console.log(value);
};

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");

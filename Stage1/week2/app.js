console.log("-------------------------Task1-------------------------");
const greenStation = ['Songshan',
'Nanjing Sanmin',
'Taipei Arena',
'Nanjing Fuxing',
'Songjiang Nanjing',
'Zhongshan',
'Beimen',
'Ximen',
'Xiaonanmen',
'Chiang Kai-Shek Memorial Hall',
'Guting',
'Taipower Building',
'Gongguan',
'Wanlong',
'Jingmei',
'Dapinglin',
'Qizhang',
'Xiaobitan',
'Xindian City Hall',
'Xindian']

const messages={
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Leslie":"I'm at home near Xiaobitan station.",
"Vivian":"I'm at Xindian station waiting for you."
};

function cleanUp(messages) {
  let cleanMessages = { ...messages };
  for (let message in messages) {
    for (let station of greenStation) {
      if (messages[message].includes("Xiaobitan")) {
        cleanMessages[message] = greenStation.indexOf("Qizhang") + 0.4;
      }
      else if (messages[message].includes("Xindian City Hall")) {
        cleanMessages[message] = greenStation.indexOf("Xindian City Hall")
      }
      else if (messages[message].includes(station)) {
        cleanMessages[message] = greenStation.indexOf(station)
      }
    }
  }
  return cleanMessages
}

function findAndPrint(messages, currentStation) {
  let currentStationIndex = greenStation.indexOf(currentStation);

  let cleanedMessages = cleanUp(messages);
  for (let message in cleanedMessages) {
    cleanedMessages[message] = Math.abs(cleanedMessages[message] - currentStationIndex)
  }
  let min = Math.min(...Object.values(cleanedMessages));
  console.log(Object.keys(cleanedMessages).find(key => cleanedMessages[key] === min));
}

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian

console.log("-------------------------Task2-------------------------");


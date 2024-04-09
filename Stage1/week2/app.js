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
  let closestMessageKey = null;

  for (let key in cleanedMessages) {
    if (cleanedMessages[key] === min) {
      closestMessageKey = key;
      break;
    }
  }
  console.log(closestMessageKey);
}

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian

console.log("-------------------------Task2-------------------------");

const consultants = [
  { "name": "John", "rate": 4.5, "price": 1000 },
  { "name": "Bob", "rate": 3, "price": 1200 },
  { "name": "Jenny", "rate": 3.8, "price": 800 }
];

let consultantAvailability = null;

function initConsultantAvailability() {
  if (!consultantAvailability) {
    consultantAvailability = consultants.map(consultant => ({
      ...consultant,
      time:[]
    }));
  }
}

function checkAvailability(hour, duration) {
  let availableConsultants = [];
  let timeToBook = [];
  for (let i = 0; i < duration; i++) {
    timeToBook.push(hour + i);
  }

  consultantAvailability.forEach((consultant) => {
    let notAvailable = timeToBook.some(t => consultant.time.includes(t));
    availableConsultants = notAvailable ? availableConsultants : availableConsultants.concat(consultant);
  });

  return { availableConsultants, timeToBook };
}

function chooseBest(availableConsultants, criteria) {
  if (availableConsultants.length === 0) return null;

  return availableConsultants.reduce((best, consultant) => {
    if (criteria === "rate") {
      return consultant.rate > best.rate ? consultant : best;
    } else if (criteria === "price") {
      return consultant.price < best.price ? consultant : best;
    }
    return best;
  });
}

function book(consultants, hour, duration, criteria) {
  initConsultantAvailability();
  let { availableConsultants: candidates, timeToBook } = checkAvailability(hour, duration);
  let best = chooseBest(candidates, criteria);
  if (best) {
    best.time.push(...timeToBook);
    console.log(best.name);
  } else {
    console.log("No Service");
  }
}

book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John

console.log("-------------------------Task3-------------------------");
function findUniqueIndex(arr) {
  const frequencyMap = arr.reduce((acc, cur) => {
    acc[cur] = (acc[cur] || 0) + 1;
    return acc;
  }, {});

  return arr.findIndex(element => frequencyMap[element] === 1) ;
}

function func(...data){
  let middleName = [];
  data.forEach(name => {
    if (name.length == 2) {
      middleName.push(name[1]);
    } else if (name.length == 3) {
      middleName.push(name[1]);
    } else if (name.length == 4) {
      middleName.push(name[2]);
    } else if (name.length == 5) {
      middleName.push(name[2]);
    }
  })

  console.log(data[findUniqueIndex(middleName)] || "沒有");
}

func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安

console.log("-------------------------Task4-------------------------");

function getNumber(index) {
  let sum = 0;
  for (let i = 1; i <= index; i++) {
    if (index == 0) { break }
    if (i % 3 == 1 || i % 3 == 2) {
      sum += 4;
    } else {
      sum -= 1;
    }
  }
  console.log(sum);
}

getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70

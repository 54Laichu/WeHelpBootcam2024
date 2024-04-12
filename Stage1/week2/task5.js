function findStat(stat) {
  let car = [];
  for (let i = 0; i < stat.length; i++) {
    if (stat[i] == 1) {
      car.push(i);
    }
  }
  return car
}

function find(spaces, stat, n) {
  let carCanBook = findStat(stat);
  if (carCanBook == []) return -1;

  let perfectCar = {};
  for (let car of carCanBook) {
    spaces[car] >= n ? perfectCar[car] = spaces[car] : null;
  }

  let result = Object.keys(perfectCar).length == 0 ? -1 : Object.keys(perfectCar).reduce((a, b) => perfectCar[a] < perfectCar[b] ? a : b);
  console.log(result);
}


find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2

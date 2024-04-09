print("----------Task 1----------")
green_station = [
  'Songshan', 'Nanjing Sanmin', 'Taipei Arena', 'Nanjing Fuxing',
  'Songjiang Nanjing', 'Zhongshan', 'Beimen', 'Ximen', 'Xiaonanmen',
  'Chiang Kai-Shek Memorial Hall', 'Guting', 'Taipower Building',
  'Gongguan', 'Wanlong', 'Jingmei', 'Dapinglin', 'Qizhang', 'Xiaobitan',
  'Xindian City Hall', 'Xindian'
]

messages = {
  "Bob": "I'm at Ximen MRT station.",
  "Mary": "I have a drink near Jingmei MRT station.",
  "Copper": "I just saw a concert at Taipei Arena.",
  "Leslie": "I'm at home near Xiaobitan station.",
  "Vivian": "I'm at Xindian station waiting for you."
}

def clean_up(messages):
  clean_messages = messages.copy()
  for message, text in messages.items():
    for station in green_station:
      if "Xiaobitan" in text:
        clean_messages[message] = green_station.index("Qizhang") + 0.4
        break
      elif "Xindian City Hall" in text:
        clean_messages[message] = green_station.index("Xindian City Hall")
        break
      elif station in text:
        clean_messages[message] = green_station.index(station)
        break
  return clean_messages

def find_and_print(messages, current_station):
  current_station_index = green_station.index(current_station)
  cleaned_messages = clean_up(messages)

  for message, index in cleaned_messages.items():
    cleaned_messages[message] = abs(index - current_station_index)

  min_distance = min(cleaned_messages.values())
  closest_message_key = None

  for key, value in cleaned_messages.items():
    if value == min_distance:
      closest_message_key = key
      break

  print(closest_message_key)

find_and_print(messages, "Wanlong")  # Should print "Mary"
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian

print("----------Task 2----------")

consultants = [
  {"name": "John", "rate": 4.5, "price": 1000},
  {"name": "Bob", "rate": 3, "price": 1200},
  {"name": "Jenny", "rate": 3.8, "price": 800}
]

consultant_availability = None

def init_consultant_availability(consultants):
  global consultant_availability
  if consultant_availability is None:
    consultant_availability = [{"name": c["name"], "rate": c["rate"], "price": c["price"], "time": []} for c in consultants]

def check_availability(hour, duration):
  available_consultants = []
  time_to_book = list(range(hour, hour + duration))

  for consultant in consultant_availability:
    not_available = any(t in consultant["time"] for t in time_to_book)
    if not not_available:
      available_consultants.append(consultant)

  return available_consultants, time_to_book

def choose_best(available_consultants, criteria):
  if not available_consultants:
    return None
  best = None
  if criteria == "rate":
    best = max(available_consultants, key=lambda x: x[criteria])
  elif criteria == "price":
    best = min(available_consultants, key=lambda x: x[criteria])
  return best

def book(consultants, hour, duration, criteria):
  global consultant_availability
  init_consultant_availability(consultants)
  available_consultants, time_to_book = check_availability(hour, duration)
  chosen_one = choose_best(available_consultants, criteria)
  if chosen_one:
    chosen_one["time"].extend(time_to_book)
    print(chosen_one["name"])
  else:
      print("No Service")

# Running the book function with given parameters
book(consultants, 15, 1, "price")  # Jenny
book(consultants, 11, 2, "price")  # Jenny
book(consultants, 10, 2, "price")  # John
book(consultants, 20, 2, "rate")  # John
book(consultants, 11, 1, "rate")  # Bob
book(consultants, 11, 2, "rate")  # No Service
book(consultants, 14, 3, "price")  # John

print("----------Task 3----------")
def find_unique_index(arr):
  frequency_map = {}
  for cur in arr:
    frequency_map[cur] = frequency_map.get(cur, 0) + 1

  for index, element in enumerate(arr):
    if frequency_map[element] == 1:
      return index
  return -1

def func(*data):
  middle_name = []
  for name in data:
    if len(name) == 2 or len(name) == 3:
      middle_name.append(name[1])
    elif len(name) == 4 or len(name) == 5:
      middle_name.append(name[2])

  unique_index = find_unique_index(middle_name)
  if unique_index != -1:
    print(data[unique_index])
  else:
    print("沒有")

func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安

print("----------Task 4----------")

def get_number(index):
  sum = 0
  for i in range(1, index + 1):
    if i % 3 == 1 or i % 3 == 2:
      sum += 4
    else:
      sum -= 1
  print(sum)

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70

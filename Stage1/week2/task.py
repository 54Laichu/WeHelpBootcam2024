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

def init_consultant_availability():
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
    init_consultant_availability()
    available_consultants, time_to_book = check_availability(hour, duration)
    best = choose_best(available_consultants, criteria)
    if best:
        best["time"].extend(time_to_book)
        print(best["name"])
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

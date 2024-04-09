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

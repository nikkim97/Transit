# Transit-Info

Manage schedules of different trains for a single station

## Problem Statement

To add a new train line:

```
API Request Example:

Train=NYCP
Times=[08:00, 09:30, 11:00, 12:30]

1.a) Check to see if value exists 
1.b) Check to see if train name is 4 alphanumeric char
1.c) Check to see if the time values are in correct time format
1.d) All times must be unique and sorted

```

To get all next trains coming to the station after a given time

```
API Request Example:

Input: 10:45

Output: [12:00: [NYC1, NWRK]]

Input 07:45

Output: [8:00: [TOMO, HOBK]]

2.a) Check to see if input is in correct time format
```

## Database:

```
db.set(key, value):
    ```Sets value associated with a key```
    ```No return value```
db.fetch(key):
    ```Retrieve set as a key```
    ```Returns object else None```
db.keys():
    ```Returns list of all keys in database```
    ```Else None```
```

Key-value pair

```
{
    "NYC1": "[08:00, 09:30, 11:00, 12:30, 14:00, 15:30, 16:00, 18:00]",
    "NWRK": "[08:00, 09:30, 11:00, 12:30, 14:00, 15:30, 16:00, 18:00]",
    "TOMO": "[08:00, 09:30, 11:00, 12:30, 14:00, 15:30, 16:00, 18:00]",
    "HOBK": "[08:00, 09:30, 11:00, 12:30, 14:00, 15:30, 16:00, 18:00]",
    "PRIN": "[08:00, 09:30, 11:00, 12:30, 14:00, 15:30, 16:00, 18:00]"
}  
```

### How to run app locally:
```
Run application under src/app.py

Once local host is running, 
    1. To get train schedule: 
        curl http://127.0.0.1:5000/trains
    2. To add a new train:
        curl -d "Train=NCP1&Times=[08:00, 09:30, 11:00, 12:30]" -X POST http://localhost:5000/trains
    3. To get trains after specific time:
        curl -d "Time=16:00" -X POST http://localhost:5000/times 
```

## FAQ:
1) Accepted time formats is 24 hrs 
```
Time format that match:
1. “01:00”, “13:00”,“23:00”
2. “23:59″,”15:00”, “00:00″,”0:00”

Time format doesn’t match:
1. “24:00” or “12:60” – hour and min is out of range [0-23] & [00-59]
2. “0:0” or "11:9" – invalid format for minute, at least 2 digits
3. “101:00” – hour is out of range [0-23]
```

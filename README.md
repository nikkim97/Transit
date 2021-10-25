# Transit-Info

Manage schedules of different trains for a station

## Problem Statement

Names and times of trains that come to the station

```
1) I should be able to add a new train line: 

NYCP: [9, 10, 11, 12, 1, 2, 3, 4, 5]

1.a) Check to see if value exists 
1.b) Check to see if train name is 4 AN char
1.c) Check to see if the time values are in correct time format

```

```
2) I should be able to provide a time value and get back all next incoming trains: 

Input: 10:45

Output: 

NYC1, 12:00 PM,
NEWR: 12:00 PM,
TOMO 12:00 PM, 
HOBK, 12:00 PM
PRIN, 12:00 PM

Input 7:45 PM

NYC1, 8:00 AM
NEWR, 8:00 AM
TOMO, 8:00 PM
HOBK, 8:00 AM
PRIN, 8:00 AM

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
[
    {
        'train': 'NYC1',
        'times': ["8:00", "9:30", "11:00", "12:30", "2:00", "3:30", "5:00", "7:30"]
    },
    {
        'train': 'NWRK',
        'times': ["8:00", "9:30", "11:00", "12:30", "2:00", "3:30", "5:00", "7:30"]
    },
    {
        'train': 'TOMO',
        'times': ["8:00", "9:30", "11:00", "12:30", "2:00", "3:30", "5:00", "7:30"]
    },
    {
        'train': 'HOBK',
        'times': ["8:00", "9:30", "11:00", "12:30", "2:00", "3:30", "5:00", "7:30"]
    },
    {
        'train': 'PRIN',
        'times': ["8:00", "9:30", "11:00", "12:30", "2:00", "3:30", "5:00", "7:30"]
    },
]
```

## Q/A:
1) Why flask? 
    Was considering FASTApi but since this is just a quick prototype and doesn't have any speed requirements I used flask
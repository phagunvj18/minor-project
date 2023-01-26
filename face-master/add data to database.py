# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 21:09:18 2023

@author: phagun vijay
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendance-master-5d9b8-default-rtdb.firebaseio.com/"
})
 
ref = db.reference('Students')

data = {
        "04411504919":
            {
                "name": "phagun vijay",
           "branch": "EEE",
           "batch_year": 2019,
           "total_attendance": 7,
           "place": "library",
           "year": 4,
           "last_attendance_time": "2023-01-03 00:26:26"
                },
            "1234":
                {
                    "name": "dr. abhishek gandhar",
               "branch": "staff",
               "batch_year": 2000,
               "total_attendance": 700,
               "place": "library",
               "year": 4,
               "last_attendance_time": "2023-01-03 00:26:26"
                    },
                "04611504919":
                    { 
                        "name": "rudra sharma",
                "branch": "EEE",
                "batch_year": 2019,
                "total_attendance": 7,
                "place": "library",
                "year": 4,
                "last_attendance_time": "2023-01-03 00:26:26"
                        },
                    "04911504919":
                        {
                            "name": "adarsh patra",
                    "branch": "EEE",
                    "batch_year": 2019,
                    "total_attendance": 7,
                    "place": "library",
                    "year": 4,
                    "last_attendance_time": "2023-01-03 00:26:26"
                            },
                        "01611504919":
                            {
                                "name": "madhav sood",
                        "branch": "EEE",
                        "batch_year": 2019,
                        "total_attendance": 7,
                        "place": "library",
                        "year": 4,
                        "last_attendance_time": "2023-01-03 00:26:26"
                                }
            
            
            
            }
    
for key, value in data.items():
    ref.child(key).set(value)
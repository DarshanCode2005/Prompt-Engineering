from ics import Calendar, Event
from datetime import datetime, timedelta

# Create a new calendar
calendar = Calendar()

# Define the event details for each topic
event_details = [
    ("React.js Basics (JSX, Components, Props, and State)", "2024-11-27", "2024-11-30", "09:00", "12:00"),
    ("Hooks and Event Handling (useState, useEffect)", "2024-11-27", "2024-11-30", "13:00", "16:00"),
    ("Practice or mini-project", "2024-11-27", "2024-11-30", "17:00", "20:00"),
    ("React Native Basics (Layouts, Styling)", "2024-12-01", "2024-12-03", "09:00", "12:00"),
    ("Navigation and Forms (React Navigation)", "2024-12-01", "2024-12-03", "13:00", "16:00"),
    ("Practice or mockup project", "2024-12-01", "2024-12-03", "17:00", "20:00"),
    ("Node.js Basics and Express.js Setup", "2024-12-04", "2024-12-06", "09:00", "12:00"),
    ("REST APIs, Middleware, and Database Integration", "2024-12-04", "2024-12-06", "13:00", "16:00"),
    ("Practice building CRUD operations", "2024-12-04", "2024-12-06", "17:00", "20:00"),
    ("SQL Basics (CRUD operations)", "2024-12-07", "2024-12-07", "09:00", "12:00"),
    ("MongoDB Basics (Collections, Queries)", "2024-12-07", "2024-12-07", "13:00", "16:00"),
    ("Database integration with your project", "2024-12-07", "2024-12-07", "17:00", "20:00"),
]

# Add events to the calendar
for title, start_date, end_date, start_time, end_time in event_details:
    start_datetime = datetime.strptime(f"{start_date} {start_time}", "%Y-%m-%d %H:%M")
    end_datetime = datetime.strptime(f"{start_date} {end_time}", "%Y-%m-%d %H:%M")
    while start_datetime.date() <= datetime.strptime(end_date, "%Y-%m-%d").date():
        event = Event()
        event.name = title
        event.begin = start_datetime.isoformat()
        event.end = end_datetime.isoformat()
        calendar.events.add(event)
        start_datetime += timedelta(days=1)
        end_datetime += timedelta(days=1)

# Save the calendar to an .ics file
with open("Event_Breakdown.ics", "w") as file:
    file.writelines(calendar)

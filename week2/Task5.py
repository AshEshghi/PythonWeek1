#Task 5 Ash Eshghi
events= {
    "Dortmund Food Festival": "05.09.2026",
    "Football Match": "12.09.2026",
    "Night of Museums - Art Exhibition": "19.09.2026",
    "Night of Museums - Museum Tour": "19.09.2026",
    "Night of Museums - Light Show": "19.09.2026",
    "City Music Festival": "25.09.2026",
    "Autumn Market": "03.10.2026"
}
date= "19.09.2026"
print("Events during the Night of Museums in Dortmund:")
for event, event_date in events.items():
    if event_date == date and "Night of Museums" in event:
        print(event)

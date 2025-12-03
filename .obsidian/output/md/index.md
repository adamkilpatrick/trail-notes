---
tags: []
---
# index   
   
Hello. You've somehow made it to this place before I felt comfortable sharing things with people, but at least it means the infra works mostly. I will add some details to this in time but the intent is to capture some notes on how I die on going to the woods because I am an enormous dumbass!   
   
## Recently Updated   
```dataview
TABLE WITHOUT ID 
file.folder AS "Folder", file.link AS "File", dateformat(file.mtime, "yyyy.MM.dd - HH:mm") AS "Last modified"
FROM ""
SORT file.mtime DESC
LIMIT 10
```

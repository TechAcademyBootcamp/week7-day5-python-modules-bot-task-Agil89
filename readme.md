# pythonbot_task
## Aşağıdakı xüsusiyyətlərə malik python bot yaradın. 
1. Bot istifadəçilərin suallarına cavab verməlidir. Bunun üçün bot-un içində suallar və onlara uyğun cavablar olan fayl olmalıdır. İstifadəçi sual verdikdə bot həmin suala uyğun cavab(lar)ı fayldan axtarmalı, əgər cavabı taparsa bu zaman istifadəçiyə həmin cavablardan birini verməlidir. Əgər tapmazsa, istifadəçiyə bot-u öyrətmək imkanı verilməlidir. İstifadəçi sualı və ona uyğun cavabı daxil etməlidir. Sual və onun cavab(lar)ı fayla əlavə edilməlidir.
2. İstifadəçi bot-dan yeni xəbərlərin siyahısı tələb etdikdə bot https://oxu.az/ saytından istifadəçiyə bu günü xəbər başlıqlarını və linklərini paylaşmalıdır.
3. İstifadəçi bot-dan cari valyuta məzənnəsini istədikdə bot bu günə valyuta məzənnəsini paylaşmalıdır. API üçün https://exchangeratesapi.io/ websaytdan istifadə edə bilərsiniz.
4. İstifadəçi bot-dan bu günün hava haqqında məlumatlarını istədikdə bot hava haqqında məlumatları paylaşmalıdır. API üçün https://exchangeratesapi.io/ websaytdan istifadə edə bilərsiniz. https://openweathermap.org/api
5. İstifadəçi bot-dan google-da axtarmağı və uyğun axtarışa uyğun nəticələri paylaşmağını istədikdə bot həmin məlumatları axtarmalı və axtarışa uyğun başlıqları və linkləri paylaşmalıdır.

## Qeydlər:
- Program dövr şəklində davam etməlidir. İstifadəçi sual yerinə `exit` yazdıqda program dayanmalıdır.
- Hər bir əməliyyatin blokunun funksiya şəklində yazılmasına fikir verin. (Functional Programming)
- `requests`, `beautifulSoup` modulları istifadə edilməlidir.
- `virtualenv` istifadə etməyi unutmayın.


# Eng:
## Develop an application with following properties.  
1. Bot has to answer to the questions of users. For that there have to be file with questions and answers to them. Bot has to look for answer in that filw after user asks question and has to send send it user if there is any answer. User should let to teach Bot if there is no answer for question. User has to add question and answer for it. Question and answer of it must be added to the file. 
2. Bot has to show todays news and links to user from https://oxu.az/ when he asks for news.
3. If user asks for currency rates then bot has to show current rates. https://exchangeratesapi.io/ can be used for api.
4. If user asks for weather forecast bot has to show todays weather forecats. https://openweathermap.org/api can be used as api.
5. If users asks for goole search then bot has to show him current search results and links.
## Notes:
- The program should continue in the form of a cycle. The program must stop when the user writes `exit` instead of the question.
- Note that each operation block is written as a function. (Functional Programming)
- Use `requests`, `beautifulSoup` modules
- Do not forget to use `virtualenv`.

### Virtualenv yüklənmə forması (1 dəfə yüklənməlidir)
`pip install virtualenv`

### Virtualenv yaratma forması (hər proyekt üçün 1 dənə virtualenv olmalıdır, yəni 1 dəfə edəcəksiz)
`virtualenv .venv`

### Virtualenv aktivləşdirmə:
`source .venv/bin/activate`
- Virtualenv aktiv edildikdən sonra requests, beautifulSoup kimi yükləməlisiniz.
- Virtualenv aktiv edildikdən sonra requests, beautifulSoup moduları istifadə edə biləcəksiniz. Əks halda istifadə edə bilməyəcəksiniz.
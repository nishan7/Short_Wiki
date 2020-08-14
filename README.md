# Short Wiki
It a python script designed with requests, beautifulsoup4 and 
spaCy  to create the summary of wikipedia article

#### Wikipedia
It uses wikipedia REST API to search for the article and 
get the data from the article

API:
https://en.wikipedia.org/w/rest.php

#### spaCy
It uses the NLP spaCy module to generate summary of the wikipedia article

#### Example

```
search(search_query='Earth', no_of_sentences=5)
```
Ouput:
```
Earth is the third planet from the Sun and the only astronomical object known to harbor life.
Earth orbits around the Sun in 365.256 solar days, a period known as an Earth sidereal year.
During this time, Earth rotates about its axis 366.256 times, that is, a sidereal year has 366.256 sidereal days.
The radius of the inner core is about one fifth of that of Earth.
The mean heat loss from Earth is 87 mW m−2, for a global heat loss of 4.42×1013 W. Cartography, the study and practice of map-making, and geography, the study of the lands, features, inhabitants and phenomena on Earth, have historically been the disciplines devoted to depicting Earth.

```

 
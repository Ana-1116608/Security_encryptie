# Symmetrisch encryptie
Dit is eigenlijk de private key een sleutel die versleutelt maar ontsleutelt ook zender en ontvanger moeten beiden dezelfde private key hebben. 
Je hebt platte tekst (plaintext), een algoritme (cipher) en een sleutel. Het algoritme husselt de tekst met de sleutel door elkaar tot ciphertext. 
Dit is onleesbare data . Wie dezelfde sleutel heeft, draait het proces om en krijgt de originele tekst terug. Zonder sleutel is de ciphertext  onbruikbaar. 

## Voordeel
Het is snel en goed inzetbaar voor grote hoeveelheid data. Het is ook minder complex dan asymmetrisch

## Nadeel
Het nadeel hieraan is hoe zorg ik er voor dat ik mijn private key bij iemand anders kan krijgen op een veilige manier zonder dat iemand anders
mee luistert of mee kijkt. Je kan de private key versturen maar een aanvaller kan deze via het verkeer onderscheppen.
Om dit veilig te doen heb je eigenlijk een veilig kanaal nodig om dit te overhandigen. 
Je kan dit bijvoorbeeld persoonlijk overhandigen of via asymmetrische encryptie 


# Asymmetrisch encryptie
Bij asymmetrische encryptie heeft elke gebruiker een sleutelpaar dat bij elkaar hoort. Wat je met de ene sleutel versleutelt, 
kun je alleen met de andere ontsleutelen. De publieke sleutel deel je met iedereen, de private sleutel houd je geheim en verlaat nooit je apparaat.
Wil je een geheim bericht sturen naar je klasgenoot dan versleutelt je dit bericht met je klasgenoot zijn public key alleen je klasgenoot
kan deze ontsleutelen met zijn of haar private key. Je kan dit bericht dan niet meer terug lezen.

De veiligheid bij deze sleutels zet wiskundige problemen die in één richting makkelijk en in de andere richting extreem moeilijk zijn.
Bij RSA is dat het ontbinden van een heel groot getal in priemfactoren, bij ECC het discrete-logaritmeprobleem op elliptische krommen.

## Voordeel
Er is geen geheime uitwisseling nodig zoals bij de keys zoals bij Symmetrisch encryptie. 
De public key mag je gewoon openbaar neer zetten en delen. Ook heb je makkelijke sleutel paren dan bij symmetrische encryptie
dus 100 gebruikers hebben 100 paren nodig 

## Nadelen
De wiskunde is veel zwaarder dan bij AES, Daarom gebruik je deze keys niet bij grote bestanden en veel data.
Het kan ook niet meer data versleutelen dat groter is dan de sleutel zelf 
Ook kan je nooit zeker weten dat de publieke sleutel echt van je klasgenoot is en niet van een aanvaller die zich voor doet als je klasgenoot. 
Daarvoor heb je vertrouwensstructuur nodig, zoals certificaten en certificaatautoriteiten


# In praktijk hybride
Meestal worden beiden sleutels gecombineerd. Asymmetrisch om veilig een sleutel af te spreken, daarna symmetrisch om de eigenlijke data te versleutelen.
Zo werkt bijvoorbeeld HTTPS/TLS

# Kerckhoffs’s Principe
Hier word eigenlijk gezegd het systeem moet veilig blijven ook als een aanvaller precies weet hoe dit systeem werkt. Het enige wat geheim moet zijn zijn de sleutels of sleutel. 
Dus de veiligheid zit eigenlijk in het geheim houden van de sleutel.
Het tegenovergestelde hiervan is erop vertrouwen dat niemand het systeem kan kraken omdat niemand weet hoe het werkt. 
Dat is een slecht plan, want een geheim algoritme is nooit door onafhankelijke experts getest, dus fouten blijven onopgemerkt. 
En als het algoritme dan toch uitlekt door een medewerker, of een datalek is het hele systeem meteen waardeloos, omdat je het niet zomaar kunt vervangen. 

Daarom kies je voor openbare gesteente standaarden zoals AES (advanced Encryption Standard.) 
Er word al jaren geprobeerd deze te breken en als er zwakke plekken zijn worden deze gevonden en opgelost. 
een eigen algoritme bedenken is gevaarlijk, omdat je zelfs als ervaren ontwikkelaar fouten maakt die je zelf niet ziet.


# Mijn encryptiealgoritme keuze
Ik heb gekozen voor AES (Advanced Encryption Standard) als mijn encryptiealgoritme. Daarna kon ik kiezen tussen 3 versies hiervan de AES-128, AES-192 en de AES-256. Omdat ik een applicatie ga maken waarbij gebruikers makkelijk hun teksten kunnen versleutelen en ontsleuten heb ik gekzoen voor de AES-256 Deze heeft 256 bits. Ik heb gekzoen voor deze omdat deze de meeste bits heeft dus de meeste sleutel combinaties. Ook is dit de meest veiligste sleutel van allemaal. Hij is wel wat trager dan de andere 2 door de wiskundige berekeningen die hij moet maken maar hij is wel het veiligst. Ik zet dus veiligheod boven snelheid met deze keuze 


# Implementatie
In de implementatie heb ik gebruik gemaakt van de cryptography library in Python. Deze heeft een eenvoudige interface voor het gebruik van AES. De library zorgt ook voor een goede afhandeling van sleutels en initialisatie vectoren (IV's), wat belangrijk is voor de veiligheid van de encryptie. Ik heb deze geimport op code regel 1. 

Ik heb daarna een secret key bestand gemaakt waarin de gegenereerde sleutel is opgeslagen. deze heb ik in de gitignore gezet zodat deze niet per ongeluk geüpload wordt.

ik heb daarna de eerste if-else statment geschreven voor het generen van een secret key. Deze word opgeroepen als het bestand nog niet bestaat.

Daarna heb ik de encryptie functie geschreven. Deze neemt de plaintext en de secret key als input en geeft de ciphertext terug. Vervolgens heb ik de decryptie functie geschreven, die de ciphertext en de secret key als input neemt en de oorspronkelijke plaintext teruggeeft. Ik heb hiervoor beide base 64 toegepast. Base 64 wordt gebruikt om binaire data leesbaar te maken in mensen tekst.

Daarna heb ik de input/output functionaliteit toegevoegd, zodat gebruikers hun teksten kunnen versleutelen en ontsleutelen via de console. Ik heb ze hierbij 2 keuzes gegeven: 1 voor encryptie en 2 voor decryptie. Als je het bestand runt kan je kiezen optie 1 of 2 kies encryptie optie en voer de tekst in die je wilt versleutelen. kopieer de uitvoer en gebruik deze als invoer voor de decryptie optie.

Ook heb ik hiervoor een foutmelding toegevoegd voor het geval de gebruiker een ongeldige keuze maakt of als de decryptie mislukt.
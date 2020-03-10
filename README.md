# Prvi preizkus virtualnega IT hekatona
> Koliko pikslov je lahko velik posamezen znak besedila prikazanega na zaslonu, ne da bi pri tem razdelili katero koli besedo

## Navodila

### LedDisplay

Prejel si naročilo iz podjetja MojaTrgovina. Naročnik želi, da se kupcu, ki skenira črtno kodo izdelka, na led zaslonu izpiše ime, cena in opis skeniranega izdelka. Vsi artikli, ki jih uporabnik skenira, morajo biti izpisani na zaslonu. V različnih trgovinah po Sloveniji imajo zaslone različnih velikosti, vendar so vsi pravokotni. Širina in višina zaslona sta navedena spodaj, skupaj z besedilom, ki naj bo izpisano na zaslonu. Ker želimo izkoristiti cel led zaslon je potrebno preračunati koliko pikslov je lahko velik posamezen znak besedila prikazanega na zaslonu, ne da bi pri tem razdelili katero koli besedo. Vsi znaki morajo imeti enako širino in višino (npr. 'l' in 'm' zavzemata isti vodoravni prostor, kot tudi presledek). Znaki pisave so enake širine in višine, zato ni dodatnega razmika med sosednjimi znaki ali sosednjimi vrsticami.

### Vhod

Vsaka vrstica vhodne datoteke vsebuje en testni primer v obliki 'S V B'. S je širina in V višina število pikslov razpoložljivega prostora; B je besedilo, ki bi se naj prikazalo na led zaslonu.

### Izhod

Izhod vsebuje po eno vrstico za vsak primer. Če teksta ne moremo prikazati potem je vrednost 0.

### Oddaja rešitve

V prilogi se nahaja datoteka vhodi.txt, ki vsebuje testne primere, katere morate rešiti z vašim programom. Kot rešitev naloge oddate ZIP arhiv, ki vsebuje programsko rešitev (programsko kodo). V opis pri oddaji ideje dodajte izhode, ki jih vrne vaš program za testne primere iz datoteke vhodi.txt. Rešitve brez ustreznega opisa se ne bodo upoštevale.

Prenesi datoteko: [Datoteka vhodi.txt](http://kariernisejem.com/wp-content/uploads/2020/03/vhodi.txt)

### Primer delovanja programa
```
Vhod:
20 6 led display
100 20 led display 2020
10 20 MUST BE ABLE TO DISPLAY
55 25 Can you hack
100 20 display product text

Izhod:
2
9
1
8
8
```

## Rešitev

### Vzpostavitev
Rešitev je napisana v programskem jeziku Python. Zaženemo jo z ukazon

```bash
python solution.py vhod.txt
```

V primeru, da ne podamo argumenta ali vnesemo napačno ime datoteke, nam rešitev vrne napako.

```bash
$ python solution.py
Vhodna datoteka ni bila podana.
Delovanje: python solution.py <vhod.txt>

$ python solution.py ni_vhodov.txt
Vhodna datoteka "ni_vhodov.txt" ni bila najdena.
```


### Algoritem
Algoritem najprej z matematično formulo najde maksimum pikslov, ki jih lahko zavzame ena črka.
Nato z uporabo bisekcije poišče rezultat. 
Natančnejši opis delovanja najdemo v izvorni kodi
([solution.py](https://github.com/zanozbot/mojedelo-virtualni-hekaton-2020/blob/master/solution.py)).

### Primer delovanja programa
```
Vhod:
27 15 May the Force be with you
10 40 Legen wait-for-it dary, legendary
420 100 You want the truth? You can't handle the truth
65 65 Houston, we have a problem
345 160 My mama always said life was like a box of chocolates. You never know what you're gonna get
230 130 You know nothing, Jon Snow
14 10 Dobby is free
15 80 Say 'hello' to my little friend!
100 15 Live long and prosper
23 2 Bazinga

Izhod, kjer upoštevamo presledek kot prvi znak v novi vrstici:
$ python solution.py vhodi.txt True

3
0
25
8
22
26
2
2
7
2

Izhod, kjer ne upoštevamo presledka kot prvi znak v novi vrstici:
$ python solution.py vhodi.txt False

3
0
26
8
22
28
2
2
7
2
```
# E-Scooter Chase

Ein kleines Top-Down-Actionspiel im Browser (HTML5 Canvas, keine Abhängigkeiten).
Du fährst mit einem E-Scooter durch eine Stadt, Polizeistreifen tauchen auf und verfolgen dich –
mit einem Fahndungslevel-System (1–5 Sterne) wie in GTA 5.

## Versionen

- `index.html` – 2D-Version (Draufsicht, läuft komplett offline)
- `3d.html` – 3D-Version mit three.js (Kamera hinter dem Roller, Häuser mit Höhe, 3D-Polizeiautos und Hubschrauber mit Suchscheinwerfer). Braucht beim Laden Internet, weil three.js vom CDN kommt.

In der 3D-Version bewegst du dich zu Fuß relativ zur Kamera; die Kamera dreht sich mit, während du Roller fährst.

Nur in der 3D-Version:
- **Rechte Maustaste halten** (Handy: oben über den Bildschirm wischen) = Kamera drehen/umsehen. Beim Fahren schwenkt sie nach dem Loslassen zurück hinter den Roller.
- Der **Lenker** dreht sich beim Lenken mit, Roller und Fahrer legen sich in die Kurve.
- **Geld:** Streifenwagen zerstören (+$200 + $50 pro Stern), Hubschrauber (+$1.000), erfolgreiche Flucht (+$100 bis +$1.500 je nach Sternen). Festnahme kostet 25 % Kaution, WASTED $200 Krankenhausrechnung. Das Geld bleibt im Browser gespeichert.
- **Ampeln** an allen Kreuzungen (16-Sekunden-Takt, abwechselnd für waagrechte und senkrechte Straßen).
- **Passanten** laufen auf den Gehwegen um die Blöcke und überqueren die Straße über die Zebrastreifen – nur wenn die Autos Rot haben. Bei Schüssen rennen sie weg.
- **Anfahren** mit dem Roller (oder durch Polizeiautos) → Ragdoll, nach 2 Sekunden stehen sie wieder auf. **Erschießen** kostet 50 $ pro Passant und gibt sofort einen Stern.
- **Wheelie:** Umschalt (Shift) halten, Roller und Moped ab etwas Tempo (Handy: Taste ↥ halten).
- **Driften:** Leertaste/Bremse halten und dabei lenken, wenn du schnell genug bist – mit Reifenquietschen und Rauch.
- **Gangschaltung:** Während der Fahrt mit **Q** schalten (Handy: Zahl-Taste über der Bremse). Roller 3 Gänge, E-Moped 4. Niedrige Gänge ziehen stärker, für die Höchstgeschwindigkeit musst du hochschalten; beim Runterschalten bremst der Motor. Zu Fuß wechselt Q weiterhin die Waffe.
- **2 Werkstätten** (W auf der Minikarte): Mit **F** das Rolltor öffnen – mit Sternen geht das nicht. Mit dem Roller reinfahren, dann öffnet sich das Tuning-Menü: 3 Upgrades (400 $, 900 $, 1.600 $), sie machen den Roller schneller (**39 → 43 → 47 → 50 km/h**).
- **Autohaus** (A auf der Minikarte): Nach allen 3 Upgrades gibt es dort das **E-Moped für 5.000 $** – noch schneller (70 km/h), stabiler bei Crashs und Rammstößen. Upgrades und Moped bleiben im Browser gespeichert.
- **3 Dealer** (grünes $ auf der Minikarte): Zu Fuß hingehen und E drücken → Munition für eine Waffe deiner Wahl nachfüllen, neue Waffen, Schutzweste und Erste Hilfe kaufen. Solange du gesucht wirst, handeln sie nicht.

## Starten

`index.html` einfach im Browser öffnen (Doppelklick reicht) – oder lokal ausliefern:

```bash
python3 -m http.server 8000   # dann http://localhost:8000 öffnen
```

## Handy / Tablet

Das Spiel erkennt Touch automatisch. Handy quer halten:

- **Linker Daumen:** Stick zum Fahren/Laufen (der Roller fährt in die Richtung, in die du ziehst)
- **Rechter Daumen:** Stick zum Zielen – weit ziehen = schießen
- **⇅** auf-/absteigen · **⟳** Waffe wechseln · **■** Bremse · **II** Pause

## Steuerung (PC)

| Taste | Aktion |
|---|---|
| W / ↑ | Gas geben (Roller) / nach oben laufen |
| S / ↓ | Bremsen, rückwärts / nach unten laufen |
| A D / ← → | Lenken / seitlich laufen |
| Leertaste | Vollbremsung |
| E | Auf den Roller auf- / absteigen |
| Maus | Zielen |
| Linke Maustaste | Schießen – zu Fuß **und** auf dem Roller |
| 1–6, Mausrad, Q | Waffe wechseln |
| P / Esc | Pause |
| M | Ton an/aus |

## Spielmechanik

- **Streifenwagen** spawnen ab und zu in der Nähe. Sehen sie dich auf dem Roller oder mit gezogener Waffe,
  bekommst du ★ und sie verfolgen dich.
- **Fahndungslevel ★–★★★★★**
  - ★ Schüsse in Hörweite der Polizei / Anwohner rufen die Polizei / auf dem Roller erwischt
  - ★★ Polizei angegriffen – ab jetzt wird zurückgeschossen
  - ★★★+ jeder zerstörte Streifenwagen erhöht das Level
  - ★★★★ Polizeihubschrauber mit Suchscheinwerfer
  - Mehr Sterne = mehr und schnellere Polizeiautos
- **Entkommen:** Sichtkontakt brechen (Gebäude dazwischen) und den Suchradius verlassen
  (Kreis auf der Minikarte). Blinkende Sterne = die Polizei sucht dich nur noch.
- **Waffen** (Pistole, Uzi, Schrotflinte, Sturmgewehr, Raketenwerfer) sowie Gesundheit und
  Schutzwesten liegen verteilt auf Gehwegen und in Parks. Aufheben geht nur zu Fuß – also absteigen!
- **Rammen:** Polizeiautos können dich vom Roller stoßen.
- **BUSTED:** Bleibst du bei bis zu 3 Sternen stehen, während ein Polizist neben dir hält,
  wirst du festgenommen (Waffen weg, Neustart an der Polizeiwache).
- **WASTED:** Gesundheit auf 0 → Neustart am Krankenhaus.

## Großstadt (3D-Version)

- **Umzug:** Mit E-Moped und 10.000 $ zur Autobahn-Auffahrt ganz im Osten der Kleinstadt (→ auf der Minikarte) und E drücken.
  Unterwegs stoppt dich die Polizei: Moped und Geld werden beschlagnahmt, du kommst in Haft und wirst in der Großstadt entlassen.
- **Neustart ohne alles:** kein Geld, keine Fahrzeuge, keine Waffen auf den Straßen (nur Gesundheit und Westen).
- **Automaten** (€ auf der Karte): E drücken und stehen bleiben. Snackautomaten 35–90 $, Geldautomaten 120–260 $; manchmal gibt es stillen Alarm (1 Stern). Danach sind sie 3 Minuten leer.
- **Verkehr:** NPC-Autos fahren rechts, halten an roten Ampeln, hinter anderen Autos und vor Fußgängern und hupen, wenn du im Weg stehst. Man kann sie abschießen (1 Stern).
- **Downtown:** Hochhausviertel in der Stadtmitte mit deiner **Wohnung** (⌂). Rein kommst du nur zu Fuß und ohne Sterne. Drinnen gehst du langsamer,
  lagerst Waffen im **Tresor** (mitgenommene Waffen sind nach Tod/Festnahme weg) und wählst am **Schlüsselbrett** dein Fahrzeug.
- **Scooter-Laden** (S): Stadtflitzer (250 $), Sprinter (700 $), Blitz X (1.500 $). Mit allen drei gibt es das **E-Moped** (5.000 $).
- **Werkstatt** (W): Roller-Upgrades, +2 km/h je Stufe (max. 50 km/h).
- **Autohaus** (A): Sportwagen (15.000 $, 5 Gänge) – erst nach dem E-Moped.
- **Tune-Shop** (T): Lackierung, Spoiler, Goldfelgen, Motor (+10 km/h je Stufe bis 120 km/h), Panzerung.
- „Spielstand zurücksetzen“ auf dem Startbildschirm bringt dich zurück in die Kleinstadt.

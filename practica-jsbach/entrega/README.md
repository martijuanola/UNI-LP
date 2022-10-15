# Doble interpret de JSBach

Aquest doble interpret permet interpretar codi i generar notació músical.

## Programari necessari

És necessari tenir els següents programes instal·lats i disponibles des de la variable $PATH

- antlr4
- lilypond
- timidity
- ffmpeg

## Ús

```shell
# Generació de Lexers, Parsers i Visitors utilitzant antlr4
antlr4 -Dlanguage=Python3 -no-listener -visitor jsbach.g4

# Execució Genèrica
python3 jsbach.py test.jsb mainFunction

# Execució dels Tests
python3 jsbach.py test-alterations.jsb
python3 jsbach.py test-allNotes.jsb Alle_Schlüssel
python3 jsbach.py test-tempo.jsb
```

## Extensions Respecte JSBach base

- **Tempo**: S'afegeix una instrucció per canviar el tempo de reproducció de la peça musical utilitzant `<t> bpm` on `bpm` és igual a la mesura en *beats per minut* d'una negra.
- **Operacions algebràiques amb sentit utilitzant notes musicals**: S'ha escollit un mapeig de notes músicals a enter que permet operar-hi amb sentit. Cada unitat representa una distànci de semitó, d'aquesta manera té sentit que `E4+1==F4` i `F4+2==G4`.
- **Alteracions**: S'ha afegit la possibilitat d'interpetar i utilitzar notes amb alteracions, sostinguts i bemolls. Així doncs el mapeig permet que si `G4=n` després `G4#=A4b=n+1`.

## Llista d'Exepcions Considerades

- [Undef Variable]
- [Undef Procedure]
- [Main function doesn't exists]
- [Already Defined Procedure]
- [Repeted Parameter Name]
- [Not Matchin Number of Parameters]
- [Out of Bounds Index]
- [Note out of range]
- [Division by 0]

### Problemes i Possibles Extensions

- **Dificultat amb la persistència de les alteracions**: Part de l'informació de l'input de l'usuari es pot perdre, ja que el mapeig triat fa que `G4#=A4b` per exemple. Per això, a l'output s'ha pres la decisió de només tornar note reals de l'escala de do o alterades amb sostinguts. En una futura versió es podria guardar més informació per evitar aquestes ambiguetats, tot i que a l'hora de generar fitxers d'audio no suposin cap diferència.
- **Més Excepcions i Comprovacions**: Només es generen excepcions bàsiques, es podria afegir una comprovació de tipus de cara a les expressions o altre comprovacions per evitar errors en el programa.
- **Procediments amb `return`**: Una ampliació senzilla i útil seria permetre que les funcions puguin retornar valors i acabar la seva execució en trobar-se una instrucció de `return`.

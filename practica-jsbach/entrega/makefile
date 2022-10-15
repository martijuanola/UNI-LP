ANTLR = java -Xmx500M -cp "/usr/local/Cellar/antlr/4.10.1/antlr-4.10.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool

make:
	python3 jsbach.py input.jsb

allNotes:
	python3 jsbach.py test/allNotes.jsb Alle_Schlüssel

hanoi:
	python3 jsbach.py test/hanoi.jsb

helloWorld:
	python3 jsbach.py test/helloWorld.jsb

mcd:
	python3 jsbach.py test/mcd.jsb

notesHanoi:
	python3 jsbach.py test/notesHanoi.jsb Hanoi

antlr:
	$(ANTLR) -Dlanguage=Python3 -no-listener -visitor jsbach.g4

clean:
	rm -f *.pdf
	rm -f *.midi
	rm -f *.wav
	rm -f *.mp3
	rm -f *.interp
	rm -f *.tokens
	rm -f jsbachParser.*
	rm -f jsbachLexer.*
	rm -f jsbachVisitor.*
	rm -r -f -d __pycache__/

realclean:
	make clean
	rm -r -f -d JSB*
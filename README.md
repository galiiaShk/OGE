# MusiGesture
Objekt- und Gestenerkennung Projekt

1.	F�r die Funktion der Anwendung ist die Installation von anaconda https://www.anaconda.com/download/ notwendig

2.	Es wurde Python der Versionen 3.8 oder 3.9 verwendet

3.	Der Code ist �ber jupyter Notebook im anaconda Navigator implementiert und ist unter MusiGesture.ipynb aufrufbar

4.	Die ersten 5 Zellen f�hren die Installationen der Bibliotheken bzw. Module aus, wenn diese in der Umgebung noch nicht vorhanden sind

5.	Ab Zelle 6 muss der Code nach einem Neustart immer wieder ausgef�hrt werden, in der Zelle 6 werden erst alle Module importiert.

6.	Zelle 7 enth�lt den Hinweis, dass ein neuer Datensatz �ber die pickle-Datenstruktur erstellt wird. Dieser Datensatz mussim Root-Verzeichnis unter "data" hinterlegt werden, daf�r muss die vorletzte Zelle ausgef�hrt werden.

7.	Zelle 8 enth�lt den Hinweis dass eine eigene pickle-Datenstruktur zu einem Random Forest Model trainiert wird und muss daf�r die letzte Zelle ausgef�hrt werden soll.

8.	Zelle 9 empf�ngt Akkord-Applikatur als Eingabe, sucht unter den vorhandenen Akkorden (falls vorhanden) und spielt den im Ordner "chords" gespeicherten Akkord ab.

9.	Die Zelle 10 dient zur �berpr�fung der Funktionalit�t des play_chords aus Zelle 9

10.	Funktion in Zelle 11 �berpr�ft mithilfe der linearen Algebra, ob die Finger ausgestreckt sind

11.	N�chste Funktion verwenden die Ergebnisse der vorherigen, um unterschiedliche Handzeichen anhand der ausgestreckten oder zugedr�ckten Finger zuzuweisen. 

12.	In Zelle 13 befindet sich die �Main� Funktion, welche die Variablen f�r die Nebenfunktion beinhaltet, das Model aufruft und die Akkord-Applikaturen-Bezeichnungen hinterlegt. Es wird eine Video-Aufnahme f�r die erste Webcam (VideoCapture(0)) initialisiert und die Aufl�sung festgelegt. Danach wird die maximale Anzahl der H�nde festgelegt, sowie deren Verfolgungs- und Erkennungs-Konfidenz, 0.5 entsprechen dabei 50%. Wird dieser Wert zu niedrig angesetzt, dann werden unter Umst�nden die Ohren oder das Gesicht als H�nde erkannt. Ein zu hoher Wert f�r tracking-confidence lastet das System unter Umst�nden zu sehr aus. Anschlie�end wird die while-Schleife gestartet, welche auf das Erscheinen einer oder zwei H�nde wartet, falls vorhanden, aktiviert sich das Wiedergabe-Fenster. Es wird Mediapipe genutzt, um die Hilfsfunktionen mit Daten zu bef�llen. Dabei wird die die letzte im Bild erscheinende Hand als die Akkord-greifende Hand festgelegt. Ist eine andere Hand als Greifhand gew�nscht, dann muss diese kurzzeitig aus dem Bild genommen werden und wieder gezeigt werden. Danach wird die Hand umrahmt und es wird die erkannte Akkord-Applikatur dr�bergeschrieben. Um die Wiedergabe der T�ne f�r Akkorde zu aktivieren, muss mit der anderen Spielhand kurzzeitig das OK-Handzeichen gezeigt werden, dabei soll der Daumen und der Zeigefinger kr�ftig eingerollt werden, damit dazwischen kein O zu sehen ist. Nun m�ssen anhand der dargestellten Akkorde der Greifhand die Melodien abgespielt werden. F�r die Spielhand wird rechts neben der Frames-Per-Second Anzeige zus�tzlich das erkannte Handzeichen bzw. Schlagmuster ausgegeben. Um die Wiedergabe der T�ne zu beenden, muss ein Shaka-Handzeichen (Daumen und kleiner Finger sind ausgestreckt, rest eingerollt) gezeigt werden.

13.	Zelle 14 beinhaltet die nicht fertiggestellte Funktion der Erkennung von Fingerwinkel-Ver�nderung als Kommentar.

14.	Zelle 15 f�hrt Datacleaning in den Datens�tzen durch.
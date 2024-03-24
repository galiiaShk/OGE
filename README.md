# MusiGesture
Objekt- und Gestenerkennung Projekt

1.	Für die Funktion der Anwendung ist die Installation von anaconda https://www.anaconda.com/download/ notwendig

2.	Es wurde Python der Versionen 3.8 oder 3.9 verwendet

3.	Der Code ist über jupyter Notebook im anaconda Navigator implementiert und ist unter MusiGesture.ipynb aufrufbar

4.	Die ersten 5 Zellen führen die Installationen der Bibliotheken bzw. Module aus, wenn diese in der Umgebung noch nicht vorhanden sind

5.	Ab Zelle 6 muss der Code nach einem Neustart immer wieder ausgeführt werden, in der Zelle 6 werden erst alle Module importiert.

6.	Zelle 7 enthält den Hinweis, dass ein neuer Datensatz über die pickle-Datenstruktur erstellt wird. Dieser Datensatz mussim Root-Verzeichnis unter "data" hinterlegt werden, dafür muss die vorletzte Zelle ausgeführt werden.

7.	Zelle 8 enthält den Hinweis dass eine eigene pickle-Datenstruktur zu einem Random Forest Model trainiert wird und muss dafür die letzte Zelle ausgeführt werden soll.

8.	Zelle 9 empfängt Akkord-Applikatur als Eingabe, sucht unter den vorhandenen Akkorden (falls vorhanden) und spielt den im Ordner "chords" gespeicherten Akkord ab.

9.	Die Zelle 10 dient zur Überprüfung der Funktionalität des play_chords aus Zelle 9

10.	Funktion in Zelle 11 überprüft mithilfe der linearen Algebra, ob die Finger ausgestreckt sind

11.	Nächste Funktion verwenden die Ergebnisse der vorherigen, um unterschiedliche Handzeichen anhand der ausgestreckten oder zugedrückten Finger zuzuweisen. 

12.	In Zelle 13 befindet sich die „Main“ Funktion, welche die Variablen für die Nebenfunktion beinhaltet, das Model aufruft und die Akkord-Applikaturen-Bezeichnungen hinterlegt. Es wird eine Video-Aufnahme für die erste Webcam (VideoCapture(0)) initialisiert und die Auflösung festgelegt. Danach wird die maximale Anzahl der Hände festgelegt, sowie deren Verfolgungs- und Erkennungs-Konfidenz, 0.5 entsprechen dabei 50%. Wird dieser Wert zu niedrig angesetzt, dann werden unter Umständen die Ohren oder das Gesicht als Hände erkannt. Ein zu hoher Wert für tracking-confidence lastet das System unter Umständen zu sehr aus. Anschließend wird die while-Schleife gestartet, welche auf das Erscheinen einer oder zwei Hände wartet, falls vorhanden, aktiviert sich das Wiedergabe-Fenster. Es wird Mediapipe genutzt, um die Hilfsfunktionen mit Daten zu befüllen. Dabei wird die die letzte im Bild erscheinende Hand als die Akkord-greifende Hand festgelegt. Ist eine andere Hand als Greifhand gewünscht, dann muss diese kurzzeitig aus dem Bild genommen werden und wieder gezeigt werden. Danach wird die Hand umrahmt und es wird die erkannte Akkord-Applikatur drübergeschrieben. Um die Wiedergabe der Töne für Akkorde zu aktivieren, muss mit der anderen Spielhand kurzzeitig das OK-Handzeichen gezeigt werden, dabei soll der Daumen und der Zeigefinger kräftig eingerollt werden, damit dazwischen kein O zu sehen ist. Nun müssen anhand der dargestellten Akkorde der Greifhand die Melodien abgespielt werden. Für die Spielhand wird rechts neben der Frames-Per-Second Anzeige zusätzlich das erkannte Handzeichen bzw. Schlagmuster ausgegeben. Um die Wiedergabe der Töne zu beenden, muss ein Shaka-Handzeichen (Daumen und kleiner Finger sind ausgestreckt, rest eingerollt) gezeigt werden.

13.	Zelle 14 beinhaltet die nicht fertiggestellte Funktion der Erkennung von Fingerwinkel-Veränderung als Kommentar.

14.	Zelle 15 führt Datacleaning in den Datensätzen durch.
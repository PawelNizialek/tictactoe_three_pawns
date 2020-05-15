# Tic Tac Toe with three pawns
* https://github.com/pawel850m/tictactoe_three_pawns
#Opis
* Gra umożliwia rozgrywkę jednego gracza z komputerem w kółko i krzyżyk z modyfikacją.
* Modyfikacja polega na dopuszczeniu maksymalnie 3 pionków gracza oraz 3 pionków komputera w grze (razem 6 pionków) - 
zamiast tradycyjnego modelu, w którym gra kończy się gdy nie ma już dostępnych wolnych pól
* Z tego względu po osiągnięciu liczby 3 pionków przez każdą ze stron możliwe jest przenoszenie pionków na inne pola.
* Gra rozpoczyna się od wybrania poziomu trudności, podania imienia oraz wyboru kształtu przez gracza (X lub O)
* Następnie pierwszy ruch należy do gracza.
* Po ruchu gracza komputer musi właściwie zareagować niedopuszczając do wygranej gracza ale także sprawiając że może wygrać
* W pierwszym etapie gry (gdy na planszy są 2 lub mniej pionków każdego z graczy) komputer oblicza odpowiedni ruch
zakładając że dostępna jest skończona liczba ruchów, ponieważ nie jest możliwe przesuwanie pionków po planszy.
* Przesuwanie pionków w pierwszym etapie nie jest możliwe ze względu na to że jest to nieopłacalne dla każdej ze stron i 
skutkuje w najlepszym wypadku oddaniem pierwszeństwa ruchu przeciwnikowi.
* W późniejszym etapie, gdy na planszy jest 3 lub więcej pionków każdego z graczy występuje nieskończona liczba ruchów do rozważenia przez komputer 
(zawsze znajdzie się taki pionek który komputer może przenieść, ale i każdy pionek gracza może zostać przeniesiony).
* Gdyby ilość ruchów była skończona, komputer nie uwzględniałby ruchów w których gracz 
przesuwa pionki z jednego miejsca na inne. Również to komputer nie miałby takiej szansy. Dlategoteż do późniejszego etapu rozgrywki niezbędny jest dodatkowy algorytm, który daje określony czas komputerowi na
ruch. Po zadanym czasie komputer musi wykonać ruch bez względu na to czy jest to najlepszy ruch jaki może wykonać.
* Przy stosowaniu algorytmu konieczym jest aby zapamiętane zostało zarówno położenie najlepszego możliwego ruchu jak i najlepszego 'usunięcia'
pionka z danej pozycji.
* Zadany czas determinuje więc poziom trudności rogrywki. Jeżeli będzie stosunkowo bardzo krótki komputer może nie mieć 
wystarczająco dużo czasu aby móc wyznaczyć najlepszy z możliwych ruchów. Wtedy możliwa będzie wygrana gracza.
* Po zakończeniu rozgrywki (wygrana jednej ze stron) wyświetlane jest imie gracza jeżeli wygrał oraz gra umożliwia
rozpoczęcie rozgywki od nowa, przy czym czyszczona jest plansza, możliwy jest ponowny wybór kształtu, podanie imienia 
oraz wybor poziomu trudnosci.
* Do rysowania planszy służącej do rogrywki zastosowana została biblioteka tkinter.

#Testy
* Gra uniemożliwia wybór kształtu innego niż X lub O  
* Gra umożliwia wybór poziomu trudności - tak aby była 
możliwość zwycięstwa gracza.
* W pierwszym etapie gry (gdy na planszy jest do 2 pionków każdej ze stron) gra uniemożliwia usunięcie z pola zarówno
pionka komputera jak i gracza
* W drugim etapie gra uniemożliwia usunięcie pionka komputera i dodanie pionka gracza (2 pionki komputera i 4 
pionki gracza w grze)
* Gracz nie może również usunąć dwóch swoich pionków.
* Gra uniemożliwia dodanie do planszy 4. pionka przez gracza pomijając usunięcie.
* Nie można przenieść pionka na pole należące do komputera.
* Komputer nie może usunąć pionka należącego do gracza ani ustawić pionka na polu gracza.
* Gra uwzględnia wszystkie możliwości wygranej zarówno po stronie gracza jak i komputera (pion, poziom, ukos) 
i odpowiednio to sygnalizuje.
* Po zakończonej rozgrywce możliwe jest ponowne rozpoczęcie nowej z wymazaną planszą bez zamykania programu; możliwy ponowny wybór poziomu trudności,
kształtu oraz napisanie imienia. 

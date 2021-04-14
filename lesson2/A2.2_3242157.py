rootQuestion = input("Funktioniert das System?: ");

if(rootQuestion.lower() == "ja"):
    print("Fummel nicht daran herum!");
    print("Alles ist gut");
else:
    responsibilityQuestion = input("Bist du Schuld?: ");

    if(responsibilityQuestion.lower() == "nein"):
        print("Dich trifft es nicht");
    else:
        print("Du Idiot !");

        didSomeoneRealiseQuestion = input("Hat es jemand gemerkt?: ");

        if(didSomeoneRealiseQuestion.lower() == "nein"):
            print("Man wird dich nie finden");
        else:
            print("Du bist am Arsch !");

            canSomeoneElseBeResponsibleQuestion = input("Kannst du einem Anderen die Schuld zuschieben?: ");

            if(canSomeoneElseBeResponsibleQuestion.lower() == "ja"):
                print("Keine Sorge, jemand anderes ist im Arsch");
            else:
                print("Du bist wirklich am Arsch!!");
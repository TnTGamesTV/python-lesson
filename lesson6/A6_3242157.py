from pathlib import Path

local_path = Path(__file__).parent.absolute();

def read_data():
    data = [];

    with open(local_path.joinpath('Konto.txt'), 'r', 512, 'utf-8') as f:
        content = f.read();

        members = content.splitlines();

        for member in members:
            member_data = member.split(",");

            data.append([int(member_data[0]), member_data[1].strip(), float(member_data[2])]);

    return data;

def write_data(data):
    total_output = "";

    for member_data in data:
        member = str(member_data[0]) + "," + member_data[1] + "," + str(member_data[2]);

        total_output += member + "\n";

    with open(local_path.joinpath('Konto.txt'), 'w', 512, 'utf-8') as f:
        f.write(total_output);

def change_amount(data, index, to_change):
    current_amount = get_amount(data, index);

    current_amount += to_change;

    try:
        member_data = [x for x in data if x[0] == index][0];
    except:
        print("Bitte wählen Sie ein vorhandenes Konto aus");
        exit();

    member_data[2] = current_amount;

    return data;

def get_amount(data, index):
    try:
        member_data = [x for x in data if x[0] == index][0];
    except:
        print("Bitte wählen Sie ein vorhandenes Konto aus");
        exit();

    return member_data[2];

print("Was möchten Sie tun ?");
print(" [1] Kontostand anzeigen");
print(" [2] Einzahlen");
print(" [3] Auszahlen");

mode = int(input(" Ihre Eingabe: "));

if mode == 0:
    exit();

data = read_data();

print("Welches Konto möchten Sie verwenden ?");

for member_data in data:
    print(" [{}] {}".format(member_data[0], member_data[1]));

print(" [0] Ende");
index = int(input(" Ihre Eingabe: "));

if index == 0:
    exit();

if mode == 1:
    amount = get_amount(data, index);

    print("Kontostand: {}€".format(amount));

if mode == 2 or mode == 3:
    if mode == 2: to_change = float(input("Einzahlung: "));
    if mode == 3: to_change = float(input("Auszahlung: ")) * -1;

    data = change_amount(data, index, to_change);

    if mode == 2: print("Es wurden {}€ eingezahlt".format(to_change));
    if mode == 3: print("Es wurden {}€ ausgezahlt".format(to_change * -1));

    new_amount = get_amount(data, index);

    print("Neuer Kontostand: {}€".format(new_amount));

write_data(data);
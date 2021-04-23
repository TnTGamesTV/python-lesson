from math import ceil

def calc_parking_costs(hours):
    return hours * 1.5;

def calc_parking_costs_detailed(hours):
    if hours <= 8:
        total = 0;

        if hours > 0: 
            total += 2;
            hours -= 1;
        
        if hours > 0:
            total += 1.5;
            hours -= 1;

        if hours > 0:
            total += hours * 1;

        return total;
    else:
        # the parking time is "a day or more"
        return ceil(hours / 24) * 10;

def is_coin_or_note(money):
    correct_values = [.1,.2,.5,1,2,5,10,20,50];

    return money in correct_values;

def calc_returned_coins_and_notes(money):
    correct_values = [.1,.2,.5,1,2,5,10,20,50];
    correct_values.sort(reverse=True);

    returned_values = {};

    for correct_value in correct_values:
        while money >= correct_value:
            money -= correct_value;
            if not correct_value in returned_values.keys():
                returned_values[correct_value] = 1;
            else:
                returned_values[correct_value] += 1;

    return returned_values;

def output_returned_money(returned_values: dict):
    for money_value, amount in returned_values.items():
        print("Sie bekommen {}x {} EUR.".format(amount, money_value));


hours = ceil(float(input("Geparkte Stunden: ")));

current_cost = calc_parking_costs_detailed(hours);

print("Es werden {} Euro fällig".format(current_cost));

total_paid = 0;
total_return = 0;
while current_cost > total_paid:
    paid_money_input = input("Wieviel zahlen Sie ein: ");

    try:
        paid_money = float(paid_money_input);

        total_paid += paid_money;

        if current_cost > total_paid:
            print("Sie müssen noch {} EUR bezahlen.".format(current_cost));
        else:
            total_return = total_paid - current_cost;
            break;
    except:
        print("Vorgang abgebrochen.");
        total_return = total_paid;

if total_return > 0:
    returned_values = calc_returned_coins_and_notes(total_return);
    output_returned_money(returned_values);

print("Vielen Dank und auf Wiedersehen");

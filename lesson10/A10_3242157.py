from pathlib import Path
import numpy as np
import pandas as pd

local_path = Path(__file__).parent.absolute();

global_frame = pd.read_csv(local_path.joinpath("baustelleneinsatz.csv"), sep=",", thousands=".", decimal=",", encoding="utf-8", header=0);

sum_frame = global_frame.groupby('Qualifikation', as_index=False).sum();
min_frame = global_frame.sort_values('Einsatzkosten').head(1);
max_frame = global_frame.sort_values('Einsatzkosten', ascending=False);
total_frame = global_frame.sum();

min_entry = ["min. Einzelposten: " + min_frame.iloc[0, 3], min_frame.iloc[0, 8]];
max_entry = ["max. Einzelposten: " + max_frame.iloc[0, 3], max_frame.iloc[0, 8]];
total_entry = ['Gesamt', total_frame['Einsatzkosten']];

sum_frame = sum_frame.rename(columns={
    "Qualifikation": "Posten",
    "Einsatzkosten": "Kosten",
})[['Posten', 'Kosten']]

next_index = sum_frame.count(axis=0).Kosten;

sum_frame = sum_frame.append(pd.DataFrame({'Posten': min_entry[0], 'Kosten': min_entry[1]}, index=[next_index]))
sum_frame = sum_frame.append(pd.DataFrame({'Posten': max_entry[0], 'Kosten': max_entry[1]}, index=[next_index + 1]))
sum_frame = sum_frame.append(pd.DataFrame({'Posten': total_entry[0], 'Kosten': total_entry[1]}, index=[next_index + 2]))

sum_frame.to_csv(local_path.joinpath("out.csv"))
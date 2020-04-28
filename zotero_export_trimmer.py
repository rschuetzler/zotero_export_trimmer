import csv
import datetime

LAST_RUN_FILE = "lastrun.txt"

# original_fields = [
#     "Title",
#     "Author",
#     "Item Type",
#     "Publication Year",
#     "Publication Title",
#     "Date Added",
#     "Conference Name",
#     "Key",
# ]

new_fields = [
    "Title",
    "Authors",
    "Type",
    "Year",
    "Publication",
    "Date Added",
    "Manual Tags",
    "Key",
]


def get_last_run(file):

    dateformat = "%Y-%m-%d %H:%M"

    try:
        with open(file, "r") as checkpoint:
            last_run_str = checkpoint.readline()
            last_run_datetime = datetime.datetime.strptime(last_run_str, dateformat)
    except FileNotFoundError:
        last_run_datetime = datetime.datetime(1900, 1, 1, 0, 0)

    with open(file, "w") as checkpoint:
        checkpoint.write(f"{datetime.datetime.now().strftime(dateformat)}")

    return last_run_datetime


with open("library.csv", encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    last_run = get_last_run(LAST_RUN_FILE)
    with open("zot.csv", "w") as outfile:
        writer = csv.DictWriter(outfile, new_fields, extrasaction="ignore")
        writer.writeheader()
        for row in reader:
            if row["Publication Title"] == "":
                row["Publication"] = row["Conference Name"]
            else:
                row["Publication"] = row["Publication Title"]
            row["Authors"] = row["Author"]
            row["Year"] = row["Publication Year"]
            row["Type"] = row["Item Type"]
            # Date added: 2019-05-17 19:30:51
            date_added = datetime.datetime.strptime(
                row["Date Added"], "%Y-%m-%d %H:%M:%S"
            )
            if date_added > last_run:
                writer.writerow(row)

get_last_run(LAST_RUN_FILE)

from glob import glob
import csv
import db
import config

# main function, handles a file and inserts it to its collection
def etl(collection_name, filename):
    with open(filename, newline='',encoding='utf-8-sig') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',')
        # read line by line because files can be big
        for row in csv_reader:
            # insert to db
            db.insert(collection_name,row)

def main():
    print('[.] Loading files...')

    for filename in glob('files/*Patient.csv'):
        print(f'[.] Loading file {filename}...')
        try:
            etl(config.PATIENTS_COLLECTION_NAME,filename)
            print(f'[V]  Finished loading file {filename}...')
        except Exception as ex:
            print(f'[X]  Error loading file {filename}...')
            print(str(ex))
    
    for filename in glob('files/*Treatment.csv'):
        print(f'[.] Loading file {filename}...')
        try:
            etl(config.TREATMENTS_COLLECTION_NAME,filename)
            print(f'[V]  Finished loading file {filename}...')
        except Exception as ex:
            print(f'[X]  Error loading file {filename}...')
            print(str(ex))

    print('[V] Finished loading files.')
    return 0 

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)

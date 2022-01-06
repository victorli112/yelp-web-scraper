from openpyxl import load_workbook
from datetime import date

cities = {
    'NewYorkCity' : 'NY',
    'LosAngeles' : 'CA',
    'Chicago' : 'IL',
    'Houston' : 'TX',
    'Phoenix' : 'AZ',
    'Philadelphia': 'PA',
    'SanAntonio' : 'TX',
    'SanDiego' : 'CA',
    'Dallas' : 'TX',
    'Austin' : 'TX',
    'SanJose' : 'CA',
    'FortWorth' : 'TX',
    'Jacksonville' : 'FL',
    'Columbus' : 'OH',
    'Charlotte' : 'NC',
    'Indianapolis' : 'IN',
    'SanFrancisco' : 'CA',
    'Seattle' : 'WA',
    'Denver' : 'CO',
    'Washington' : 'DC',
    'Boston' : 'MA',
    'ElPaso' : 'TX',
    'Nashville' : 'TN',
    'OklahomaCity' : 'OK',
    'LasVegas' : 'NV',
    'Detroit' : 'MI',
    'Portland' : 'OR',
    'Memphis' : 'TN',
    'Louisville' : 'KY',
    'Milwaukee' : 'WI',
    'Baltimore' : 'MD',
    'Albuquerque' : 'NM',
    'Tuscon' : 'AZ',
    'Mesa' : 'AZ',
    'Fresno' : 'CA',
    'Sacramento' : 'CA',
    'Atlanta' : 'GA',
    'KansasCity' : 'MO',
    'ColoradoSprings' : 'CO',
    'Raleigh' : 'NC',
    'Omaha' : 'NE',
    'Miami' : 'FL',
    'LongBeach' : 'CA',
    'VirginiaBeach' : 'VA',
    'Oakland' : 'CA',
    'Minneapolis' : 'MN',
    'Tampa' : 'FL',
    'Tulsa' : 'OK',
    'Arlington' : 'TX',
    'Wichita' : 'KS'}

numbers = range(0,50)
numbers_as_str = list(map(str, numbers))

# prints the date and writes the date and the city data to the excel document
def write_to_excel(excel_name, file_name, column):
    today = date.today()
    written_date = today.strftime("%B_%d_%Y")
    #written_date = "December_28_2021"
    print("Date = ", written_date)

    with open(file_name) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    # load the sheet
    wb = load_workbook(excel_name)

    # initialize counter
    total_states_written = 1;

    for line in lines:
        if line != ' ':
            first_word = line.split(' ')[0]
        if first_word in cities.keys():
            city = first_word + ', ' + cities[first_word]
            print(str(total_states_written) + '/50. ' + 'Currently on ' + city)
            
            if excel_name == 'employees_vaccinated.xlsx':
                sheet = wb[city]
            else:
                sheet = wb[first_word]

            #set the date to todays date
            sheet[column + str(1)] = written_date

            #set the counter to iterate down excel column
            current_row = 2

            #increase written counter
            total_states_written = total_states_written + 1

        # if the first word is a restaurant
        elif first_word not in numbers_as_str:
            cell = column + str(current_row)
            sheet[cell] = first_word
            current_row = current_row + 1

    #save the sheet
    try:
        wb.save(excel_name)
        print(excel_name + ' saved. Exiting now.')
    except:
        print('Failed to save.')


# vaccine_required
# employees_vaccinated

# first argument is the specified excel document, second argument is the data where it's coming from, 
# third argument is the column of where the data should be written
write_to_excel('vaccine_required.xlsx', 'data.txt', 'EQ')
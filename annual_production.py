import matplotlib.pyplot as plt
import pandas as pd
import re

# Define some functions which named by their usage.
def process_data_to_list(data):
    text_list = []
    for i in data:
        text_list.extend(re.split(r'; | |;', str(i).upper()))
    return text_list

def count_year(data):
    count_dict = {}
    for i in data:
        try:
            count_dict[int(float(i))] += 1
        except KeyError:
            count_dict[int(float(i))] = 1
        except ValueError:
            continue

    return count_dict

def select_math_edu_journal(source_df):
    import numpy as np
    import pandas as pd
    data_df = pd.DataFrame(np.zeros(68).reshape(1, 68))
    data_df.columns = source_df.columns
    data_df = data_df.drop([0, ])

    for index, row in source_df.iterrows():
        title = row['Source Title']
        if 'education'.upper() in title or 'learning'.upper() in title:
            if 'mathematics'.upper() in title:
                data_df = data_df.append(row)
            elif 'science'.upper() in title:
                if 'life science'.upper() not in title and 'theory & practice'.upper() not in title:
                    data_df = data_df.append(row)
            else:
                if 'engineering education'.upper() in title:
                    data_df = data_df.append(row)
    data_df = data_df.reset_index()
    return data_df

def select_other_journal(source_df):
    import numpy as np
    import pandas as pd
    data_df = pd.DataFrame(np.zeros(68).reshape(1, 68))
    data_df.columns = source_df.columns
    data_df = data_df.drop([0])

    for index, row in source_df.iterrows():
        title = row['Source Title']
        if 'education'.upper() not in title and'learning'.upper() not in title:
            data_df = data_df.append(row)
        elif 'mathematics'.upper() not in title and 'science'.upper() not in title and 'engineering education'.upper() not in title:
            data_df = data_df.append(row)
        elif 'life science'.upper() in title or 'theory & practice'.upper() in title:
            data_df.append(row)

    data_df = data_df.reset_index()
    return data_df

# Read the data.
source_df = pd.read_csv('C:/Users/user/python-workspace/ssciMathematicsAffect.csv')

# Process the data.
year_data_list = process_data_to_list(source_df['Publication Year'])
year_count_dict = count_year(year_data_list)
year_list = list(range(min(year_count_dict.keys()), max(year_count_dict.keys())+1))
all_count_list = []

for i in year_list:
    try:
        all_count_list.append(year_count_dict[i])
    except:
        all_count_list.append(0)

# Process math&sci edu data.
math_sci_edu_df = select_math_edu_journal(source_df)
year_data_list = process_data_to_list(math_sci_edu_df['Publication Year'])
year_count_dict = count_year(year_data_list)
math_sci_edu_count_list = []

for i in year_list:
    try:
        math_sci_edu_count_list.append(year_count_dict[i])
    except:
        math_sci_edu_count_list.append(0)

# Process others data.
others_df = select_other_journal(source_df)
year_data_list = process_data_to_list(others_df['Publication Year'])
year_count_dict = count_year(year_data_list)
year_list = list(range(min(year_count_dict.keys()), max(year_count_dict.keys())+1))
others_count_list = []

for i in year_list:
    try:
        others_count_list.append(year_count_dict[i])
    except:
        others_count_list.append(0)


# Draw the figure.
plt.plot(year_list, all_count_list, label='All')
plt.plot(year_list, math_sci_edu_count_list, label='Math&Sci Edu')
plt.plot(year_list, others_count_list, label='Others')
plt.title('Publication of Each Year')
plt.xlabel('Y.ear')
plt.ylabel('Publication')
plt.xticks(list(year for year in year_list if year % 2 == 0))
plt.yticks(list(range(0, 190, 10)))
plt.grid(True)
plt.legend()

# Set the size of the figure.
fig = plt.gcf()
fig.set_size_inches(15, 6)

# Show the figure and save it.
plt.tight_layout() # This statement is used to make the figure won't be cut but save all the figure.
plt.savefig('C:/Users/user/python-workspace/ssciResult/all_annual_production.png')
plt.show()

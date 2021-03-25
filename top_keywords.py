# Top Keywords

import matplotlib.pyplot as plt
import pandas as pd
import re

# Read the data.
source_df = pd.read_csv('C:/Users/user/python-workspace/ssciMathematicsAffect.csv')

# Define some functions which named by their usage.
def process_data_to_list(data):
    text_list = []
    for i in data:
        text_list.extend(re.split(r'; | |;', str(i).upper()))
    return text_list

def count_word(data_text):
    useless_words_list = ['NAN', 'OF', 'AND', 'IN']
    global count_dict
    count_dict = {}
    for i in data_text:
        if i not in useless_words_list:
            try:
                count_dict[i] += 1
            except:
                count_dict[i] = 1
    count_dict['MATHEMATICS'] += count_dict['MATH'] + count_dict['MATHEMATICAL']
    count_dict['MATH'] = 0
    count_dict['MATHEMATICAL'] = 0
    count_dict['EDUCATION'] += count_dict['EDUCATIONAL']
    count_dict['EDUCATIONAL'] = 0
    count_dict['TEACHER'] += count_dict['TEACHERS']
    count_dict['TEACHERS'] = 0
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

# Process the data by functions that I defined.
all_df = source_df
math_sci_edu_df = select_math_edu_journal(source_df)
others_df = select_other_journal(source_df)

all_processed_text = process_data_to_list(all_df['Author Keywords'])
math_sci_edu_processed_text = process_data_to_list(math_sci_edu_df['Author Keywords'])
others_processed_text = process_data_to_list(others_df['Author Keywords'])

all_count_dict = count_word(all_processed_text)
math_sci_edu_count_dict = count_word(math_sci_edu_processed_text)
others_count_dict = count_word(others_processed_text)

# Tidy up the processed data.
def tidy_up(count_dict):
    name_count_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    name_list = list(i[0].upper() for i in name_count_list[0:20])
    count_list = list(i[1] for i in name_count_list[0:20])
    name_list.reverse()
    count_list.reverse()
    return name_list, count_list

# Plot it as a bar chart.
def draw_fig(name_list, count_list, title):
    plt.barh(range(20), count_list, align='center', alpha=0.5)
    plt.yticks(range(20), name_list)
    plt.grid(True)
    plt.title('Top Keywords Using Author Keywords')

    for index, value in enumerate(count_list):
        plt.text(value, index, str(value))

  # Save it.
    plt.tight_layout() # This statement is used to make the figure won't be cut but save all the figure.
    plt.savefig(f'C:/Users/user/python-workspace/ssciResult/{title}_top_keywords.png')
    plt.show()


draw_fig(tidy_up(all_count_dict)[0], tidy_up(all_count_dict)[1], 'all')
draw_fig(tidy_up(math_sci_edu_count_dict)[0], tidy_up(math_sci_edu_count_dict)[1], 'math&sci_edu')
draw_fig(tidy_up(others_count_dict)[0], tidy_up(others_count_dict)[1], 'others')
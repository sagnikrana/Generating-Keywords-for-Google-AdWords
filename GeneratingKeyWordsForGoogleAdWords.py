import pandas as pd


file_path = "D:\ProjectWork\Generating Keywords for Google AdWords\Keywords for online marketing.xlsx"

column_name1 = "Products"

column_name2 = "Keywords for the search"

#TASK 1


def remove_NaN(file_path,column_name):

    file_df = pd.read_excel(file_path)

    list1 = file_df[column_name].tolist()

    list2 = pd.isnull(list1)

    i = 0

    products_str = []

    for i in range(len(list2)):

        get_val = list2[i]

        if get_val == False:

            if i == 0:

                products_str = list1[i] + "#"

            else:

                products_str = products_str + list1[i] + "#"

    products = products_str.split("#")

    return products

i = 0

j = 0

def mix_keyword_product(keyword_list_index_max, get_product_name):

    for i in range(keyword_list_index_max):

        get_keyword_name = keyword_list[i]

        if i == 0:

            possible_phrases = get_product_name + " " + get_keyword_name + "#" + get_keyword_name + " " + get_product_name + "#"


        else:

            possible_phrases = possible_phrases + " " + get_product_name + " " + get_keyword_name + "#"

            possible_phrases = possible_phrases + " " + get_keyword_name + " " + get_product_name + "#"

    return possible_phrases


def calculate_criterion_type(keyword_list_index_max, get_product_name):
    for i in range(keyword_list_index_max):

        get_keyword_name = keyword_list[i]

        if i == 0:

            criterion_type = "Exact" + "#" + "Phrase" + "#"


        else:

            criterion_type = criterion_type + "Exact" + "#"

            criterion_type = criterion_type + "Phrase" + "#"

    return criterion_type


products = remove_NaN(file_path,column_name1)

keyword_list = remove_NaN(file_path,column_name2)


#TASK_2

products_index_max = len(products)-1

keyword_list_index_max = len(keyword_list)-1

array_max_capacity = products_index_max * keyword_list_index_max


for j in range((products_index_max)):

    productname = products[j]

    if j == 0:

        possible_phrases = mix_keyword_product(keyword_list_index_max, productname)

        criterion_type_string = calculate_criterion_type(keyword_list_index_max, productname)
    else:

        possible_phrases = possible_phrases + mix_keyword_product(keyword_list_index_max, productname)

        criterion_type_string = criterion_type_string + calculate_criterion_type(keyword_list_index_max, productname)



possible_phrases = possible_phrases.split("#")

possible_phrases.pop(-1)

criterion_type = criterion_type_string.split("#")

criterion_type.pop(-1)


i = 0

for items in possible_phrases:

    get_value = items

    get_value = get_value.strip()

    if i == 0:

        buffer_string = get_value

    else:

        buffer_string = buffer_string + "#" + get_value

    i = i+1


possible_phrases = buffer_string.split("#")

possible_phrases_df = pd.DataFrame(possible_phrases)


print(len(products))

print(len(keyword_list))

print(len(possible_phrases))


product_divisor = len(possible_phrases)/(len(products) - 1)

product_divisor = int(product_divisor)

i = 0

j = 0

k = 0

for i in range(len(products) - 1):

    for j in range(product_divisor):

        get_val = products[i]

        if i == 0:
            #print("The value of i is "+str(i)+" and the value of iterator is "+get_val)

            if(k>0):

                combined_string = combined_string + get_val + "#"

                campaign_string = campaign_string + "Campaign1" + "#"

            else:

                combined_string = get_val + "#"

                campaign_string = "Campaign1" + "#"
            k = k + 1

        else:

            combined_string = combined_string + get_val + "#"

            campaign_string = campaign_string + "Campaign1" + "#"


combined_string = combined_string.split("#")

campaign_list = campaign_string.split("#")

combined_string.pop(-1)

final_df = pd.DataFrame(list(zip(campaign_list,combined_string, possible_phrases,criterion_type)),columns=['Campaign','Products','Possible Keywords','Criterion Type'])

print(final_df)

# def generate_list(product_divisor,j):
#
#     for i in range(product_divisor - 1):
#
#         get_val = products[j]
#
#         if i == 0:
#
#             combined_string = get_val + "#"
#
#         else:
#
#             combined_string = combined_string + get_val + "#"
#
#     return combined_string
#
#
#
# for j in range(len(products) - 1):
#
#     get_val = generate_list(product_divisor,j)
#
#     if i == 0:
#
#         final_string = get_val + "#"
#
#     else:
#
#         final_string = final_string + get_val + "#"
#
# print(final_string)
#
# final_string = final_string.split("#")
#
# print(len(final_string))
#
# print(final_string)

# #print(possible_phrases_df.head())
#
# #possible_phrases_df.rename({"0":'Phrases'}, axis='columns')
#
# possible_phrases_df = possible_phrases_df.rename(columns={'':'name1',0: 'newName1'})
#
# #possible_phrases_df.columns.values[2] = 'b'
# print(len(products),len(keyword_list),len(possible_phrases))
#
# final_df = pd.DataFrame(list(zip(products, keyword_list, possible_phrases)),columns=['Products','Keywords','Possible Keywords'])
#
# print(final_df)
# # print(type(products))
# # print(type(possible_phrases))
# # print(type(keyword_list))
# #Changing the above list into DataFrame
#
# #possible_phrases_df = pd.DataFrame(possible_phrases)
#
# #possible_phrases_df.ee==rena
#
# #print(possible_phrases_df.head())
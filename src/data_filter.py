# -*- coding=utf-8 -*-
import config
import json

def get_text_from_file(path):
    """ get the pure chinese line from file

    Parameters:
    -----------
    path: the data path in the system.

    Return:
    -------
    texts: format: [["aa bb cc"],["a  sd  d"]..  ]
           all the character here is Chinese
    """
    texts = []
    with open(path) as file_ob:
        for line in file_ob:
            line_json = json.loads(line) # string to json
            # from unicode to str
            word_with_property = line_json.get("text").encode("utf-8")
            words = word_with_property.split(" ")
            # from each line we get a word_list at last
            word_list = [word.split("/")[0] for word in words]
            texts.append(' '.join(word_list))

    return texts



def write_to_file(data, file_name):
    """ write the data to the file

    Parameters:
    -----------
    data: just the data, always is a LIST
    file_name: contain file_path and file_name exactly,
               for example: "../data/chinese_data.txt"

    Returns:
    --------
    None

    """
    with open(file_name, 'w') as file_ob:
        for data_line in data:
            file_ob.write(data_line + "\n")
    file_ob.close()
    return

def main():
    """ the main function

    """
    texts = get_text_from_file(config.frozen_data_path)
    write_file_path = "../data/chinese_data.txt"
    write_to_file(texts, write_file_path)

    return

if __name__ == "__main__":
    main()

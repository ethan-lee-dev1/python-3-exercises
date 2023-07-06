from pprint import pprint
import os
def create_files(file_path):
    # unique_words = set()
    # with open(input_file, "r") as file:
    #     content = file.read()
    #     words = content.split()
    #     for word in words:
    #         unique_words.add(word)
    #
    # count = 0
    # for word in unique_words:
    #     if len(word) < 3:
    #         with open("small-words.txt", "a") as small_file:
    #             count += 1
    #             small_file.write(word + "\n")
    #     else:
    #         with open("large-words.txt", "a") as large_file:
    #             count += 1
    #             large_file.write(word + "\n")
    #
    # return count

    folder_path = os.path.dirname(file_path)
    small_words_file = os.path.join(folder_path, "small-words.txt")
    large_words_file = os.path.join(folder_path, "large-words.txt")

    small_words = set()
    large_words = set()

    with open(file_path, 'r') as file:
        words = file.read().split()

        for word in words:
            if len(word) < 3:
                small_words.add(word)
            else:
                large_words.add(word)

    with open(small_words_file, 'w') as file:
        file.write("\n".join(small_words))

    with open(large_words_file, 'w') as file:
        file.write("\n".join(large_words))

    return len(small_words) + len(large_words)

def ex3():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "../files/words.txt")

    total_words = create_files(file_path)
    print(f"Total words: {total_words}.")

ex3()
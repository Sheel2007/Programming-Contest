def calculate(num_words, text):

    for i in range(num_words):
        if text[i] == "Bing":
            text[i] = "Bong"
        elif text[i] == "bing":
            text[i] = "bong"
        elif text[i] == "BING":
            text[i] = "BONG"

    return text


test_cases = int(input())

for _ in range(test_cases):
    text = input().split()
    num_words = int(text[0])

    text.pop(0)
    text = calculate(num_words, text)

    output = ""
    for word in text:
        output += word + " "

    print(output)

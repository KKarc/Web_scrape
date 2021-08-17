from playground import csv_append

lin = str(input('Provide link without page number digit: '))
nu_pages = int(input('Provide number of pages for the search result: '))


def master(link, num_pages):
    return csv_append(link, num_pages)

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    master(lin, nu_pages)

import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(URL):
    '''
    This function will return the number of citations needed
    '''
    citation_need_count = 0
    res = requests.get(URL)
    soup = BeautifulSoup(res.content, "html.parser")
    for pargrapth in soup.find("div", class_="mw-parser-output").find_all("p"):
        for citation in pargrapth.find_all("a", title="Wikipedia:Citation needed"):
            citation_need_count += 1
    print(citation_need_count)
    return citation_need_count


def get_citations_needed_report(URL):
    ''' 
    This function will return a string of the citations needed report
    '''
    new_string_list = []
    result = []
    string = ''
    res = requests.get(URL)
    sub_str = '[citation needed]'
    soup = BeautifulSoup(res.content, "html.parser")
    
    for pargrapth in soup.find("div",class_="mw-parser-output").find_all("p"):

        if sub_str in pargrapth.text:
            result += pargrapth.text.strip().split('[citation needed]')
        for stripped_line in result:
          
            cit_line = stripped_line.strip() +'[citation needed]'           
            if cit_line  in pargrapth.text.strip() and cit_line != '[citation needed]':
                if cit_line not in new_string_list:
                    new_string_list.append(cit_line)

    for line in new_string_list:
        string += f'\n{line}\n'
    print(string)
    
    return string  
            
    

if __name__ == "__main__":
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    get_citations_needed_count(URL)
    get_citations_needed_report(URL)
     
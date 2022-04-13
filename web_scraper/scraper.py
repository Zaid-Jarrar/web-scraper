from operator import indexOf
import requests
from bs4 import BeautifulSoup



URL = "https://en.wikipedia.org/wiki/History_of_Mexico"


def get_citations_needed_count(URL):
    citation_need_count = 0
    res = requests.get(URL)
    soup = BeautifulSoup(res.content, "html.parser")
    for pargrapth in soup.find("div", class_="mw-parser-output").find_all("p"):
        for citation in pargrapth.find_all("a", title="Wikipedia:Citation needed"):
            # print(citation)
            citation_need_count += 1
    print(citation_need_count)
    return citation_need_count
    
def get_citations_needed_report(URL):
    # citlist = []
    # a = []
    # result = []
    # i = 0
    res = requests.get(URL)
    sub_str = '[citation needed]'
    soup = BeautifulSoup(res.content, "html.parser")
    
    for pargrapth in soup.find("div",class_="mw-parser-output").find_all("p"):
        if sub_str in pargrapth.text:
            line = pargrapth.text.strip().split('[citation needed]')[0]+'[citation needed]'
            print(line)
    return line



if __name__ == "__main__":
    get_citations_needed_count(URL)
    get_citations_needed_report(URL)


    #         citlist.append(pargrapth.text.strip())
    #         par = pargrapth.text.strip()
    #         result.append(par[:par.index(sub_str) + len(sub_str)])

    # for line in citlist:
    #     a+=line.strip().split('[citation needed]')
    #     if a[i] +  '[citation needed]' == result[i]:
    #         print(a[i])
    #     i+=1

# def get_citations_needed_report(url):


#   response = requests.get(url)
#   soup = BeautifulSoup(response.text, 'html.parser')

#   a_tags = soup.find_all('a')
#   citations = [a for a in a_tags if 'citation needed' in a.text]
#   citation_needed = [a.find_parent('p') for a in citations]

#   output_str = ''
#   for item in citation_needed:
#     word_list = item.text.split()
#     output_str += '\n' + ' '.join(word_list)
  
#   print(output_str)
#   return output_str

# def get_citations_needed_report(URL):
#   passages = ''
#   # Next 3 lines are same as needed_count function
#   page = requests.get(URL)
#   soup = BeautifulSoup(page.content, 'html.parser')
#   titles = soup.find_all('p')
#   # Loops through found tags and appends the text if the paragraph has citation needed in it
#   for title in titles:
#     if 'citation needed' in title.text:
#       passages += title.text
#   passages = passages.replace("'\n '", ' ')
#   print(passages)
#   return passages



    # print(a)
  
    # print(citlist)
  
    # print(result)

        # for citation in pargrapth.find_all("a",title="Wikipedia:Citation needed"):
    #         citlist.append(pargrapth.text.strip())
    # print(citlist)


            # if pargrapth.text not in citlist:
            #     citlist.append(pargrapth.text.strip())


            # result+=line[:line.index(sub_str) + len(sub_str)]
     
            # result = line[:line.index(sub_str) + len(sub_str)]


            # listm += pargrapth.text.strip().split('[citation needed]')




    #         line2 = pargrapth.text.strip().split('[citation needed]')[0]+'[citation needed]'
    #         i += 1
    #         if line2 not in citlist:
    #             citlist.append(line2)
    #         print(f'\n{line2}\n')
    # print(citlist)
            # for lines in line2:
            #     lines[i]
            #     i += 0

            # if pargrapth.text.endswith("[citation needed]"):
            #     citlist.append(pargrapth.text.strip())
            # print(citlist)
            # line2 = pargrapth.text.strip().split('[citation needed]')[0]+'[citation needed]'
            # line = pargrapth.text.strip()
            # sub_str = '[citation needed]'
            # result = line[:line.index(sub_str) + len(sub_str)]

            # print(f'\n{result}\n')
            



      
            # print("-"*100)
            # citation_needed_paragraph = pargrapth.text.strip()    
            # print(f"\n{citation_needed_paragraph}")
    # return citation_needed_paragraph
    
# '''
# # Python3 code to demonstrate working of 
# # Remove after substring in String
# # Using index() + len() + slicing
  
# # initializing strings
# test_str = 'geeksforgeeks is best for geeks'
  
# # printing original string
# print("The original string is : " + str(test_str))
  
# # initializing sub string 
# sub_str = "best"
  
# # slicing off after length computation
# res = test_str[:test_str.index(sub_str) + len(sub_str)]
  
# # printing result 
# print("The string after removal : " + str(res)) 
# Output
# The original string is : geeksforgeeks is best for geeks
# The string after removal : geeksforgeeks is best '''
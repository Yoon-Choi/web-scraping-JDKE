from bs4 import BeautifulSoup
def Get_ip_user_agent(soup):
    paragraphs = soup.find_all(text=True)
    #print(type(paragraphs))
    ip = ''
    user_agent = ''
    for p in paragraphs:
        if 'python' in p:
            user_agent = p

        if 'My IP Address' in p:
            parse_result = str(p).split(": ")
            ip = parse_result[1]
    return ip, user_agent







#####################################################################
# def Get_ip_user_agent(soup):
#     paragraphs = soup.find_all(text=True)
#     #print(type(paragraphs))
#     ip = ''
#     user_agent = ''
#     for p in paragraphs:
#         if 'python' in p:
#             user_agent = p
#
#         if 'My IP Address' in p:
#             parse_result = str(p).split(": ")
#             ip = parse_result[1]
#     return ip, user_agent



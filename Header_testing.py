# Python_assignment2020
import requests

    #Part1:Request package, request testing
    #Perform a “get” request on the given website & return a status and "OK"
class header_testing:
    get_response = "OK"

    def test_header(self):
        #url= "http://172.18.58.238/headers.php"
        url = "https://www.reddit.com/r/AskReddit/comments/innw5q/how_do_you_feel_about_a_friend_with_benefits_but/"
        response_get = requests.get(url) "200 OK"
        print("---------------START OF LINE:GET REQUEST-------------")
        print(response_get,self.get_response)
        print("---------------END OF LINE:GET REQUEST---------------")
        print("\n")

        #Perform a "head" request and display the response
        header_response = requests.head(url)
        for x in header_response.headers:
            print("---------------START OF LINE: HEAD REQUEST---------------")
            print("\t", x, ":", header_response.headers[x])
            print("---------------END OF LINE:HEAD REQUEST---------------")


        #Modify User-Agent to display "Mobile"(Does't work on all URL)
        headers = {
            'User-Agent': 'Mobile'
        }

        response_get2 = requests.get(url, headers=headers)
        print("---------------START OF LINE:DISPLAY \"MOBILE\"---------------")
        print(response_get2.text)
        print("---------------END OF LINE:DISPLAY \"MOBILE\"---------------")


#YongEn_First Test
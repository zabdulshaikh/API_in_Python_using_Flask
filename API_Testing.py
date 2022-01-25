import requests

###############################
###############################
#API
def Test_API(URL):
    try:
        status_code = 0
        page = requests.get(URL) 
        status_code = page.status_code
        if status_code == 200:
            return str(URL) + ": Success"
        else:
            return str(URL) + ": Failed"
    except Exception as e: 
        return str("The testing encountered an exception error: ") + str(e)


###############################
# MAIN FUNCTION
###############################
if __name__ == "__main__":
    print ( Test_API("http://127.0.0.1:5000/")  )
    print ( Test_API("http://127.0.0.1:5000/metadata") )
    print ( Test_API("http://127.0.0.1:5000/health")    )

    #Control URL to test failure
    print ( Test_API("http://127.0.0.1:5000/metadat")   )
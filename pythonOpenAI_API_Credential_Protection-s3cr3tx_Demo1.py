import os
import requests
import logging

def print_msg(strMessage):
    logging.debug(strMessage)
    print(strMessage)
    
def main():
    try:
        # This demo works if you have the openai python module. use the s3cr3tx Python Demo #1 if you would rather use the requests library for openai API calls. 
        # Demo example without s3cr3tx Assumes you have set the OPENAI_API_KEY to store you OPENAI API Key:
        logging.debug('Start of s3cr3tx demo in python.')
        #openai.organization = os.getenv("OPENAI_API_ORG")
        openai_api_key_HEADER = "Bearer " + os.getenv("OPENAI_API_KEY")
        URL_ROOT = "https://api.openai.com/v1/models"
        request1 = requests.get(URL_ROOT,headers={"Authorization":openai_api_key_HEADER})
        openai_response = request1.text
        print_msg("response from OpenAI API call to list openai.Models without using s3cr3tx to protect the API credentials: " + str(openai_response))
        #Now we set the values of two new environment variables to the s3cr3tx encrypted versions of the OPENAI_API_ORG and OPENAI_API_KEY values to protect the values stored in the new environment variables
        #os.environ["s3cr3tx_OPENAI_API_ORG"] = setS3cr3tx(os.getenv("OPENAI_API_ORG"))
        os.environ["s3cr3tx_OPENAI_API_KEY"] = setS3cr3tx(os.getenv("OPENAI_API_KEY"))
        #Now our API_Org and API_KEY are encrypted and protected in our new s3cr3tx env vars
        #openai_api_key_HEADER = "Bearer " + getS3cr3tx(os.getenv("s3cr3tx_OPENAI_API_KEY"))
        #For this example we will print the cyphertext values of the new s3cr3tx env vars for you below:
        #print_msg("s3cr3tx ciphertext for your OPENAI_API_ORG: " + os.environ.get["s3cr3tx_OPENAI_API_ORG"])
        print_msg("s3cr3tx ciphertext for your OPENAI_API_KEY: " + os.environ.get("s3cr3tx_OPENAI_API_KEY"))
        #openai.organization = getS3cr3tx(os.getenv("s3cr3tx_OPENAI_API_ORG")) 
        request2 = requests.get(URL_ROOT,headers={"Authorization":"Bearer " + getS3cr3tx(os.getenv("s3cr3tx_OPENAI_API_KEY"))})
        openai_response_2 = request2.text
        print_msg("response from OpenAI API call to list the openai.Models after using s3cr3tx to protect the stored OpenAI API credentials: " + str(openai_response_2))
        
    except Exception as err:
        print('An error occured: ' + str(err))
def getS3cr3tx(strInput):
    try:
        strInput = str(strInput)
        #please set the following environment variables with the appropriate values s3cr3tx_Email, s3cr3tx_APIToken, s3cr3tx_AuthCode, s3cr3tx_URL for your s3cr3tx API account
        DOC_FORMAT="text/plain"
        Email_Header=os.getenv("s3cr3tx_Email")
        API_Token_Header=os.getenv("s3cr3tx_APIToken")
        Auth_Code_Header=os.getenv("s3cr3tx_AuthCode")
        #set the vakue to "d" to decrypt the secret using the s3cr3tx API
        EorD_Header="d"
        Input_Header=strInput
        URL_ROOT = os.getenv("s3cr3tx_URL")
        result3 = requests.get(URL_ROOT,headers={"Accept": DOC_FORMAT ,"Email": Email_Header,"APIToken":API_Token_Header,"AuthCode":Auth_Code_Header,"EorD":EorD_Header,"Input":Input_Header })
        s3cr3tx=result3.text
        return s3cr3tx
    except Exception as err:
        print('An error occured: ' + str(err))  
def setS3cr3tx(strInput):
    try:
        strInput = str(strInput)
        #please set the following environment variables with the appropriate values s3cr3tx_Email, s3cr3tx_APIToken, s3cr3tx_AuthCode, s3cr3tx_URL for your s3cr3tx API account
        DOC_FORMAT="text/plain"
        Email_Header=os.getenv("s3cr3tx_Email")
        API_Token_Header=os.getenv("s3cr3tx_APIToken")
        Auth_Code_Header=os.getenv("s3cr3tx_AuthCode")
        #set the vakue to "e" to encrypt the secret using the s3cr3tx API
        EorD_Header="e"
        Input_Header=strInput
        URL_ROOT = os.getenv("s3cr3tx_URL")
        result3 = requests.get(URL_ROOT,headers={"Accept": DOC_FORMAT ,"Email": Email_Header,"APIToken":API_Token_Header,"AuthCode":Auth_Code_Header,"EorD":EorD_Header,"Input":Input_Header })
        s3cr3tx=result3.text
        return s3cr3tx
    except Exception as err:
        print('An error occured: ' + str(err))       
        
def elementExists(anything):
    if anything != None:
        return True
    else:
        return False 


if __name__ == "__main__":
    main()
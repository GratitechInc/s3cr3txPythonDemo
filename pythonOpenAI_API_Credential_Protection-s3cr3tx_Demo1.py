import os
import requests
import logging

def print_msg(strMessage):
    logging.debug(strMessage)
    print(strMessage)
    
def main():
    try:
        # This demo uses the python requests module for openai API calls. 
        # Demo example without s3cr3tx Assumes you have set the OPENAI_API_KEY to store you OPENAI API Key:
        logging.debug('Start of s3cr3tx demo in python.')
        openai_api_key_HEADER = "Bearer " + os.getenv("OPENAI_API_KEY")
        URL_ROOT = "https://api.openai.com/v1/models"
        request1 = requests.get(URL_ROOT,headers={"Authorization":openai_api_key_HEADER})
        openai_response = request1.text
        print_msg("response from OpenAI API call to list openai.Models without using s3cr3tx to protect the API credentials: " + str(openai_response))
        #Now we set the value of new environment variable to hold the s3cr3tx encrypted versions of the OPENAI_API_KEY value to protect the API Key
        os.environ["s3cr3tx_OPENAI_API_KEY"] = setS3cr3tx(os.getenv("OPENAI_API_KEY"))
        #Now the API_KEY is encrypted and protected in our new s3cr3tx env var
        #openai_api_key_HEADER = "Bearer " + getS3cr3tx(os.getenv("s3cr3tx_OPENAI_API_KEY"))
        #Print the cyphertext value of the new s3cr3tx environment var below to show that the value is no longer in clear text, in prod we recommend commenting out the following line:
        print_msg("s3cr3tx ciphertext for your OPENAI_API_KEY: " + os.environ.get("s3cr3tx_OPENAI_API_KEY"))
        #Now we use the ciphertext value as input for the getS3cr3tx method in our Authorization Header value for our OPENAI API Call 
        request2 = requests.get(URL_ROOT,headers={"Authorization":"Bearer " + getS3cr3tx(os.getenv("s3cr3tx_OPENAI_API_KEY"))})
        openai_response_2 = request2.text
        #As you can see in the response from the API we have the same results and we have protected our API credentials from being stored in cleartext this time.
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
        #set the value to "d" to decrypt the secret using the s3cr3tx API
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
        #set the value to "e" to encrypt the secret using the s3cr3tx API
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

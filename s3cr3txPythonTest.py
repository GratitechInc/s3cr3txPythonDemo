import requests
import logging

def print_msg(strMessage):
    logging.debug(strMessage)
    print(strMessage)
    
def main():
    try:
        logging.debug('Start of Demonstrating s3cr3tx in python.')
        DOC_FORMAT="text/plain"
        Email_Header=os.getenv("s3cr3tx_Email")
        API_Token_Header=os.getenv("s3cr3tx_APIToken")
        Auth_Code_Header=os.getenv("s3cr3tx_AuthCode")
        EorD_Header="e"
        Input_Header="This is a secret!"
        URL_ROOT = "https://s3cr3tx.com/Values"
        result3 = requests.get(URL_ROOT,headers={"Accept": DOC_FORMAT ,"Email": Email_Header,"APIToken":API_Token_Header,"AuthCode":Auth_Code_Header,"EorD":EorD_Header,"Input":Input_Header })
        Output=result3.text
        print_msg("Your Encrypted text Output is: " + Output)
        EorD_Header="D"
        Input_Header=Output
        result4 = requests.get(URL_ROOT,headers={"Accept": DOC_FORMAT ,"Email": Email_Header,"APIToken":API_Token_Header,"AuthCode":Auth_Code_Header,"EorD":EorD_Header,"Input":Input_Header })
        Output=result4.text
        print_msg("Your Decrypted text Output is: " + Output)
    except Exception as err:
        print('An error occured: ' + str(err))
def elementExists(anything):
    if anything != None:
        return True
    else:
        return False 


if __name__ == "__main__":
    main()

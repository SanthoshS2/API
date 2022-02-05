import requests
import json
import sys

url = "https://veriphone.p.rapidapi.com/verify"
querystring = {}
headers = {
    'x-rapidapi-host': "veriphone.p.rapidapi.com",
    'x-rapidapi-key': "578b771870mshea19d8ae701033fp1db6d1jsnc270e20be7bf"
    }

def printResult(phone_number_info):
  print("Phone Number Details for ", phone_number_info["phone"])
  print("Phone Valid: ", phone_number_info["phone_valid"])
  if(phone_number_info["phone_type"]!="unknown"):
    print("Phone Type: ", phone_number_info["phone_type"])
  if(phone_number_info["phone_region"]!=""):
    print("Phone Region: ", phone_number_info["phone_region"])
  print("Phone Country: ", phone_number_info["country"])
  print("Country Prefix: ", phone_number_info["country_prefix"])
  print("International Number: ", phone_number_info["international_number"])
  if(phone_number_info["carrier"]!=""):
    print("Carrier: ", phone_number_info["carrier"])


def main():
  phone_number = sys.argv[1]
  querystring["phone"] = str(phone_number)
  response = requests.request("GET", url, headers=headers, params=querystring)
  phone_number_info = response.json()
  printResult(phone_number_info)
  

if __name__ == "__main__":
  main()

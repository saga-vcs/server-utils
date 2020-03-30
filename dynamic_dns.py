"""
Script for interacting with the Dynamic DNS for Google domains.
"""
import requests

def main():
    username = input("Dynamic DNS username: ")
    password = input("Dynamic DNS password: ")
    subdomain = input("What is the subdomain you'd like to redirect (e.g. \"testing.sagalab.org\"): ")
    ip = input("What is the IPv4 Public IP you would like to redirect to: ")

    url = f"https://{username}:{password}@domains.google.com/nic/update?hostname={subdomain}&myip={ip}"

    response = requests.post(url)
    print("\nResponse:")
    print(response.content.decode("utf-8") )




if __name__ == "__main__":
    main()
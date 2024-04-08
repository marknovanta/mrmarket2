import os
from dotenv import load_dotenv

def configure():
    load_dotenv()

def main():
    configure()
    api_key = os.getenv('api_key')



if __name__ == '__main__':
    main()
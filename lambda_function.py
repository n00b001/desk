import json

from webdriver_wrapper import WebDriverWrapper

# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = WebDriverWrapper(download_location='/tmp')

def lambda_handler(event, context):

    driver.get("https://thomsonreuters.condecosoftware.com/")

    print(driver)

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


if __name__ == '__main__':
    lambda_handler(None, None)

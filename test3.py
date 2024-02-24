import sys
import re
import requests
import subprocess
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def extract_img_list_value(url):
    # print("====> enter extract_img_list_value()")

    # fetch the HTML content
    response = requests.get(url)
    html_content = response.text
    #    print("=====> html_content: ", html_content)

    # parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # find the script tag containing img_list variable
    script_tag = soup.find('script', string=re.compile(r'var img_list = .*;'))
    #    print("================> script_tag: ", script_tag)

    if script_tag:
        #        print("======> enter script_tag")
        # extract img_list value using regular expression or other methods
        img_list_value = re.search(r'var img_list = (.*?);', script_tag.string).group(1)
        return img_list_value
    else:
        return None


def download_images(img_list_value, output_directory):
    #    print("====> download_images()")
    #    print("=====> img_list_value: ", img_list_value)
    #    print("=====> output_directory: ", output_directory)

    # Parse img_list_value as a Python list
    img_list = eval(img_list_value)
    #    print("========> img_list: ", img_list)

    # Initialize a counter for file numbering
    counter = 1

    # Construct the URLs and download the files
    for img_url in img_list:
        # Replace "//www" with "https://www"
        img_url = img_url.replace("//www", "https://www")

        # print("============> img_url: ", img_url)

        # Extract the filename from the URL
        filename = img_url.split("/")[-1]

        #        print("============> filename: ", filename)

        # Format the counter with leading zeros
        counter_str = str(counter).zfill(3)
        # print("================> counter_str: ", counter_str)

        # Construct the curl command
        #        curl_command = f"curl -O {img_url}"
        curl_command = f"curl -o {output_directory}/{counter_str}_{filename} {img_url}"

        print("============> curl_command: ", curl_command)

        # Execute the curl command using subprocess
        #        subprocess.run(curl_command, shell=True, cwd=output_directory)
        subprocess.run(curl_command, shell=True)

        #        print(f"Downloaded {filename} to {output_directory}")
        print(f"Downloaded {filename} to {output_directory} as {counter}_{filename}")

        # Increment the counter
        counter += 1


if __name__ == "__main__":
    argument = sys.argv
    if len(argument) < 3:
        print('*******************************************')
        print('check usage')
        print('python test3.py [sequence_number] [output_dir]')
        print('*******************************************')
        exit()  # 프로그램 종료

    # 맨 앞에 있는 아규먼트는 파일명이기 때문에 불필요해서 삭제함
    del argument[0]
    # print('arguments: {}'.format(argument))

    # argument1: 일련 번호
    # argument2: 저장 경로
    dynamic_wr_id = argument[0]
    output_directory = argument[1]
    # print('dynamic_wr_id: ', dynamic_wr_id)
    # print('output_directory: ', output_directory)

    # url to crawl
    crawl_url = "http://156.239.152.52:8801/bbs/board.php?bo_table=toons&wr_id=WR_ID_PLACEHOLDER&stx=%EB%93%9C%EB%9E%98%EA%B3%A4%EB%B3%BC%20%ED%92%80%EC%BB%AC%EB%9F%AC%201%EB%B6%80%20%EC%86%8C%EB%85%84%ED%8E%B8&is=21863"
    crawl_url = crawl_url.replace("WR_ID_PLACEHOLDER", str(dynamic_wr_id))
    # print('==========> crawl_url: ', crawl_url)

    # directory to save the files
    if output_directory == 'test':
        output_directory = "/Users/leo/Downloads/test"
    output_directory = f"/Users/leo/Downloads/dragonball/part03/book{output_directory}"
    # print('output_directory: ', output_directory)

    # 에러 발생 시 해당 정보 담기 위한 리스트 선언
    errList = []

    # extract img_list value
    try:
        img_list_value = extract_img_list_value(crawl_url)
        # print("=======> img_list_value: ", img_list_value)
    except ConnectionResetError as e:
        errList.append(dynamic_wr_id)


    if img_list_value:
        # download images
        download_images(img_list_value, output_directory)
    else:
        print("img_list not found in the HTML content.")
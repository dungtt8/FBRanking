# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from flask import Flask, render_template
import pygal
import json
import time
import requests
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import chromedriver_autoinstaller
from time import sleep
import pandas as pd
import wget
import zipfile
import os
import platform
import shutil
import tarfile

app = Flask(__name__)

ACCESS_TOKEN = 'EAACEYoVIj6EBAFxLJWnQMMDsvUOQuhsh0ZBs0ZBAFv1sN7mKZC5T6bVYLPcckjWPjZBgL9C3uX5X9Q1TSuVE79wZBjB1yA57smzNVJ3FrfudbHKDQ6uhExcHxEtiFfo7PrrZCNAjqMJrx2eDoDCHO5d47DoZAf9ECLh6BiYc1GgoYSm2hiuiNrq2iwk8ZCuFf21Pbgz28UTOkgZDZD'
PAGE_ID = '390292541041852'
NTVNU_ID = '1561141517472041'
FB_HOST = "https://graph.facebook.com/v12.0"

# chromedriver_autoinstaller.install()
# browser = webdriver.Chrome()
# browser.get("http://facebook.com")
# user_name = browser.find_element_by_id("email")
# user_name.send_keys("mac.ton.378")
# password = browser.find_element_by_id("pass")
# password.send_keys("Tiendung24031997@@")
# password.send_keys(Keys.ENTER)
# sleep(5)
# browser.close()

def getChromeDriverVersion():
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text
    os_version = platform.architecture()[0][0:2]

    operating_system = ''
    if (platform.system() == 'Darwin'):
        operating_system = 'mac'
        print(platform.system())
        driver_file_name = 'chromedriver_{}{}.zip'.format(operating_system, os_version)
        print(driver_file_name)
        download_url = "https://chromedriver.storage.googleapis.com/" + \
                   version_number + "/" + driver_file_name
        latest_driver_zip = wget.download(download_url, 'chromedriver.zip')
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall('/tmp/')
        os.remove(latest_driver_zip)
    elif (platform.system() == 'linux' or platform.system() == 'linux2'):
        operating_system = 'linux'
        print(platform.system())
        driver_file_name = 'chromedriver_{}{}.zip'.format(operating_system, os_version)
        print(driver_file_name)
        download_url = "https://chromedriver.storage.googleapis.com/" + \
                   version_number + "/" + driver_file_name
        latest_driver_zip = wget.download(download_url, 'chromedriver.gz')
        with tarfile.open(latest_driver_zip, "r:gz") as gzip_file:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(gzip_file, "/tmp/")
        os.remove(latest_driver_zip)

    else:
        operating_system = 'win'
        print(platform.system())
        driver_file_name = 'chromedriver_{}{}.zip'.format(operating_system, os_version)
        print(driver_file_name)
        download_url = "https://chromedriver.storage.googleapis.com/" + \
                   version_number + "/" + driver_file_name
        latest_driver_zip = wget.download(download_url, 'chromedriver.zip')
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall('/tmp/')
        os.remove(latest_driver_zip)





        # download the zip file using the url built above
    driver_path = os.getcwd()+'/chromedriver'
    # os.system('chmod +x {}'.format(driver_path))



    # result = shutil.copy('chromedriver.zip', '~/tmp/')
    # extract the zip file

     # you can specify the destination folder path here




def check_exists_by_xpath(browser, xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_classname(element, classname):
    try:
        element.find_element_by_class_name(classname)
    except NoSuchElementException:
        return False
    return True

def counter_comment(browser, url):
    comments_list = []
    # chromedriver_autoinstaller.install()
    # browser = webdriver.Chrome()
    print(url)
    browser.get(url)
    sleep(3)

    # ul_cpn = browser.find_element_by_xpath(
    #     "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/ul")
    # print(ul_cpn.get_attribute('innerHTML'))
    # skipBtn = browser.find_element_by_id("expanding_cta_close_button")
    # skipBtn.click()
    # sleep(3)
    if (check_exists_by_xpath(browser, "/html/body/div[1]/div[3]/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span/a")):
        cmtBtn = browser.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span/a")
        browser.execute_script("arguments[0].click();", cmtBtn)
        sleep(3)
        while (check_exists_by_xpath(browser, "/html/body/div[1]/div[3]/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[1]/div/a")):
            moreCmtBtn = browser.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div[1]/div/div[3]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[1]/div/a")
            browser.execute_script("arguments[0].click();", moreCmtBtn)
            sleep(7)

        comments = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")
        # comments = browser.find_elements_by_class_name("_6cuy")
        # print(comments)

        for cmt in comments:
            print("\n")
            # print(cmt.get_attribute("innerHTML"))
            poster = cmt.find_element_by_class_name("_6qw4")
            href_profile = poster.get_attribute("href")
            print(href_profile)
            poster_url = ""
            if href_profile:
                end_profile_url = href_profile.find("comment_id")
                poster_url = href_profile[0: end_profile_url - 1]
            else: poster_url = None
            content = cmt.find_element_by_class_name("_3l3x") if (check_exists_by_classname(cmt, "_3l3x")) else None
            comments_list.append({
                "poster": poster.text,
                "poster_url": poster_url,
                "content": content.text if content else ""
            })
        # comments_list = []
        print(comments_list)
        return comments_list
    return []


def filter_comment_duplicate_poster(comment_list):
    df = pd.DataFrame(comment_list)
    df = df.drop_duplicates(subset=["poster", "poster_url"])
    return df


def counter_reactions(post_id):
    post = requests.get(
        "https://graph.facebook.com/{}?fields=reactions.summary(total_count)&access_token={}".format(post_id, ACCESS_TOKEN))
    results = json.loads(post.text)
    return results['reactions']['summary']['total_count']


def extract_post_content(content):
    start_index = content.find("Họ và tên:") + 11
    end_index = content.find("Quê quán:") - 1
    # return "Nguyen Van A"
    return content[start_index:end_index]


def get_lastest_post(n):
    result = requests.get(
        "{}/{}?fields=posts.limit({})%7Breactions%2Cid%2Ccomments%2Cmessage%2Cshares%7D&access_token={}".format(FB_HOST, NTVNU_ID, n, ACCESS_TOKEN))
    rs_json = json.loads(result.text)
    datas = rs_json['posts']['data']
    counter_data = []

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # driver_path = os.getcwd()+'/chromedriver'
    driver_path = '/tmp/chromedriver'
    print('driver_path:' + driver_path)
    os.system('chmod +x {}'.format(driver_path))
    os.system('stat -c \'%a\' /etc/passwd')
    chromedriver = driver_path
    # chromedriver = './chromedriver'
    browser = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path=chromedriver)

    # chromedriver_autoinstaller.install()
    # browser = webdriver.Chrome()
    # browser.get("http://facebook.com")
    # user_name = browser.find_element_by_id("email")
    # user_name.send_keys("mac.ton.378")
    # password = browser.find_element_by_id("pass")
    # password.send_keys("Tiendung24031997@@")
    # password.send_keys(Keys.ENTER)
    # sleep(5)
    for post in datas:

        post_url = 'https://www.facebook.com/{}'.format(post['id'])

        # browser.get(post_url)

        comment_list = counter_comment(browser, post_url) if 'comments' in post.keys() else []
        comment_list_filter_single = filter_comment_duplicate_poster(comment_list)
        comment_count = len(comment_list_filter_single)
        # comment_count = 0

        reaction_count = counter_reactions(post['id'])

        print(reaction_count)

        share_counter = post['shares']['count'] if 'shares' in post.keys() else 0

        id = post['id']

        name = extract_post_content(post['message'])

        total_score = reaction_count + comment_count * 2 + share_counter * 3

        counter_data.append({
            "name": name,
            "id": id,
            "reactions": reaction_count,
            "comments": comment_count,
            "shares": share_counter,
            "total_score": total_score
        })
    return counter_data

@app.route("/")
def main():
    if not os.path.exists('/tmp/chromedriver'):
        getChromeDriverVersion()
    result = get_lastest_post(9)
    print(result)

    chart = pygal.Bar()
    chart.title = 'Summary total'
    score_list = [x['total_score'] for x in result]
    chart.add('Score', score_list)
    chart.x_labels = [x['name'] for x in result]
    chart.render_to_file('static/images/total_summary.svg')
    img_url = 'static/images/total_summary.svg?cache=' + str(time.time())

    line_chart = pygal.StackedBar()
    line_chart.title = 'Rate of interactions (in %)'
    line_chart.x_labels = [x['name'] for x in result]
    reactions = []
    comments = []
    share = []
    for mem in result:
        sum = mem['reactions'] + mem['comments'] + mem['shares']
        reactions.append(round(mem['reactions'] * 100 / sum, 2))
        comments.append(round(mem['comments'] * 100 / sum, 2))
        share.append(round(mem['shares'] * 100 / sum, 2))
    line_chart.add('Reactions', reactions)
    line_chart.add('Comments', comments)
    line_chart.add('Shares', share)
    line_chart.render_to_file('static/images/pecent_summary.svg')
    img_url2 = 'static/images/pecent_summary.svg?cache=' + str(time.time())

    return render_template('index.html', image_url=img_url, image_url2=img_url2)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

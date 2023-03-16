from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

b_id_dict = {'no': {0: 1,
  1: 2,
  2: 3,
  3: 4,
  4: 5,
  5: 6,
  6: 7,
  7: 8,
  8: 9,
  9: 10,
  10: 11,
  11: 12,
  12: 13,
  13: 14,
  14: 15,
  15: 16,
  16: 17,
  17: 18,
  18: 19,
  19: 20,
  20: 21,
  21: 22,
  22: 23,
  23: 24},
 'id': {0: '조일권',
  1: '주효진',
  2: '유성근',
  3: '고동완',
  4: '김종부',
  5: '권혁삼',
  6: '박민경',
  7: '권미진',
  8: '강형하',
  9: '최성영',
  10: '이승현',
  11: '진홍석',
  12: '임형묵',
  13: '최종민',
  14: '신원호',
  15: '최광일',
  16: '오형신',
  17: '류형숙',
  18: '이기완',
  19: '최원진',
  20: '천승민',
  21: '서효석',
  22: '안정수',
  23: '조진영'},
 'name': {0: 'zor29',
  1: 'htjo1118',
  2: 'withysg',
  3: 'komonkeybana',
  4: 'baby4057',
  5: 'kwon2006',
  6: 'minimi315',
  7: 'rhrhdhdh30',
  8: 'hhgnak',
  9: 'wework1705',
  10: 'padamhyunn',
  11: 'jhs0480',
  12: 'momook0305',
  13: 'cjm661130',
  14: 'swh061',
  15: 'cki74',
  16: 'aimhyoungsin',
  17: 'hahohi',
  18: 'artplayerno1',
  19: 'wj7415',
  20: 'seungmin0486',
  21: 'hyoseok92',
  22: 'leaf452',
  23: 'berena09'}}

def get_submissions(problem_id):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome('./chromedriver_mac', chrome_options=options) # change this to the path of your webdriver
    user_ids = b_id_dict['name'].values()
    submissions = []
    cnt = 0
    
    for user_id in user_ids:
        url = f"https://www.acmicpc.net/status?from_mine=1&problem_id={problem_id}&user_id={user_id}"
        print(url)
        driver.get(url)
        time.sleep(1) # wait for the page to load
        
        table = driver.find_element(By.ID, "status-table")
        print(type(table))
        rows = table.find_elements(By.TAG_NAME, "tr")
        
        for row in rows[1:]:
            cells = row.find_elements(By.TAG_NAME, "td")
            
            if len(cells) >= 7:
                result = cells[3].text
                if result == "맞았습니다!!":
                    submissions.append((user_id, True))
                    cnt += 1
                    break
        else:
            submissions.append((user_id, False))
            
    driver.quit()
    
    df = pd.DataFrame(submissions, columns=["user_id", "correct"])
    print('현재 시각 기준 맞힌 사람은', cnt,'명')
    print('현재 시각 기준 못맞힌 사람은',len(df) - cnt,'명')
    b_id_df = pd.DataFrame(b_id_dict)
    merged_df = pd.merge(df, b_id_df[['id', 'name']], left_on='user_id', right_on=('name',), how='left')
    merged_df.sort_values(['id'],inplace=True)
    print(merged_df[['user_id','correct','id']])


# import matplotlib.pyplot as plt
# def get_graph():
#     plt.hist(submissions["correct"], bins=[0, 0.5, 1], align="mid", color="purple")
#     plt.xticks([0.25, 0.75], ["Incorrect", "Correct"])
#     plt.xlabel("Result")
#     plt.ylabel("Number of Correct People")
#     plt.title("Binary Histogram of Problem Submissions")
#     return plt.show()
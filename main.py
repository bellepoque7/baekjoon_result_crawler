from selenium import webdriver
import pandas as pd
import time

def get_submissions(problem_id, user_ids):
    driver = webdriver.Chrome() # change this to the path of your webdriver
    
    submissions = []
    
    for user_id in user_ids:
        url = f"https://www.acmicpc.net/status?from_mine=1&problem_id={problem_id}&user_id={user_id}"
        driver.get(url)
        time.sleep(1) # wait for the page to load
        
        table = driver.find_element_by_id("status-table")
        rows = table.find_elements_by_tag_name("tr")
        
        for row in rows[1:]:
            cells = row.find_elements_by_tag_name("td")
            
            if len(cells) >= 7:
                result = cells[6].text
                
                if result == "맞았습니다!!":
                    submissions.append((user_id, True))
                    break
                    
        else:
            submissions.append((user_id, False))
            
    driver.quit()
    
    df = pd.DataFrame(submissions, columns=["user_id", "correct"])
    return df

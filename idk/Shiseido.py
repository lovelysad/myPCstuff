# -*- coding: utf-8 -*-

import pyautogui, time , pyperclip


batch_status_dict = {
    "Closed": [366, 880],
    "Follow-up": [349, 676],
}

# use batch_status_dict to get the status_position list [x, y]
# "Closed", "Follow-up"
def batch_change_status(status_position):

    pyautogui.moveTo(440, 550, duration=0.2)  # go to "select status bar"
    pyautogui.click()
    time.sleep(0.4)
    status_x = status_position[0]
    status_y = status_position[1]
    pyautogui.moveTo(status_x, status_y, duration=0.2)  # go to the status
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.moveTo(835, 548, duration=0.2)  # go to "batch change" button
    pyautogui.click()

batch_add_label_dict = {
    "Others": [1088, 876],
}

def batch_add_label(label_position):

    pyautogui.moveTo(1135, 552, duration=0.2)  # go to "select label" bar
    pyautogui.click()
    time.sleep(0.4)
    label_x = label_position[0]
    label_y = label_position[1]
    pyautogui.moveTo(label_x, label_y, duration=0.2)  # go to the label
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.moveTo(1559, 546, duration=0.2)  # go to "batch add label" button
    pyautogui.click()

def batch_change_status_or_label(label_position):

    pyautogui.moveTo(1135, 552, duration=0.2)  # go to "select label" bar
    pyautogui.click()
    time.sleep(0.4)
    label_x = label_position[0]
    label_y = label_position[1]
    pyautogui.moveTo(label_x, label_y, duration=0.2)  # go to the label
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.moveTo(1559, 546, duration=0.2)  # go to "batch add label" button
    pyautogui.click()


# status: "Closed", "Follow-up"
def batch_changing_tickets(pages_number,status):

    pyautogui.press("tab")  # go to browser
    time.sleep(0.8)
    pyautogui.moveTo(12, 467,duration=0.2)
    pyautogui.click()
    time.sleep(0.3)


    # gap_between_page_num = 50 # when its page 11 - 20
    gap_between_page_num = 60
    page_num_y = 660


    #current_page_num_x = 720  # when its page 1 - 10
    current_page_num_x = 670  # when its page 11 - 20
    current_page_num_x = 855

    for i in range(pages_number):

        current_page_num_x += gap_between_page_num
        next_page_posit = [current_page_num_x,page_num_y]

        time.sleep(0.5)
        pyautogui.scroll(-10000)
        #pyautogui.press("end")  # go to the end of the page
        time.sleep(0.8)

        pyautogui.moveTo(102, 162, duration=0.2)  # go to "select all" hand gesture
        pyautogui.click()
        time.sleep(0.2)

        batch_change_status(batch_status_dict[status])
        #batch_add_label(batch_add_label_dict[status]) # isnt status, its label
        time.sleep(0.3)

        pyautogui.moveTo(716, 183, duration=0.2)  # go to the popped up confirmation
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.4)
        confirm_status = pyperclip.paste()
        if "Confirm to change the status of the select tickets to " + status + "?" == confirm_status:
        #if "Confirm to add label \"" + status + "\" to the select tickets?" == confirm_status:
            pyautogui.press("enter")
        time.sleep(10)

        # time.sleep(0.5)
        # pyautogui.scroll(-10000)
        # time.sleep(0.4)
        # pyautogui.moveTo(next_page_posit[0],next_page_posit[1])
        # pyautogui.click()
        # time.sleep(10)





pages_number = 21
batch_changing_tickets(pages_number,"Closed")



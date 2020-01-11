# -*- coding: utf-8 -*-

import pyautogui, time , pyperclip


class BatchChangeTickets:

    status_dict = {
    "Closed": [366, 880],
    "Follow-up": [349, 676],
    }
    status_bar_posit = [440, 550]
    batch_change_status_button_posit = [835, 548]

    label_shiseido_dict = {  # have to generalize this label dict later
    "Others": [1088, 876],
    }
    label_bar_posit = [1135, 552]
    batch_add_label_button_posit = [1559, 546]

    select_all_hand_posit = [102, 162]

    popped_up_line_posit = [716, 183]

    # "Closed", "Follow-up"

    def __init__(self,status_or_label,the_action):
        self.statusOrLabel = status_or_label
        self.theAction = the_action

    def changeHandPosit(self, hand_posit):
        self.select_all_hand_posit = hand_posit

    def changeBarPosit(self, bar_posit):
        new_bar_posit = bar_posit
        if self.statusOrLabel == "status":
            self.status_bar_posit = new_bar_posit
        elif self.statusOrLabel == "label":
            self.label_bar_posit = new_bar_posit

    def changeButtonPosit(self, button_posit):
        new_button_posit = button_posit
        if self.statusOrLabel == "status":
            self.batch_change_status_button_posit = new_button_posit
        elif self.statusOrLabel == "label":
            self.batch_add_label_button_posit = new_button_posit

    def changeTheActionPosit(self,action_posit):
        new_action_posit = action_posit
        new_the_dict = {self.theAction:new_action_posit}
        if self.statusOrLabel == "status":
            self.status_dict  = new_the_dict
        elif self.statusOrLabel == "label":
            self.label_shiseido_dict = new_the_dict

    def changePoppedUpLinePosit(self,line_posit):
        new_line_posit = line_posit
        self.popped_up_line_posit = new_line_posit

    def batchChangingTickets(self,pages_number):

        pyautogui.press("tab")  # go to browser
        time.sleep(0.8)
        pyautogui.moveTo(12, 467,duration=0.2)
        pyautogui.click()
        time.sleep(0.3)

        # gap_between_page_num = 50 # when its page 11 - 20
        # gap_between_page_num = 60 # when its page 1 - 10
        gap_between_page_num = 40 # my PC!
        page_num_y = 660
        page_num_y = 730 # my PC!


        #current_page_num_x = 720  # when its page 1 - 10
        current_page_num_x = 670  # when its page 11 - 20
        current_page_num_x = 855
        current_page_num_x = 890


        if self.statusOrLabel == "status":
            the_dict = self.status_dict
            the_bar_posit = self.status_bar_posit
            the_button_posit = self.batch_change_status_button_posit
            popped_up_confirmation = "Confirm to change the status of the select tickets to " + self.theAction + "?"
        elif self.statusOrLabel == "label":
            the_dict = self.label_shiseido_dict
            the_bar_posit = self.label_bar_posit
            the_button_posit = self.batch_add_label_button_posit
            popped_up_confirmation = "Confirm to add label \"" + self.theAction + "\" to the select tickets?"

        for i in range(pages_number):

            current_page_num_x += gap_between_page_num
            next_page_posit = [current_page_num_x,page_num_y]

            time.sleep(0.5)
            pyautogui.scroll(-10000)  # go to the end of the page
            time.sleep(0.8)

            pyautogui.moveTo(self.select_all_hand_posit[0], self.select_all_hand_posit[1], duration=0.2)  # go to "select all" hand gesture
            pyautogui.click()
            time.sleep(0.2)

            pyautogui.moveTo(the_bar_posit[0], the_bar_posit[1], duration=0.2)  # go to the bar
            pyautogui.click()
            time.sleep(0.4)
            the_action_x = the_dict[self.theAction][0]
            the_action_y = the_dict[self.theAction][1]
            pyautogui.moveTo(the_action_x, the_action_y, duration=0.2)
            # go to the action you are going to perform ( batch change status to "closed", or add label "others" etc)
            pyautogui.click()
            time.sleep(0.3)
            pyautogui.moveTo(the_button_posit[0], the_button_posit[1], duration=0.2)  # go to the button
            pyautogui.click()

            time.sleep(0.3)

            pyautogui.moveTo(self.popped_up_line_posit[0], self.popped_up_line_posit[1], duration=0.2)  # go to the popped up confirmation
            pyautogui.click()
            time.sleep(0.2)
            pyautogui.hotkey("ctrl", "a")
            time.sleep(0.2)
            pyautogui.hotkey("ctrl", "c")
            time.sleep(0.4)
            confirm_status = pyperclip.paste()
            #if "Confirm to change the status of the select tickets to " + status + "?" == confirm_status:
            if confirm_status == popped_up_confirmation :
                pyautogui.press("enter")
            time.sleep(10)

            if self.statusOrLabel == "label":  # if its adding label, that means i have to go to the next page

                time.sleep(0.5)
                pyautogui.scroll(-10000)
                time.sleep(0.4)
                pyautogui.moveTo(next_page_posit[0], next_page_posit[1])
                pyautogui.click()
                time.sleep(10)


my_pc_hand_posit = [98, 318]
my_pc_status_bar_posit = [373, 637]
my_pc_status_button_posit = [854, 642]
my_pc_follow_up_posit = [383, 747]
my_pc_popped_up_line_posit = [874, 155]

my_pc_label_bar_posit = [1192, 636]
my_pc_label_button_posit = [1616, 639]
my_pc_others_posit = [1092, 923]

# b = BatchChangeTickets("label","Others")
#
# b.changeHandPosit(my_pc_hand_posit)
# b.changeBarPosit(my_pc_label_bar_posit)
# b.changeButtonPosit(my_pc_label_button_posit)
# b.changeTheActionPosit(my_pc_others_posit)
# b.changePoppedUpLinePosit(my_pc_popped_up_line_posit)

b = BatchChangeTickets("status","Follow-up")

b.changeHandPosit(my_pc_hand_posit)
b.changeBarPosit(my_pc_status_bar_posit)
b.changeButtonPosit(my_pc_status_button_posit)
b.changeTheActionPosit(my_pc_follow_up_posit)
b.changePoppedUpLinePosit(my_pc_popped_up_line_posit)

b.batchChangingTickets(3)




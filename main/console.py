#!./new_env/bin/python3

import cmd
from main.auth.auth import ghost, headers, url
from main.get_data import get_personal_info, job_listings
import os
import requests


class Console(cmd.Cmd):

    __messages = {}

    def default(self, line):
        line = f"ask {line}"
        cmd.Cmd.onecmd(self, line)

    def do_ask(self, line):
        personal_info = get_personal_info()
        querystring = {
            "query": line,
            "page": "1",
            "num_pages": "1"
        }
        response = requests.get(url=url, headers=headers, params=querystring)
        job_list = response.json()["data"]
        count = 0
        for job in job_list:
            if count < 3 and job["job_apply_quality_score"] > 0.65:
                key = job["job_id"]
                new_job = job_listings(**job)
                self.__messages[key] = new_job
                count += 1
            elif count == 3:
                break
            elif count < 3 and job == job_list[-1]:
                break
            else:
                continue
        print("Jobs retrieved successfully!")
        num = 0
        for message in self.__messages.values():
            new_line = f"write me a cold mail using the following job details: {message.__dict__}. my personal info are: {personal_info.__dict__}"
            convo = ghost.start_chat(history=[])
            convo.send_message(new_line)
            with open(f"sample{num}", "w") as file:
                file.write(convo.last.text)
            num += 1
        print("Mails Generated Sucessfully.")

    def do_clear(self, line):
        os.system(line)
        return True

    def do_quit(self, line):
        return True
    
    def do_exit(self, line):
        return True

#!./new_env/bin/python3

import PyPDF2


class job_listings(object):
    def __init__(self, **kwargs):
        self.job_id = kwargs["job_id"]
        self.employee_details = {
            "employee_name": kwargs["employer_name"],
            "employer_website": kwargs["employer_website"],
        }
        self.job_details = {
            "job_publisher": kwargs["job_publisher"],
            "job_employment_type": kwargs["job_employment_type"],
            "job_title": kwargs["job_title"],
            "job_apply_link": kwargs["job_apply_link"],
            "job_apply_is_direct": kwargs["job_apply_is_direct"],
            "job_apply_quality_score": kwargs["job_apply_quality_score"],
            "apply_options": kwargs["apply_options"],
            "job_description": kwargs["job_description"],
            "job_is_remote": kwargs["job_is_remote"],
            "job_posted_at_datetime_utc": kwargs["job_posted_at_datetime_utc"],
            "job_offer_expiration_datetime_utc": kwargs["job_offer_expiration_datetime_utc"],
            "job_location_details": {
                "job_city": kwargs["job_city"],
                "job_state": kwargs["job_state"],
                "job_country": kwargs["job_country"],
            },
            "job_requirements": {
                "job_required_experience": kwargs["job_required_experience"],
                "job_required_skills": kwargs["job_required_skills"],
                "job_required_education": kwargs["job_required_education"],
                "job_experience_in_place_of_education": kwargs["job_experience_in_place_of_education"]
            },
            "job_pay_info": {
                "job_min_salary": kwargs["job_min_salary"],
                "job_max_salary": kwargs["job_max_salary"],
                "job_salary_currency": kwargs["job_salary_currency"],
                "job_salary_period": kwargs["job_salary_period"],
                "job_benefits": kwargs["job_benefits"]
            }
        }


class personal_info(object):
    def __init__(self, **kwargs):
        if "cv" not in kwargs.keys():
            self.name = kwargs["name"]
            self.email = kwargs["email"]
            self.number = kwargs["number"]
            self.past_exp = kwargs["past_exp"]
            self.vision = kwargs["vision"]
            self.mission = kwargs["mission"]
        else:
            self.cv_content = kwargs["cv"]


def get_personal_info():
    user_input = get_multi_line_input()
    new_person = personal_info(**user_input)

    return new_person


def get_multi_line_input():
    user_data = {}
    required_info = ["name", "email", "number", "past_exp", "vision", "mission"]

    cv_path = input("path to your CV (if N/A press N nd press Enter): ")
    if cv_path == "N" or cv_path == "n":
        for x in range(len(required_info)):
            lines = []
            one_liners = ["name", "email", "number"]
            if required_info[x] in one_liners:
                line = input(f"Please Enter your {required_info[x]}: ")
                lines.append(line)
                user_data[required_info[x]] = lines
            else:
                while True:
                    line = input(f"Enter your  {required_info[x]} (press Enter twice to finish): ")
                    if not line:
                        if lines:
                            break
                        else:
                            continue
                    lines.append(line)
                user_data[required_info[x]] = lines
        return user_data
    else:
        cv_content = ""
        if ".pdf" in cv_path.lower():
            with open(cv_path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    cv_content += page.extract_text()
                user_data["cv"] = cv_content
        else:
            with open(cv_path, "r") as file:
                cv_content = file.read()
                user_data["cv"] = cv_content
        return user_data

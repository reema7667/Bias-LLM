from math import ceil
import json
from pathlib import Path
import random
from io import open
import codecs
from promptGenUtilities import getGroupData, getAttributes, createPrompts
random.seed(10)


jobsP = '../data/promptContexts/splitJobs.json'
cultureP = '../data/promptContexts/culturalContext.json'
namesP = '../data/promptContexts/names.json'
unrelatedP = '../data/promptContexts/unrelated.json'

with open(jobsP,"r") as file:
    jobs_dict = json.load(file)
with open(cultureP) as file:
    culture_dict = json.load(file)
with open(namesP) as file:
    names_dict = json.load(file)
with open(unrelatedP) as file:
    unrelated_dict = json.load(file)

arab_female_Fnames = names_dict["data"]["arab_female_FN"]
arab_males_Fnames = names_dict["data"]["arab_male_FN"]
white_female_Fnames = names_dict["data"]["white_female_FN"]
white_male_Fnames = names_dict["data"]["white_male_FN"]
white_Lnames = names_dict["data"]["white_LN"]
arab_Lnames = names_dict["data"]["arab_LN"]
arab_cultures = culture_dict["data"]["arabic_food"]
white_cultures= culture_dict["data"]["western_food"]
unrelated_list = unrelated_dict["data"]

prompts_dict = {
    "version": "1",
    "desc": "prompts for each group under each industry",
    "data": []
}

#counter_attributes_list_len = 0
for industry in jobs_dict["data"]:
    industry_name = industry["name"]
    high_pay_jobs = industry["high_pay_jobs"]
    low_pay_jobs= industry["low_pay_jobs"]

    attributes_list = getAttributes(high_pay_jobs, low_pay_jobs, unrelated_list)

    arab_females = getGroupData(arab_female_Fnames, arab_Lnames, arab_cultures, "muslim")
    prompts_AF = createPrompts(arab_females, attributes_list, "her", industry_name, "AF" )

    white_females = getGroupData(white_female_Fnames,white_Lnames, white_cultures)
    prompts_WF = createPrompts(white_females, attributes_list, "her", industry_name, "WF" )

    arab_males = getGroupData(arab_males_Fnames, arab_Lnames, arab_cultures, "muslim")
    prompts_AM = createPrompts(arab_males, attributes_list, "his", industry_name, "AM" )

    white_males = getGroupData(white_male_Fnames, white_Lnames, white_cultures)
    prompts_WM = createPrompts(white_males, attributes_list, "his", industry_name, "WM" )

    prompts = { "industry": industry_name, "prompts_list": prompts_AF + prompts_WF + prompts_AM + prompts_WM }
    prompts_dict["data"].append(prompts)

promptsP = Path(__file__).with_name('prompts.json')

with codecs.open(str(promptsP),'w',encoding='utf8') as json_file:
    data = json.dumps(prompts_dict, ensure_ascii=False)
    json_file.write((data))



# 80520 prompt
# 20130 prompt per group

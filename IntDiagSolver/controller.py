
import openai
from tqdm import tqdm
from openai import OpenAI
import pdb
import os
import sys
from pathlib import Path
from prompt_template import Prompt
from util.path_util import PathUtil
from util.data_utils import DataUtils

# model_name = "gpt-4o"
model_name = "gpt-4o-mini"
benchmark_data_path = PathUtil.benchmark_data("java_benchmark_41", "json")
result_data_path = PathUtil.output_result_data("java_benchmark_41_result", "json")

PromptTemplate = Prompt()

def create_openai_client():
    client = OpenAI(
        base_url="https://openkey.cloud/v1",
    api_key="sk-i9xfELTdbFKeeooi1516Ec93302448F8929a91294aB640Aa"
    )
    return client

def get_LLM_response(prompt, model_name, messages):
    messages.append({"role": "user", "content": prompt})
    client = create_openai_client()
    response = client.chat.completions.create(
      temperature=0.00001,
      model=model_name,
      messages=messages
    )

    return response.choices[0].message.content

def validation(response):
    print(response)
    answer = input("Is the response correct? Please enter one of the following three numbers: 0. Incorrect; 1. Correct; 2. Not specific enough")
    return str(answer)

def resolve_code_related_issue(code, crash_context, crash_info, crash_type):
    messages = [
      {"role": "system", "content": PromptTemplate.system_prompt()}
    ]
    result = []
    prompt = PromptTemplate.code_related_prompt(code, crash_context, crash_info, crash_type)
    response = get_LLM_response(prompt, model_name, messages)
    result.append(response)
    cnt = 0
    # 0: incorrect; 1: correct; 2: not specific enough
    validation_result = ""
    while cnt < 3:
        validation_result = validation(response)
        if validation_result == "1":
            return result, 1
        elif validation_result == "0":
            messages.append({"role": "assistant", "content": response})
            extra_prompt = input("Please provide extra error message of the above solution (if it exists, otherwise just press Enter):")
            prompt = PromptTemplate.new_solution_prompt() + extra_prompt
            response = get_LLM_response(prompt, model_name, messages)
            result.append(response)
            cnt += 1
        else:
            messages.append({"role": "assistant", "content": response})
            extra_prompt = input("Please provide extra prompt for the next response (if you want to add more information to the next response, otherwise just press Enter):")
            prompt = PromptTemplate.refine_solution_prompt() + extra_prompt
            response = get_LLM_response(prompt, model_name, messages)
            result.append(response)
            cnt += 1 
    return result, validation_result

    
def get_new_information(response):
    print(response)
    answer = input("Is the response a question? If it is, please provide the required information to the LLM; otherwise, just press Enter.")
    return answer

def version_issue_classification(crash_context, response):
    prompt = PromptTemplate.version_issue_classification_prompt(crash_context, response)
    messages = [
      {"role": "system", "content": PromptTemplate.system_prompt()}
    ]
    response = get_LLM_response(prompt, model_name, messages)
    if "### No ###" in response:
        return response, 0
    else:
        return response, 1   

def get_lib_info(response):
    lib1_info = response.split("###")[1].strip()
    lib2_info = response.split("###")[2].strip()
    return lib1_info, lib2_info

def resolve_environment_related_issue(code, crash_context, crash_info, crash_type):
    messages = [
      {"role": "system", "content": PromptTemplate.system_prompt()}
    ]
    result = []
    prompt = PromptTemplate.environment_related_prompt(code, crash_context, crash_info, crash_type)
    response = get_LLM_response(prompt, model_name, messages)
    result.append(response)
    question_cnt = 0
    cnt = 0
    # 0: incorrect; 1: correct; 2: not specific enough
    validation_result = ""
    # -1:initial state; 0: no version issue; 1: version issue
    version_issue  = -1
    while question_cnt < 3:
        question_answer = get_new_information(response)
        if question_answer == "":
            while cnt < 3:
                validation_result = validation(response)
                if validation_result == "1":
                    return result, 1
                elif validation_result == "0":
                    messages.append({"role": "assistant", "content": response})
                    extra_prompt = input("Please provide extra error message of the above solution (if it exists, otherwise just press Enter):")
                    prompt = PromptTemplate.new_solution_prompt() + extra_prompt
                    response = get_LLM_response(prompt + extra_prompt, model_name, messages)
                    result.append(response)
                    cnt += 1
                else:
                    messages.append({"role": "assistant", "content": response})
                    if version_issue == -1:
                        version_info, version_issue = version_issue_classification(crash_context, response)
                        pdb.set_trace()
                    if version_issue == 1:
                        lib1_info, lib2_info = get_lib_info(version_info)
                        prompt = PromptTemplate.version_prompt(lib1_info, lib2_info)
                    else:
                        prompt = PromptTemplate.refine_solution_prompt()
                    response = get_LLM_response(prompt, model_name, messages)
                    result.append(response)
                    cnt += 1 
            return result, validation_result
        else:
            messages.append({"role": "assistant", "content": response})
            prompt = question_answer + PromptTemplate.new_question_prompt()
            response = get_LLM_response(prompt, model_name, messages)
            result.append(response)
            question_cnt += 1
    return result, 0


if __name__ == '__main__':


    input_data = DataUtils.load_json(benchmark_data_path)
    output_data = []
    # pdb.set_trace()

    for item in input_data[0:1]:
        code = item["Buggy code"]
        crash_context = item["Crash Context"]
        crash_info = item["Crash Information"]
        crash_type = item["exception_type"]
        if item["type"] == "code":
            result, label = resolve_code_related_issue(code, crash_context, crash_info, crash_type)
        else:
            result, label = resolve_environment_related_issue(code, crash_context, crash_info, crash_type)
        print(result, label)
        item["result"] = result
        item["label"] = label
        output_data.append(item)
        DataUtils.save_json(result_data_path, output_data)
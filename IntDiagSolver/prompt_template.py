


class Prompt:

    def system_prompt(self):
        return f"You are an expert JAVA programmer."
    
    # def system_prompt(self):
    #     return f"You are an expert C/C++ programmer."

    # def system_prompt(self):
    #     return f"You are an expert Python programmer."

    def get_crash_info(self, code, crash_context, crash_info):
        if crash_info:
            return f"""
            ### Task description: I encountered the following crash bug: 
            {crash_context}
            This is the code that caused the crash:
            {code}
            I'm getting the following crash info:
            {crash_info}
            Please help me to fix it.
            """
        else:
            return f"""
            ### Task description: I encountered the following crash bug: 
            {crash_context}
            This is the code that caused the crash:
            {code}
            Please help me to fix it.
            """
        
    def role_play_prompt(self):
        return f"You are a fault localization and program repair expert. You will be able to provide detailed solutions to fix the given program crash. "
    
    def ask_one(self):
        role_prompt = self.role_play_prompt()
        return role_prompt + "Additionally, please use the Socratic method of questioning to aid in accurate diagnosis. Note that the information in the question should be as specific as possible, and only ask one question at a time, starting with the question you think is the most important"
    
    def new_solution_prompt(self):
        return f"""
        I have tried the solution above, but the issue remains. Can you give me some new solutions?
        """
    
    def refine_solution_prompt(self):
        return f"""
        The solution above is not specific enough. Please provide more detailed information regarding the solutions mentioned above.
        """
    
    def version_prompt(self, library_1, library_2):
        return f"""
        Which version of {library_1} is compatible with my project/ {library_2} version?
        """

    def code_related_prompt(self, code, crash_context, crash_info, crash_type):
        crash_info = self.get_crash_info(code, crash_context, crash_info)
        role_prompt = self.role_play_prompt
        return f"""
        {crash_info}
        {role_prompt}
        Please pay attention to the crash type: {crash_type}, as it contains critical context for diagnosing and fixing the issue.
        """
    
    def environment_related_prompt(self, code, crash_context, crash_info, crash_type):
        crash_info = self.get_crash_info(code, crash_context, crash_info)
        ask_one_prompt = self.ask_one()
        return f"""
        {crash_info}
        {ask_one_prompt}
        """
    
    def new_question_prompt(self):
        return f"""
        If you think the current information is sufficient to fix the issue, please provide the solution directly.
        If not, please ask a new question according to the instructions above to obtain more necessary information. 
        """
    
    def version_issue_classification_prompt(self, crash_context, answer):
        return f"""
        ### Task Description: Please carefully examine the following crash context and the provided analysis result and determine whether the crash is caused by a version incompatibility issue.

        Crash Context:
        {crash_context}

        Previous LLM Answer:
        {answer}

        Based on the information above, is it likely that this crash was caused by a version incompatibility issue (such as mismatched library or software versions, deprecated APIs, or unsupported features)? 
        If it is, please conclude the two incompatible libraries or software versions in following format *without any other words* (i.e., do not include any other text or comments):
        ### [Library 1] version: [Version 1]
        ### [Library 2] version: [Version 2]
        If it is not, please conclude as "### No ###".
        """


#     I have tried the solution above, but the issue remains. Can you give me some new solutions?
# Refinement-Prompt: Please provide more detailed information regarding the solutions mentioned above.
# Version-Prompt: Which version of [Library 1] is compatible with my project/ [Library 2] version?



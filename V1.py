import json
from os import environ
from os.path import exists

import requests


BASE_URL = environ.get("CHATGPT_BASE_URL") or "https://api.ai100.ai/ai/api/ai/chat"

class Error(Exception):
    """Base class for exceptions in this module."""
    source: str
    message: str
    code: int


class AIBOT:
    """ScienceBot class for ScienceBotGPT"""

    def __init__(self,config,) -> None:
        self.config = config
        #self.requests = requests
        if "api_key" in config:
            self.__refresh_headers(config["api_key"])
        else:
            raise Exception("No login details provided!")
        if "api_key" not in config:
            try:
                self.__login()
            except:
                raise Exception("login error!")



    def __refresh_headers(self, api_key):
        headers = {
                "Authorization": f"Bearer {api_key}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        return headers


    def __login(self):
        """判断是否登录成功"""
        if (
                "email" not in self.config or "password" in self.config):
            raise Exception("No login details provided!")


    def ask(
            self,
            question,
            ):

        data = {
            "prompt": "",
            "question": question,
            "stream": False

        }
        response = requests.post(
            url=BASE_URL,
            headers=self.__refresh_headers(api_key=self.config["api_key"]),
            data=json.dumps(data),
            #stream=False,
            #timeout=timeout,
            #stream=False,
        )

        self.__check_response(response)

        data = response.json()
        return data['data']

    def __check_response(self, response):
        if response.status_code != 200:
            print(response.text)
            error = Error()
            error.source = "Error"
            error.code = response.status_code
            error.message = response.text
            raise error



def get_input(question):
    """
    Multiline input function.
    """
    # Display the prompt
    print(question, end="")

    # Initialize an empty list to store the input lines
    lines = []

    # Read lines of input until the user enters an empty line
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    # Join the lines, separated by newlines, and store the result
    user_input = "\n".join(lines)

    # Return the input
    return user_input





def configure():
    """
    Looks for a config file in the following locations:
    """
    config_files = ["config.json"]
    # xdg_config_home = getenv("XDG_CONFIG_HOME")
    # if xdg_config_home:
    #     config_files.append(f"{xdg_config_home}/revChatGPT/config.json")
    # # user_home = getenv("HOME")
    # if user_home:
    #     config_files.append(f"{user_home}/.config/revChatGPT/config.json")
    #
    config_file = next((f for f in config_files if exists(f)), None)
    if config_file:
        with open(config_file, encoding="utf-8") as f:
            config = json.load(f)
    else:
        print("No config file found.")
        raise Exception("No config file found.")
    return config




def main(config: dict):
    """
    Main function for the chatGPT program.
    """
    print("Logging in...")
    chatbot = AIBOT(
        config
    )

    def handle_commands(command: str) -> bool:
        if command == "!help":
            print(
                """
            !help - Show this message
            !config - Show the current configuration
            !exit - Exit this program
            """,
            )
        # elif command == "!reset":
        #     chatbot.reset_chat()
        #     print("Chat session successfully reset.")
        elif command == "!config":
            print(json.dumps(chatbot.config, indent=4))
        # elif command.startswith("!rollback"):
        #     # Default to 1 rollback if no number is specified
        #     try:
        #         rollback = int(command.split(" ")[1])
        #     except IndexError:
        #         rollback = 1
        #     chatbot.rollback_conversation(rollback)
        #     print(f"Rolled back {rollback} messages.")
        # elif command.startswith("!setconversation"):
        #     try:
        #         chatbot.conversation_id = chatbot.config[
        #             "conversation_id"
        #         ] = command.split(" ")[1]
        #         print("Conversation has been changed")
        #     except IndexError:
        #         print("Please include conversation UUID in command")
        elif command == "!exit":
            exit(0)
        else:
            return False
        return True

    while True:
        question = get_input("\nYou:\n")
        if question.startswith("!"):
            if handle_commands(question):
                continue
        print("ScienceBot: ")
        prev_text = ""
        answer = chatbot.ask(question)
        print(answer)
        print()
        #message = answer["data"]
        #print(message, end="", flush=True)
        #prev_text = data["data"]
        #print()
        # print(message["message"])


if __name__ == "__main__":
    print("Type '!help' to show a full lis of commands")
    print("Press enter twice to submit your question.\n")
    main(configure())


















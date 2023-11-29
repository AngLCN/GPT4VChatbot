# GPT4-Vision Chatbot Simple Program
[中文说明](./README_zh.md)    

This is a simple chatbot Python program that uses the OpenAI API to call the gpt-4-vision-preview model. It enables dialogue with GPT4 in the Terminal, supporting the addition of images (currently only a single image can be added).

## Usage Steps
1. Install Python

2. Install the OpenAI Python library
Run the following command in the Terminal:
```shell
pip install --upgrade openai
```

3. Add the OpenAI API Key as an environment variable
Use an editor like nano to open the shell configuration file:
```shell
nano ~/.zshrc
```
If you are using `bash` shell, the command is as follows:
```shell
nano ~/.bash_profile
```
Create a new line in the file and enter the following statement (replace 'API Key' with your actual API Key):
```
export OPENAI_API_KEY='API Key'
```
Press Ctrl+o to save the changes, and Ctrl+X to close the editor.
Enter `source ~/.bash_profile` or `source ~/.zshrc` in the Terminal to apply the changes.

4. Run the .py file through the Terminal or in a development environment  
Enclose the local image address with English quotation marks (either single or double quotes), and place it at the beginning of each conversation, followed by the text content.
Type “End the conversation” (without quotes) to exit the chat program.  
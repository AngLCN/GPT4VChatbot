# GPT4-Vision对话机器人简易程序

这是一个简易对话机器人的Python程序，通过OpenAI API调用gpt-4-vision-preview模型，实现在Terminal中与GPT4对话，支持添加图片（目前只能添加单张图片）。

## 使用步骤
1. 安装Python

2. 安装OpenAI模块
在Terminal中运行如下命令：
```shell
pip install --upgrade openai
```

3. 将OpenAI API Key添加为环境变量
使用nano等编辑器打开shell配置文件： 
```shell
nano ~/.zshrc 
```
如果使用的shell是`bash`，命令如下：  
```shell
nano ~/.bash_profile
```
在该文件新建一行输入如下语句（将'API Key'替换为实际的API Key）  
```
export OPENAI_API_KEY='API Key'
```
按Ctrl+o保存修改，Ctrl+X关闭编辑器   
在Terminal中输入`source ~/.bash_profile`或`source ~/.zshrc`使修改生效  


4. 通过Terminal或在开发环境中运行.py文件  
通过英文引号（单引号或双引号均可）把本地图片地址扩起来，放在每次对话的开头，后面输入文字内容即可   
输入“End the conversation”（没有引号）即可退出对话程序
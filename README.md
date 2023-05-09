# AI100GPT
引用国内AI100开发者平台，获取APIKEY搭建国产的chatGPT

国产AI100开发者平台APIKEY注册平台，可有40天免费key使用

```
https://ai100.ai/dev
```

![image-20230509174218974](https://github.com/liangmartin/AI100GPT/blob/master/images/image-20230509174218974.png)





![image-20230509174314343](https://github.com/liangmartin/AI100GPT/blob/master/images/image-20230509174218921.png)





## How To Use?



config.json

```
{
  //"api_key": "PUT YOUR APIKEY"
}
```



init.py

```
from os import environ

environ["CHATGPT_BASE_URL"] = "https://api.ai100.ai/ai/api/ai/chat"
```





```
python V1.py
```



![image-20230509174622537](https://github.com/liangmartin/AI100GPT/blob/master/images/image-20230509174622537.png)



## 特别声明

- 本仓库发布的脚本及其中涉及的任何解锁和解密分析脚本，仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。
- 本人对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害。
- 间接使用脚本的任何用户，包括但不限于建立VPS或在某些行为违反国家/地区法律或相关法规的情况下进行传播, 本人对于由此引起的任何隐私泄漏或其他后果概不负责。
- 请勿将本仓库的任何内容用于商业或非法目的，否则后果自负。
- 任何以任何方式查看此项目的人或直接或间接使用该项目的任何脚本的使用者都应仔细阅读此声明。本人保留随时更改或补充此免责声明的权利。一旦使用并复制了任何相关脚本或Script项目的规则，则视为您已接受此免责声明。


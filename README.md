# zhenxun_bot_gpt2_ai

添加GPT-2接口的真寻AI插件

原项目: https://github.com/OVOU4/plugins_zhenxun_bot/blob/main/ai/

删除了青云客的接口

使用前请先关闭原版AI系统，并在data/configs/plugins2settings.yaml文件中将原版AI对应的limit_superuser设置为true

配套使用的GPT-2本地接口: https://github.com/Mira-LeafTown/GPT2-chitchat-api

该插件有一个配置项
| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| GPT_2_API | 否 | http://127.0.0.1:5000 | GPT-2对应API的地址，一般不需要修改 |
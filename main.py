#调用qianfan接口
import time
import time
import os
from ui_auto_wechat import WeChat
os.environ["QIANFAN_ACCESS_KEY"] = "your_qianfan_access_key"
os.environ["QIANFAN_SECRET_KEY"] = "your_qianfan_secret_key"


if __name__ == "__main__":
    wechat_path = "C:\Program Files\Tencent\WeChat\WeChat.exe"
    wechat = WeChat(wechat_path)
    wechat.zhipuai_key = "zhipuai_key"

    auto_reply_names = ["group1, group2", "friend1, friend2"]
    wechat.set_auto_reply(auto_reply_names)
    wechat.set_retard_list([])
    wechat.check_new_msg()

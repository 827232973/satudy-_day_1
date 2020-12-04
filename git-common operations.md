1、从github 使用gitclone 到本地的分支(master)，在$ git push origin master时弹出框输入用户名、密码，
输入后用户名密码后，界面提示  HttpRequestException encountered
    解决：Github 禁用了TLS v1.0 and v1.1，必须更新Windows的git凭证管理器
    通过此网址 https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/

![](./picture/error1.png)
   
   下载后重启git Bash 命令窗口即可

2、 在$ git push origin master时 报错remote: Invalid username or password

    fatal: Authentication failed for 'https://github.com/ ...
    出现原因：执行命令后，git会弹出一个GitHub登陆的小界面，你登录成功后要求你输入用户名和密码。
    这里的密码并不是你的GitHub的密码或者本地git的密码。
    而是GitHub的Personal access tokens

![](./picture/tips.png)
  
    
   
    
    
    


# easyssh
> 简易免密ssh登录工具


##使用之前需要简单配置
- 安装sshpass
```
 brew install sshpass

```
- 将你的ssh密码保存到下面文件中

```
 vim  ~/.ssh/public_pass
 cat ~/.ssh/public_pass
 admin888
```
- 将essh的bin文件copy到环境变量中
```
cp essh/dist/essh /usr/local/bin/essh
```

- 配置完成

- 开始使用

```
essh 10.10.10.10


essh -h

```
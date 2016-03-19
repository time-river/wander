# wander

## 介绍

用来制造代理池的烂脚本

base.py -- 对 redis-py 的一些封装及通用的一些设置

claw.py -- 负责抓取

filter.py -- 多进程提取代理

proxy.py -- 代理的验证

monitor.py -- 监控进程

## 使用

`$python3.5 monitor.py`

## LICENSE

[MIT license](LICENSE)

## 后记

断断续续捣鼓爬虫三月有余，从 urllib 至 requests，再到现在的 aiohttp。  

我所知到的

在速度方面，还欠缺 Bloom Filter 与集群化爬取。曾想过实现集群，却没有相应的资源，即使实现也属鸡肋，遂罢。而 Bloom Filter 现在也用不到，不予考虑。

不同于速度的发展方向 -- Ajax 异步加载 / 模拟登录 / 反反爬虫 / 验证码识别 / 解析 JavaScrpit 等等，应对策略只有基本常识 -- 提取 Ajax 地址 / session / 代理，后两个还没有做。

到现在这程度，也能满足一般的需求了。现在，还差一个守护进程~

timeline -- 2016/03/16

放弃打造成框架的想法了，准备改造成代理池。
哭了，以后一定经常`$git commit`。

timeline -- 2016/03/18
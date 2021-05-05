# FastAPI-MongoEngine基础框架

## 使用docker启动

学了学Python,用fastapi构建了一套快速开发的框子,默认使用docker启动,使用的是docker中的环境变量配置的数据库,当前框子使用的是mongodb数据库,这是我根据我之前Java-springboot的框子改的,如果之前做java开发,看现在这个框子应该很舒服.


### 启动方式

`docker-compose up -d`



### 启动类在 `main.py` 中 ,初始类在`router.py`,没有数据库可以禁用

## 目录结构

```
│  .gitignore
│  docker-compose.dev.yml
│  docker-compose.prod.yml
│  Dockerfile
│  README.md
│  requirements.txt
│
├─.envs                                      #环境变量
│      .env.dev
│      .env.prod
│
│
├─conf                                       #相关配置
├─log                                        #日志
└─src
    │  main.py                               #启动类
    │
    ├─api                                    #相关api操作
    │  ├─comment
    │  │      welcome_controller.py
    │  │
    │  ├─login                               #登录接口
    │  │      login.py
    │  │
    │  ├─message_controller
    │  │  │  data_type_controller.py
    │  │  │  data_type_default_controller.py
    │  │  │  event_controller.py
    │  │  │  step_controller.py
    │  │  │
    │  │
    ├─config                                 #初始化环境变量配置
    │  │  setting.py
    │  │
    │
    ├─exception                              #自定义异常拦截
    │  │  global_exception.py                #全局异常拦截
    │  │  my_exception.py                    #自定义错误
    │  │  status_code.py                     #常见状态码
    │  │
    │
    ├─mapper                                 #数据库映射层
    │  │  init_db.py
    │  │
    │  ├─model                               #数据库模型mongoengine
    │  │  │  comment.py
    │  │  │  data.py
    │  │  │  data_type.py
    │  │  │  data_type_default.py
    │  │  │  event.py
    │  │  │  event_data.py
    │  │  │  step.py
    │  │  │  user_auth.py
    │  │  │
    │  │
    │  ├─service                             #数据相关操作,对应model
    │  │      event_service.py
    │  │      step_service.py
    │  │
    │
    ├─responsebody                           #统一响应规则
    │      response.py
    │
    ├─router                                 #路由管理,初始化,配置类
    │  │  router.py
    │  │
    │
    ├─test                                   #测试类
    │      test.py
    │
    ├─util                                   #工具类
    │  ├─jwt
    │  │      check_token.py                 #检查token,登录检查
    │  │      create_token.py                #创建token,hash加密
    │  │
    │  └─schedule                            #其他工具类,定时任务等
    │          __init__.py
    │
    ├─validator                              #数据校验,对应model
    │      comment.py
    │      data_type.py
    │      data_type_default.py
    │      event.py
    │      step.py
    │
```
 

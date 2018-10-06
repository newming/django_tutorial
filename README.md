# django 起步

[官方教程](https://docs.djangoproject.com/zh-hans/2.0/intro/)

## 安装 virtualenvwrapper

```bash
pip3 install virtualenvwrapper
```

修改 .zshrc，使得 virtualenvwrapper 生效

```bash
# 告诉 virtualenvwrapper 使用的 python 所在位置，因为本地有两个版本的 python
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
# 创建的虚拟环境放到哪里
export WORKON_HOME='~/.virtualenvs'
source /usr/local/bin/virtualenvwrapper.sh
```

创建支持 django 的虚拟环境

```bash
mkvirtualenv django
workon django
deactivate
```

在 django 虚拟环境下安装 django

```bash
pip install django
```

## 开发

```bash
# 启动项目
python manage.py runserver port
# 创建一个新的应用
python manage.py startapp polls
```

初始化 settings.py 中 INSTALLED_APPS 安装的应用数据库配置

```bash
# 主要是 django 自带的一些应用(admin auth等等)初始化 表 结构
python manage.py migrate

# 对新增的 polls 应用的数据库模型文件进行初始化，会生成 polls/migrations/0001_initial.py 文件
python manage.py makemigrations polls

# 检查项目的问题
python manage.py check
```

进入交互式 Python 命令行：

```bash
python manage.py shell
# 接下来是一大波的数据库操作
# https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial02/#playing-with-the-api
```

## 管理页面

```bash
# 创建管理员账号
python manage.py createsuperuser
# newming woai. 977@qq.com
```

## 测试

编写测试文件 `polls/tests.py`

```bash
python manage.py test polls
```
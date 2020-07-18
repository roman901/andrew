# Andrew

Multi-protocol bot for chats and groupchats with plugin system

### Concepts

#### Connector

When bot is running, it polling/waiting for webhook's events and parsing/processing it to plugins. 

#### Service

Services are isolated components (singletons). They allow plugins and connectors manipulate with data - use DB,
cache them, etc.

Example:
```python
db = DatabaseService()
db.run('SELECT * FROM messages')
```

Services receives configuration from `ConfigurationServer`, which is a mandatory service.
#### Plugin

There is two types of plugins - `core` (bundled and available for everyone) and `external`, which can be loaded by
passing an argument.

Plugin has 
### How to run

Via `docker-compose`:

```shell script
docker-compose up
```

Via `docker`:

```shell script
docker run -t . 
```


Install requirements:

```shell script
pip install -r requirements.txt
```

Run:

```shell script
python run.py
```

### More information

Join us in [telegram](https://t.me/ubuntu_group)

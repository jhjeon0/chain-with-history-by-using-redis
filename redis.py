import redis


class Connection:
    def __init__(self, host: str = "localhost", port: int = 6379, password: str = ""):
        self.client = redis.Redis(host=host, port=port, password=password)

    def connection_check(self):
        return self.client.ping()

    def add_data(self, key: str, value: str):
        return self.client.set(key, value)

    def get_data(self, key: str):
        key_type = self.client.type(key)

        if key_type == b"string":
            return self.client.get(key)
        elif key_type == b"list":
            return self.client.lrange(key, start=0, end=-1)

    def get_key_infos(self):
        return self.client.scan()

    def delete_data(self, key: str):
        return self.client.delete(key)

import cx_Oracle

class DatabaseConnector:
    def __init__(self, host, user, password, database):
        # 初始化连接参数
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        """建立 Oracle 数据库连接"""
        try:
            # 格式为：用户名A/密码@主机:端口/服务名
            dsn = cx_Oracle.makedsn(self.host, 1521, service_name=self.database)  # 1521 是默认端口
            self.conn = cx_Oracle.connect(self.user, self.password, dsn)
            self.cursor = self.conn.cursor()
            print("数据库连接成功")
        except cx_Oracle.Error as err:
            print(f"数据库连接错误: {err}")

    def insert_object_count(self, track_id, class_name, in_count, out_count, detection_time):
        """将对象计数插入到数据库"""
        query = """
        INSERT INTO object_counts (track_id, object_class, in_count, out_count, detection_time)
        VALUES (:1, :2, :3, :4, TO_TIMESTAMP(:5, 'YYYY-MM-DD HH24:MI:SS'))
        """
        self.cursor.execute(query, (track_id, class_name, in_count, out_count, detection_time))
        self.conn.commit()

    def close(self):
        """关闭数据库连接"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

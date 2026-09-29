class ApiClient:

    def __init__(self, base_url,session):
        self.base_url = base_url
        self.session = session

    def get_users(self):
        return self.session.get(f"{self.base_url}/users")

    def get_user(self, user_id):
        return self.session.get(f"{self.base_url}/users/{user_id}")

    def create_post(self,data):
        return self.session.post(f"{self.base_url}/posts", json=data)

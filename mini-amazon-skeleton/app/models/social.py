from flask import current_app as app


class Review:
    def __init__(self,
                 user_id: int,
                 user_name: str,
                 product_id: int,
                 content: str):
        self.user_id = user_id
        self.user_name = user_name
        self.product_id = product_id
        self.content = content

    @staticmethod
    def get_reviews_of_one_product(product_id: int):
        rows = app.db.execute(
            "SELECT uid, CONCAT(firstname, ' ', lastname) AS user_name, pid, content "
            "FROM Reviews "
            "LEFT JOIN Users ON Reviews.uid = Users.id "
            "WHERE Reviews.pid = :product_id ",
            product_id=product_id
        )
        return [Review(*row) for row in rows]

    def __repr__(self) -> str:
        return f"{self.user_name} ({self.user_id}) says: \n" + \
            f"{self.content}" + \
            f"for product {self.product_id}"

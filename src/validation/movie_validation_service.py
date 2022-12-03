class MovieValidationService:

    @staticmethod
    def validate_title(title: str):
        if not title.isalpha():
            raise Exception('Title is invalid.')
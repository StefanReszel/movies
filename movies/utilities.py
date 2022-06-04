from sqlalchemy.exc import SQLAlchemyError


ERROR_MESSAGE = "Wystąpił błąd, spróbuj ponownie."


def add_obj_to_db(db, obj):
    try:
        db.session.add(obj)
        db.session.commit()
    except SQLAlchemyError as error:
        error.message = ERROR_MESSAGE
        return error
